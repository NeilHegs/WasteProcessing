import sqlite3
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

SCHEMA = """
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent TEXT NOT NULL,
    category TEXT NOT NULL,
    title TEXT NOT NULL,
    summary TEXT NOT NULL,
    details TEXT,
    source TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""


@dataclass
class Report:
    agent: str
    category: str
    title: str
    summary: str
    details: str = ""
    source: str = ""


def init_db(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as connection:
        connection.executescript(SCHEMA)


def save_report(db_path: Path, report: Report) -> None:
    with sqlite3.connect(db_path) as connection:
        connection.execute(
            "INSERT INTO reports (agent, category, title, summary, details, source) VALUES (?, ?, ?, ?, ?, ?)",
            (report.agent, report.category, report.title, report.summary, report.details, report.source),
        )
        connection.commit()


def list_reports(db_path: Path) -> Iterable[Report]:
    with sqlite3.connect(db_path) as connection:
        cursor = connection.execute("SELECT agent, category, title, summary, details, source FROM reports ORDER BY created_at DESC")
        for row in cursor.fetchall():
            yield Report(*row)


def summarize_reports(db_path: Path) -> str:
    reports = list(list_reports(db_path))
    return f"{len(reports)} report(s) stored in {db_path}."
