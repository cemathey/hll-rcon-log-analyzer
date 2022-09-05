import csv
from pathlib import Path

import pandas as pd
import typer

from hll_rcon_log_analyzer.config import config
from hll_rcon_log_analyzer.constants import (
    COMMUNITY_RCON_CONTENT_PATTERNS,
    PROJECT_ROOT_PATH,
)
from hll_rcon_log_analyzer.malfeasance import find_admin_cam_abuse
from hll_rcon_log_analyzer.utils import find_not_existing_file, load_logs

app = typer.Typer()

# Make flake8 happy about function calling in argument defaults
path: str = typer.Argument(..., help="Path to the input rcon log file.")
output: str = typer.Option(
    "console", help="Output format, valid options are console or csv."
)
output_path: str = typer.Option(
    "", help=f"Filename to write, defaults to {PROJECT_ROOT_PATH}/output/output.csv."
)
field_separator: str = typer.Option(
    ", ", help="Field separator to use when printing to the console."
)


@app.command()
def admin_cam_abuse(
    path: str = path,
    output: str = output,
    output_path: str = output_path,
    field_separator: str = field_separator,
):
    """Search the given log file for admin camera abuse as defined in the config."""
    df = load_logs(path, COMMUNITY_RCON_CONTENT_PATTERNS)
    converted_path = Path(output_path)
    collected_events: list[pd.DataFrame] = find_admin_cam_abuse(df, config)

    if output == "console":
        fields = config["output"]["console"]
        for row in collected_events:
            values = [str(row[field]) for field in fields]
            print(field_separator.join(values))
    elif output == "csv":
        if output_path == "":
            converted_path = find_not_existing_file("output", format="csv")

        converted_path.parents[0].mkdir(parents=True, exist_ok=True)

        with open(converted_path, "w+") as fp:
            csv_writer = csv.writer(fp, dialect="excel")
            csv_writer.writerows(collected_events)


if __name__ == "__main__":
    app()
