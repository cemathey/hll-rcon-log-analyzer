from pathlib import Path

PROJECT_ROOT_PATH = Path(__file__).parent.parent.parent
CONFIG_FILE_NAME = "hll_rcon_log_analyzer.toml"
CONFIG_FILE_DIR_NAME = "config"


# Needs to stay in sync with
# https://github.com/MarechJ/hll_rcon_tool/blob/master/rcon/extended_commands.py
COMMUNITY_RCON_LOG_ACTIONS = [
    "ADMIN BANNED",
    "ADMIN KICKED",
    "CHAT",
    "CHAT[Allies]",
    "CHAT[Allies][Team]",
    "CHAT[Allies][Unit]",
    "CHAT[Axis]",
    "CHAT[Axis][Team]",
    "CHAT[Axis][Unit]",
    "CONNECTED",
    "DISCONNECTED",
    "KILL",
    "MATCH ENDED",
    "MATCH START",
    "MATCH",
    "TEAM KILL",
    "TEAMSWITCH",
    "TK AUTO BANNED",
    "TK AUTO KICKED",
    "TK AUTO",
    "VOTE COMPLETED",
    "VOTE STARTED",
    "VOTE",
]

COMMUNITY_RCON_CSV_HEADERS = [
    "event_time",
    "type",
    "player1_name",
    "player1_id",
    "player2_name",
    "player2_id",
    "content",
    "server",
    "weapon",
]

COMMUNITY_RCON_CONTENT_PATTERNS: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        r"^(?:KICK|BAN): \[.+\] has been (?:kicked|banned)\. \[(.+?)\]{0,1}$",
        ("admin_action_message",),
    ),
    (
        r"MATCH START (.+) (WARFARE|OFFENSIVE|)",
        ("map_name", "match_type"),
    ),
    (
        r"MATCH ENDED `(.+) (WARFARE|OFFENSIVE|)` (ALLIED|AXIS) \((\d) - (\d)\) (\w+)",
        ("map_name", "match_type", "map_score_allied", "map_score_axis"),
    ),
    (
        r"\[\w+ \((\d+)\)\] (Entered Admin Camera|Left Admin Camera)",
        ("player1_steamid64", "camera_event_type"),
    ),
    # Kill / Team Kill
    (
        r".+?(?:\(Allies|Axis)\/(\d+)\) -> .+?\((?:Allies|Axis)\/(\d+)\)",
        (
            "player1_steamid64",
            "player2_steamid64",
        ),
    ),
    # Chat
    (r"^.+?:(.*) \((\d+)\)$", ("chat_message", "player1_steamid64")),
    (
        r"^TEAMSWITCH (.+) \((\w+) > (\w+)\)$",
        ("player1_name", "team_switch_from", "team_switch_to"),
    ),
)


ENTERED_CAMERA = "Entered Admin Camera"
LEFT_CAMERA = "Left Admin Camera"
