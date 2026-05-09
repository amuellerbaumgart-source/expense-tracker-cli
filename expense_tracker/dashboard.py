"""Dashboard: text summary. For pie/bar charts run charts.py."""

from analysis import get_by_category, get_by_month, get_recent_expenses, get_total_spending


def main():
    total = get_total_spending()
    by_cat = get_by_category()
    by_month = get_by_month()
    recent = get_recent_expenses(5)

    print("=== Expense summary ===\n")
    print(f"Total spent: ${total:,.2f}\n")

    print("By category:")
    for row in by_cat:
        print(f"  {row['category']}: ${row['total']:,.2f}")
    if not by_cat:
        print("  (no expenses yet)")

    print("\nBy month:")
    for row in by_month:
        print(f"  {row['month']}: ${row['total']:,.2f}")
    if not by_month:
        print("  (no expenses yet)")

    print("\nLast 5 expenses:")
    for row in recent:
        print(f"  {row['date']} | {row['category']} | ${row['amount']:,.2f} | {row['note'] or '-'}")
    if not recent:
        print("  (no expenses yet)")


if __name__ == "__main__":
    main()
