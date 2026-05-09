"""Print all expenses from the database (see your data)."""

from database import get_all_expenses, init_db


def main():
    init_db()
    rows = get_all_expenses()

    if not rows:
        print("No expenses yet. Run input_expense.py to add some.")
        return

    print(f"{'ID':<6} {'Date':<12} {'Category':<14} {'Amount':>10}  Note")
    print("-" * 60)
    for r in rows:
        note = (r["note"] or "")[:30]
        print(f"{r['id']:<6} {r['date']:<12} {r['category']:<14} ${r['amount']:>9,.2f}  {note}")

    print("-" * 60)
    total = sum(r["amount"] for r in rows)
    print(f"{'Total':<34} ${total:>9,.2f}")


if __name__ == "__main__":
    main()
