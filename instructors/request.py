import sqlite3
import json
from models import Instructor

def get_all_instructors():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            i.id,
            i.name
        FROM Instructor i
        """)

        instructors = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            instructor = Instructor(row['id'], row['name'])
            instructors.append(instructor.__dict__)

    return json.dumps(instructors)

def get_single_instructor(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            i.id,
            i.name
        FROM Instructor i
        WHERE id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        instructor = Instructor(data['id'], data['name'])
    return json.dumps(instructor.__dict__)