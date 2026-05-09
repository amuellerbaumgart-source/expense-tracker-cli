"""SQLite storage for expenses. Creates the DB and table if they don't exist."""

import sqlite3
from pathlib import Path

# Store DB next to this file
DB_PATH = Path(__file__).parent / "expenses.db"


def get_connection():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # access columns by name
    return conn


def init_db():
    """Create the expenses table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                note TEXT,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)


def add_expense(amount: float, category: str, date: str, note: str = "") -> int:
    """Insert one expense. Returns the new row id."""
    init_db()
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
            (amount, category.strip(), date, (note or "").strip()),
        )
        conn.commit()
        return cur.lastrowid


def get_all_expenses():
    """Return all expenses as list of dict-like rows (newest first)."""
    init_db()
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, amount, category, date, note, created_at FROM expenses ORDER BY date DESC, id DESC"
        ).fetchall()
    return [dict(r) for r in rows]


def delete_expense(expense_id: int) -> bool:
    """Delete one expense by id. Returns True if a row was deleted."""
    init_db()
    with get_connection() as conn:
        cur = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        return cur.rowcount > 0
