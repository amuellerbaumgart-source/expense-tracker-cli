# Expense Tracker (CLI + SQLite + charts)

Personal finance tooling that persists expenses in **SQLite**, exposes a small **Python CLI**, and supports **matplotlib** summaries plus a **Jupyter** workflow for exploratory analysis—useful as a standalone app or as a data pipeline starter.

---

## Why it’s portfolio-friendly

- **End-to-end data path:** input → relational storage → aggregations → optional CSV/notebook analytics.
- **Readable structure:** separation between persistence (`database`), analytics (`analysis`), UX (`dashboard`, `charts`), and I/O (`input_expense`, `export_to_csv`).
- **Shows practical skills:** SQL via `sqlite3`, CLI modules, reproducible installs (`requirements.txt`).

> **Tip:** After your first commits, add 1–2 screenshots (dashboard output, a chart figure) under `docs/` and link them here—recruiters scan visuals quickly.

---

## Tech stack

| Area        | Choice                          |
|------------|----------------------------------|
| Language   | Python 3                         |
| Storage    | SQLite (`sqlite3`)               |
| Charts     | matplotlib                       |
| Notebooks  | pandas (CSV/SQL loads)           |

---

## Features

- Add, view, delete expenses via CLI scripts.
- Text dashboard: totals, breakdowns by category and month, recent entries.
- Pie and bar charts by category/month.
- Export database to CSV for notebooks or downstream pipelines.
- Example notebook showing CSV and SQLite loading patterns.

---

## Quick start

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Add data (Enter on amount to quit):

```bash
python -m expense_tracker.input_expense
```

Summaries:

```bash
python -m expense_tracker.dashboard    # text
python -m expense_tracker.charts       # matplotlib windows
python -m expense_tracker.export_to_csv  # refresh CSV for Jupyter
```

Open `expense_tracker/load_expense_data.ipynb` after exporting CSV or point it at `expenses.db`.

---

## Project layout

```
.
├── expense_tracker/
│   ├── database.py           # SQLite schema + helpers
│   ├── input_expense.py      # Interactive entry
│   ├── view_expenses.py / delete_expense.py
│   ├── analysis.py          # Aggregation queries
│   ├── dashboard.py         # CLI text summary
│   ├── charts.py            # matplotlib
│   ├── export_to_csv.py     # DB → CSV
│   └── load_expense_data.ipynb
├── main.py                   # Minimal entry banner / hints
├── requirements.txt
└── README.md
```

The database (`expenses.db`) and export (`expenses.csv`) are gitignored so your real spending never lands in Git history.

---

## GitHub checklist (portfolio polish)

1. **Repository visibility:** Public, clear name (`expense-tracker-cli` or similar).
2. **Topics/tags:** Add e.g. `python`, `sqlite`, `pandas`, `matplotlib`, `cli`, `jupyter-notebook`.
3. **Pinned README section:** Lead with “What I built” in 2 sentences (mirror the opening here if you like).
4. **Optional:** GitHub Actions (lint/format on PR) shows engineering habits—only add when you want that signal.
