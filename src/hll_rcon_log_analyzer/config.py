from pathlib import Path

import tomli

from hll_rcon_log_analyzer.constants import (
    COMMUNITY_RCON_LOG_ACTIONS,
    CONFIG_FILE_DIR_NAME,
    CONFIG_FILE_NAME,
    PROJECT_ROOT_PATH,
)

full_path = Path(PROJECT_ROOT_PATH) / CONFIG_FILE_DIR_NAME / CONFIG_FILE_NAME

with open(full_path, mode="rb") as fp:
    config = tomli.load(fp)

    for event in (
        config["admin_cam_abuse"]["selected_events"]
        + config["admin_cam_abuse"]["clearing_events"]
    ):
        if event not in COMMUNITY_RCON_LOG_ACTIONS:
            raise ValueError(f"{event} in {full_path} is not a valid log action.")
