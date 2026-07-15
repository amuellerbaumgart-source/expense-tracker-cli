# Expense Tracker (CLI + SQLite + charts)

Personal finance tooling that persists expenses in **SQLite**, exposes a small **Python CLI**, and supports **matplotlib** summaries plus a **Jupyter** workflow for exploratory analysis—useful as a standalone app or as a data pipeline starter.

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
