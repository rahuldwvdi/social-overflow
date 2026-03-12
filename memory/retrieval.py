import sqlite3


def find_similar_question(question):

    conn = sqlite3.connect("debates.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT question,best_agent,confidence,evaluation FROM debates WHERE question=?",
        (question,)
    )

    row = cur.fetchone()

    conn.close()

    return row