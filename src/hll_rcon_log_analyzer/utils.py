"""Common utility functions such as parsing RCON log csv files."""
import pandas as pd


def load_logs(file_path: str) -> pd.DataFrame:
    """Return a dataframe from the given path to a historical log file from community RCON."""
    with open(file_path) as csvfile:
        df = pd.read_csv(csvfile, parse_dates=["event_time"])

    return df
