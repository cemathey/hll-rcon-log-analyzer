[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Important!
You need to put column headers in your log files for now, `event_time,type,player1_name,player1_id,player2_name,player2_id,content,server,weapon` needs to be the first row.

# hll-rcon-log-analyzer

A tool to analyze Hell Let Loose RCON logs to identify interesting or suspicious behavior such as admin camera abuse. Only admin camera abuse is currently implemented.

# Introduction

Currently this only works with log files from the community open source version of RCON found here: https://github.com/MarechJ/hll_rcon_tool

If you run a different version of RCON and would like to use it open a github issue or email me and include some sample logs and I'll work on adding support for it.

Configuration is handled by [TOML](https://toml.io/en/) and command line options.

A sample file you can test the tool with is in `./data/sample_abuse.csv`

# Special Considerations

This tool is not guaranteed to be bug free, if this flags suspicious behavior please manually investigate it before starting a witch hunt. This tool is intended to be an investigative tool, not a definitive judgement.

If your log files start part of the way through a match you may get incorrect or misleading results.

# Installation

1. git clone https://github.com/cemathey/hll-rcon-log-analyzer.git
2. cd hll-rcon-log-analyzer/
3. poetry install

# Configuration

Edit `config/hll_rcon_log_analyzer.toml` as desired. This comes with sensible defaults.

# Running It

- Getting help: `poetry run python src/hll_rcon_log_analyzer/console.py --help`
- Checking a log file: `poetry run python src/hll_rcon_log_analyzer/console.py src/sample_abuse.csv`
- Saving results to a csv file: `poetry run python src/hll_rcon_log_analyzer/console.py --output csv --output-path ./output/bad_people.csv data/sample_abuse.csv`

# Contributing

Please run `nox` and do your best to fix any linting/type checking issues before submitting pull requests.
Tests are great and preferred as well, however currently I have none implemented.
