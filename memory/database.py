import sqlite3

DB_NAME = "debates.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS debates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        best_agent TEXT,
        confidence REAL,
        evaluation TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def save_debate(question, best_agent, confidence, evaluation):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO debates (question, best_agent, confidence, evaluation)
    VALUES (?, ?, ?, ?)
    """, (question, best_agent, confidence, evaluation))

    conn.commit()
    conn.close()