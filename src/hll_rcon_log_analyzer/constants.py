from pathlib import Path

PROJECT_ROOT_PATH = Path(__file__).parent.parent.parent

CONFIG_FILE_NAME = "hll_rcon_log_analyzer.toml"

# Needs to stay in sync with
# https://github.com/MarechJ/hll_rcon_tool/blob/master/rcon/extended_commands.py
LOG_ACTIONS = [
    "DISCONNECTED",
    "CHAT[Allies]",
    "CHAT[Axis]",
    "CHAT[Allies][Unit]",
    "KILL",
    "CONNECTED",
    "CHAT[Allies][Team]",
    "CHAT[Axis][Team]",
    "CHAT[Axis][Unit]",
    "CHAT",
    "VOTE COMPLETED",
    "VOTE STARTED",
    "VOTE",
    "TEAMSWITCH",
    "TK AUTO",
    "TK AUTO KICKED",
    "TK AUTO BANNED",
    "ADMIN KICKED",
    "ADMIN BANNED",
    "MATCH",
    "MATCH START",
    "MATCH ENDED",
]

COMMUNITY_RCON_CSV_HEADERS = [
    "event_time",
    "type",
    "player_name",
    "player1_id",
    "player2_name",
    "player2_id",
    "content",
    "server",
    "weapon",
]
