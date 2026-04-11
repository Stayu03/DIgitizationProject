#!/usr/bin/env python3
"""Reset SQLite database and seed initial records."""

from pathlib import Path

from database import DEFAULT_DB_PATH, run_startup


def main() -> None:
    db_path = Path(DEFAULT_DB_PATH)
    if db_path.exists():
        db_path.unlink()
        print(f"Deleted existing database: {db_path}")

    conn = run_startup(str(db_path))

    user_count = conn.execute("SELECT COUNT(*) AS total FROM users").fetchone()["total"]
    doc_count = conn.execute("SELECT COUNT(*) AS total FROM documents").fetchone()["total"]
    tracking_count = conn.execute("SELECT COUNT(*) AS total FROM process_tracking").fetchone()["total"]
    conn.close()

    print("Database has been reset and seeded successfully.")
    print(f"users={user_count}, documents={doc_count}, process_tracking={tracking_count}")


if __name__ == "__main__":
    main()
