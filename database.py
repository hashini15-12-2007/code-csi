
import sqlite3
import os

DB_NAME = "codecsi.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reports 
                 (id INTEGER PRIMARY KEY, filename TEXT, evidence TEXT, analysis TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_report(filename, evidence, analysis):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO reports (filename, evidence, analysis) VALUES (?, ?, ?)", (filename, evidence, analysis))
    conn.commit()
    conn.close()
