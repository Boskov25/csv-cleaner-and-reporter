import argparse
from pathlib import Path
import pandas as pd

from cleaners import normalize_columns, basic_cleaning
from validators import validate_required_columns, find_duplicates
from report import build_report


def read_input_file(input_path, sheet=None):
    p = Path(input_path)

    if p.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(p, sheet_name=sheet, engine="openpyxl")
    elif p.suffix.lower() == ".csv":
        return pd.read_csv(p)
    else:
        raise ValueError("Unsupported file type")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--report", required=True)

    args = parser.parse_args()

    df = read_input_file(args.input)

    df = normalize_columns(df)
    df = basic_cleaning(df)

    errors = validate_required_columns(df, ["account_number", "name", "email"])
    dups = find_duplicates(df, ["account_number"])

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)

    text = build_report(len(df), errors, dups)

    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(text)

    print("Done")


if __name__ == "__main__":
    main()
