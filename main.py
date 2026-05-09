"""Project entry — convenience hints for the expense tracker CLI."""

from __future__ import annotations


def main() -> None:
    print(
        "Expense Tracker\n"
        "\n"
        "  Add expenses:       python -m expense_tracker.input_expense\n"
        "  View (text):       python -m expense_tracker.dashboard\n"
        "  Charts:            python -m expense_tracker.charts\n"
        "  Export CSV:        python -m expense_tracker.export_to_csv\n"
        "\n"
        "See README.md for setup (venv + pip install -r requirements.txt)."
    )


if __name__ == "__main__":
    main()
