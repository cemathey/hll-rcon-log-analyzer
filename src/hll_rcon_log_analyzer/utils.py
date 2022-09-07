"""Common utility functions such as parsing RCON log csv files."""
from itertools import count
from pathlib import Path
import re
from typing import Optional

import pandas as pd

from hll_rcon_log_analyzer.constants import (
    PROJECT_ROOT_PATH,
    COMMUNITY_RCON_CSV_HEADERS,
)


def find_not_existing_file(name: str, format: str, dir: Optional[Path] = None) -> Path:
    """Find a safe filename to write if the given file already exists."""
    dir = dir or Path(PROJECT_ROOT_PATH) / "output"

    test_path = Path(dir) / f"{name}.{format}"

    if test_path.exists():
        for i in count(1):
            test_path = Path(dir) / f"{name}_{i}.{format}"
            if not test_path.exists():
                break

    return test_path


# Return a tuple of extracted fields tuple and column names tuple
def parse_content_line(
    content: str, patterns: tuple[tuple[str, tuple[str, ...]], ...]
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Parse an RCON `content` field and return fields and column names."""

    for p, column_names in patterns:
        if match := re.match(p, content):
            return (match.groups(), column_names)

    raise ValueError(f"{content=} not found")


def parse_contents(df: pd.DataFrame, patterns: tuple[tuple[str, tuple[str, ...]], ...]):
    """Extract fields from the `content` column and update the dataframe in place."""
    # These columns don't have a content field and shouldn't be parsed
    empty_content_column_names = ("CONNECTED", "DISCONNECTED")

    for idx, row in df.iterrows():
        if row["type"] not in empty_content_column_names:
            values, headers = parse_content_line(row["content"], patterns)
            for v, h in zip(values, headers):
                df.loc[idx, h] = v


def load_logs(file_path: str, patterns) -> pd.DataFrame:
    """Return a dataframe from the given path to a log file from community RCON."""
    with open(file_path) as csvfile:
        df = pd.read_csv(
            csvfile,
            parse_dates=["event_time"],
            header=None,
            names=COMMUNITY_RCON_CSV_HEADERS,
            dtype={
                "player1_name": str,
                "player1_id": str,
                "player2_name": str,
                "player2_id": str,
                "content": str,
                "server": int,
                "weapon": str,
            },
        )

    parse_contents(df, patterns)
    df.sort_values("event_time", inplace=True)

    return df
