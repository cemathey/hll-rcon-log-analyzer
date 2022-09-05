from pathlib import Path

PROJECT_ROOT_PATH = Path(__file__).parent.parent.parent

CONFIG_FILE_NAME = "hll_rcon_log_analyzer.toml"

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
    "TEAM KILL" "TEAMSWITCH",
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
