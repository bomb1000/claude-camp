"""Analyze student CSV data and save a JSON summary."""

import csv
import json
from pathlib import Path


REQUIRED_COLUMNS = {"name", "email", "joined_date", "country", "bet_status"}


def load_students(csv_path):
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
        return [clean_row(row) for row in reader if any(row.values())]


def clean_row(row):
    return {
        "name": row["name"].strip(),
        "email": row["email"].strip(),
        "joined_date": row["joined_date"].strip(),
        "country": row["country"].strip() or "Unknown",
        "bet_status": row["bet_status"].strip().lower(),
    }


def build_report(students):
    total = len(students)
    country_counts = {}
    completed = 0

    for student in students:
        country = student["country"]
        country_counts[country] = country_counts.get(country, 0) + 1
        if student["bet_status"] == "completed":
            completed += 1

    completion_rate = round(completed / total, 2) if total else 0
    return {
        "total_students": total,
        "country_counts": dict(sorted(country_counts.items())),
        "completed_bet_count": completed,
        "completion_rate": completion_rate,
    }


def save_report(report, output_path):
    with Path(output_path).open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)


def main():
    students = load_students("students.csv")
    report = build_report(students)
    save_report(report, "report.json")
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
