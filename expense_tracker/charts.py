"""Pie and bar charts for expenses. Run this file to display charts."""

import matplotlib.pyplot as plt

from analysis import get_by_category, get_by_month


def _ensure_data(message: str = "Add some expenses first, then run again."):
    by_cat = get_by_category()
    if not by_cat:
        print(message)
        return None
    return by_cat


def plot_pie_by_category():
    """Show a pie chart of spending by category."""
    by_cat = _ensure_data()
    if not by_cat:
        return

    labels = [r["category"] for r in by_cat]
    sizes = [r["total"] for r in by_cat]
    colors = plt.cm.Set3.colors[: len(labels)]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
    ax.set_title("Spending by category")
    plt.tight_layout()
    plt.show()


def plot_bar_by_category():
    """Show a horizontal bar chart of spending by category."""
    by_cat = _ensure_data()
    if not by_cat:
        return

    categories = [r["category"] for r in by_cat]
    totals = [r["total"] for r in by_cat]
    color = plt.cm.Blues(0.6)

    fig, ax = plt.subplots(figsize=(8, max(4, len(categories) * 0.4)))
    bars = ax.barh(categories, totals, color=color)
    ax.set_xlabel("Amount ($)")
    ax.set_title("Spending by category")
    ax.bar_label(bars, fmt="${:,.0f}")
    plt.tight_layout()
    plt.show()


def plot_bar_by_month():
    """Show a bar chart of spending by month."""
    by_month = get_by_month()
    if not by_month:
        print("Add some expenses first, then run again.")
        return

    months = [r["month"] for r in reversed(by_month)]  # oldest to newest
    totals = [r["total"] for r in reversed(by_month)]
    color = plt.cm.Greens(0.6)

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(months, totals, color=color)
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount ($)")
    ax.set_title("Spending by month")
    plt.xticks(rotation=45, ha="right")
    ax.bar_label(bars, fmt="${:,.0f}")
    plt.tight_layout()
    plt.show()


def main():
    """Show pie chart and bar charts."""
    by_cat = get_by_category()
    by_month = get_by_month()

    if not by_cat:
        print("No expenses yet. Add some with input_expense.py, then run again.")
        return

    print("Opening charts (close each window to see the next)...")
    plot_pie_by_category()
    plot_bar_by_category()

    if by_month:
        plot_bar_by_month()


if __name__ == "__main__":
    main()
