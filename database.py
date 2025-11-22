import sqlite3
import json
from datetime import datetime

DB_NAME = 'salary_tracker.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                income REAL NOT NULL,
                deductions TEXT NOT NULL, -- JSON string
                in_hand REAL NOT NULL
            )
        ''')
    conn.close()

def add_entry(date, income, deductions, in_hand):
    conn = get_db_connection()
    with conn:
        conn.execute('''
            INSERT INTO entries (date, income, deductions, in_hand)
            VALUES (?, ?, ?, ?)
        ''', (date, income, json.dumps(deductions), in_hand))
    conn.close()

def get_all_entries():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM entries ORDER BY date DESC').fetchall()
    conn.close()
    
    # Convert rows to dicts and parse JSON
    results = []
    for row in entries:
        entry = dict(row)
        entry['deductions'] = json.loads(entry['deductions'])
        results.append(entry)
    return results

def delete_entry(entry_id):
    conn = get_db_connection()
    with conn:
        conn.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
    conn.close()

def get_entry(entry_id):
    conn = get_db_connection()
    entry = conn.execute('SELECT * FROM entries WHERE id = ?', (entry_id,)).fetchone()
    conn.close()
    if entry:
        entry = dict(entry)
        entry['deductions'] = json.loads(entry['deductions'])
        return entry
    return None

def update_entry(entry_id, date, income, deductions, in_hand):
    conn = get_db_connection()
    with conn:
        conn.execute('''
            UPDATE entries 
            SET date = ?, income = ?, deductions = ?, in_hand = ?
            WHERE id = ?
        ''', (date, income, json.dumps(deductions), in_hand, entry_id))
    conn.close()
