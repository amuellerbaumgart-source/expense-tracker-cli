"""Queries for dashboards and reports. Returns data ready for charts/tables."""

from database import get_connection, init_db


def get_total_spending():
    """Total amount spent (all time)."""
    init_db()
    with get_connection() as conn:
        row = conn.execute("SELECT COALESCE(SUM(amount), 0) AS total FROM expenses").fetchone()
    return row["total"]


def get_by_category():
    """Spending per category: list of {category, total}."""
    init_db()
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            GROUP BY category
            ORDER BY total DESC
            """
        ).fetchall()
    return [dict(r) for r in rows]


def get_by_month():
    """Spending per month: list of {month, total}. Month format YYYY-MM."""
    init_db()
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT strftime('%Y-%m', date) AS month, SUM(amount) AS total
            FROM expenses
            GROUP BY month
            ORDER BY month DESC
            """
        ).fetchall()
    return [dict(r) for r in rows]


def get_recent_expenses(limit: int = 10):
    """Last N expenses for a recent-activity view."""
    init_db()
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, amount, category, date, note
            FROM expenses
            ORDER BY date DESC, id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return [dict(r) for r in rows]
