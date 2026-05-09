"""Export all expenses from SQLite to a CSV file for analysis or ML."""

import csv
from pathlib import Path

from database import get_all_expenses, init_db

# CSV next to this file
CSV_PATH = Path(__file__).parent / "expenses.csv"


def export_csv(path: Path | None = None) -> Path:
    """Write all expenses to a CSV. Returns the path used. Default: expenses.csv in this folder."""
    path = path or CSV_PATH
    init_db()
    rows = get_all_expenses()

    if not rows:
        raise ValueError("No expenses in the database. Add some with input_expense.py first.")

    fieldnames = ["id", "amount", "category", "date", "note", "created_at"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    return path


def main():
    try:
        out = export_csv()
        print(f"Exported {out.stat().st_size} bytes to {out}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
