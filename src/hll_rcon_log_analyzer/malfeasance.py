"""Contains high level functions to identify potentially malicious behavior in logs."""
from dataclasses import dataclass
import datetime

import pandas as pd

from hll_rcon_log_analyzer.constants import ENTERED_CAMERA


@dataclass
class PlayerCameraState:
    in_camera: bool
    cleared: bool
    camera_timestamp: pd.Timestamp


def find_admin_cam_abuse(df: pd.DataFrame, config):
    """Analyze the provided logs identifying potential admin cam abuse for human review.

    Admin cam abuse is defined as a camera event that is followed by one or more
    configurable selected events (e.g. kills, team kills) before encountering a
    clearing event (e.g. a map change or expiration of a time period).
    """
    print("Finding abuse:")
    selected_events = config["admin_cam_abuse"]["selected_events"]
    clearing_events = config["admin_cam_abuse"]["clearing_events"]
    clearing_time_delta = datetime.timedelta(
        seconds=config["admin_cam_abuse"]["timeout"]["seconds"],
        minutes=config["admin_cam_abuse"]["timeout"]["minutes"],
        hours=config["admin_cam_abuse"]["timeout"]["hours"],
    )

    # Tracks time between exiting the camera and a selected event
    df["camera_delta"] = None
    state: dict[str, PlayerCameraState] = {}

    collected_events = []
    camera_events = []
    abuse_events = []

    for _, row in df.iterrows():
        player_name: str = row["player1_name"]
        event_type: str = row["type"]

        # Set defaults for a player if we haven't seen them before
        state_for_row = state.get(
            player_name,
            PlayerCameraState(
                in_camera=False,
                cleared=False,
                camera_timestamp=pd.Timestamp(year=2016, month=1, day=1),
            ),
        )

        camera_delta = row["event_time"] - state_for_row.camera_timestamp

        if event_type == "CAMERA":
            # Doing it this way instead of toggling state in case we're missing log lines
            if row["camera_event_type"] == ENTERED_CAMERA:
                state_for_row.in_camera = True
            else:
                state_for_row.in_camera = False
            state_for_row.camera_timestamp = row["event_time"]
            camera_events.append(row)
        elif (
            event_type in selected_events
            and not state_for_row.cleared
            and camera_delta < clearing_time_delta
        ):
            row["camera_delta"] = camera_delta
            abuse_events.append(row)
        elif event_type in clearing_events:
            state_for_row.cleared = True

        state[player_name] = state_for_row

    if abuse_events:
        collected_events = abuse_events + camera_events
        collected_events = sorted(collected_events, key=lambda row: row["event_time"])

    return collected_events
