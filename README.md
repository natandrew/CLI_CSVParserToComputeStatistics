# CLI_CSVParserToComputeStatistics

**Compute summary statistics (mean, median, mode) for a numeric column in a CSV file via a simple command-line interface.**

This repository contains a small, dependency-light Python CLI tool that reads a CSV file and computes summary statistics for a specified numeric column.

---

## Features

* Read CSV files with an arbitrary delimiter.
* Compute **count**, **mean**, **median**, and **mode** (if a unique mode exists) for a chosen numeric column.
* Graceful handling of missing or non-numeric values (they are skipped).
* Clear CLI with friendly error messages.

---

## Requirements

* Python 3.7+ (uses the standard library only: `argparse`, `csv`, `statistics`).

No external packages required.

---

## Installation

Clone the repository and (optionally) create a virtual environment:

```bash
git clone https://github.com/natandrew/CLI_CSVParserToComputeStatistics.git
cd CLI_CSVParserToComputeStatistics
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# No third-party deps to install; the tool uses the Python standard library.
```

---

## Usage

The main script is `CSVParser/Sales.py` and expects the path to a CSV file plus the name of the numeric column to analyze.

Basic usage pattern:

```bash
python CSVParser/Sales.py FILE --column COLUMN_NAME [--delimiter DELIM]
```

### Arguments

* `FILE` (positional): Path to the input CSV file.
* `--column` / `-c` (required): Name of the numeric column to analyze (must match a header in the CSV).
* `--delimiter` / `-d`: CSV delimiter (default is `,`).

### Examples

Analyze a `Price` column in a comma‑separated file:

```bash
python CSVParser/Sales.py data/sales.csv --column Price
```

If your CSV uses a semicolon delimiter:

```bash
python CSVParser/Sales.py data/sales_semicolon.csv --column Price --delimiter ";"
```

If the requested column is not found the script exits with a helpful message indicating available headers. Non-numeric or missing cells are skipped automatically when computing statistics.

### Example output

```
Summary statistics for column 'Price' on file 'data/sales.csv':
  Count : 120
  Mean  : 23.45
  Median: 19.99
  Mode  : 9.99
```

If there is no unique mode, the script prints `Mode  : None (no unique mode)`.

---

## Expected CSV format

A typical CSV file with a header row works best. Example:

```csv
Date,Item,Category,Price,Quantity
2023-01-01,Widget A,Hardware,19.99,2
2023-01-02,Widget B,Hardware,29.99,1
```

The tool will ignore non-numeric entries in the selected column.

---

## Error handling

* If the file cannot be opened, the script exits with `Error: File not found: <path>`.
* If the specified column is not found in the header, the script exits with `Error: Column '<name>' not found in CSV headers: [...]`.
* If no numeric values are found in the column, the script exits with `Error: No numeric data found to analyze.`

---

## Tests

No automated tests included yet. Suggested quick test using a small CSV:

1. Create `tests/sample.csv` with a known numeric column.
2. Run the script and verify printed values match manual calculations.

Consider adding `pytest`‑style unit tests for `read_values` and `compute_stats`.

---

## License

This project is released under the **AGPL‑3.0** license (see `LICENSE`).

---

## Contact

Created by Nat Andrew.
I'm open to contract and full-time opportunities. Connect with me on LinkedIn: [Nat Andrew](https://www.linkedin.com/in/natandrew).

