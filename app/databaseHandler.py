import sqlite3
from contextlib import closing

DATABASE = "database/data.db"

def init_db():
    with closing(sqlite3.connect(DATABASE)) as db:
        with db as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS clicks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    count INTEGER NOT NULL,
                    name  TEXT
                )
                """
            )
            cursor.execute(
                """
                INSERT INTO clicks (count) VALUES (0)
                """
            )

def get_click_count():
    with closing(sqlite3.connect(DATABASE)) as db:
        with db:
            cursor = db.cursor()
            cursor.execute("SELECT count FROM clicks WHERE id=1")
            return cursor.fetchone()[0]

def update_click_count(new_count):
    with closing(sqlite3.connect(DATABASE)) as db:
        with db:
            cursor = db.cursor()
            cursor.execute("UPDATE clicks SET count = ? WHERE id = 1", (new_count,))

def set_name(id, name):
    with closing(sqlite3.connect(DATABASE)) as db:
        with db:
            cursor = db.cursor()
            cursor.execute(f'UPDATE clicks SET name = ? WHERE id = {id}', (name,))

def get_user_by_id(id):
    with closing(sqlite3.connect(DATABASE)) as db:
        with db:
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM clicks WHERE id={id}")
            return cursor.fetchall()