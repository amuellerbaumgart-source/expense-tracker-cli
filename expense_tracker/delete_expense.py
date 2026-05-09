"""Delete an expense by ID. Shows recent expenses so you can pick the ID."""

from database import delete_expense, get_all_expenses, init_db


def main():
    init_db()
    rows = get_all_expenses()

    if not rows:
        print("No expenses in the database.")
        return

    print("Recent expenses (use ID to delete):\n")
    print(f"{'ID':<6} {'Date':<12} {'Category':<14} {'Amount':>10}  Note")
    print("-" * 60)
    for r in rows[:15]:
        note = (r["note"] or "")[:25]
        print(f"{r['id']:<6} {r['date']:<12} {r['category']:<14} ${r['amount']:>9,.2f}  {note}")

    print()
    try:
        raw = input("Enter expense ID to delete (or Enter to cancel): ").strip()
        if not raw:
            print("Cancelled.")
            return
        expense_id = int(raw)
    except ValueError:
        print("Enter a number.")
        return

    if delete_expense(expense_id):
        print(f"Deleted expense #{expense_id}.")
    else:
        print(f"No expense with ID {expense_id}.")


if __name__ == "__main__":
    main()
