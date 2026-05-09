"""Enter new expenses from the command line."""

from datetime import date

from database import add_expense, init_db


def main():
    init_db()
    print("Add an expense (leave amount empty to quit)\n")

    while True:
        try:
            amount_str = input("Amount: ").strip()
            if not amount_str:
                break
            amount = float(amount_str)
        except ValueError:
            print("Enter a valid number.\n")
            continue

        category = input("Category (e.g. Food, Transport): ").strip() or "Other"
        date_str = input("Date (YYYY-MM-DD, Enter = today): ").strip()
        if not date_str:
            date_str = str(date.today())
        note = input("Note (optional): ").strip()

        row_id = add_expense(amount, category, date_str, note)
        print(f"Saved expense #{row_id}\n")


if __name__ == "__main__":
    main()
