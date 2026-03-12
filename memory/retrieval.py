import sqlite3


def find_similar_question(question: str):

    conn = sqlite3.connect("debates.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT question, best_agent, confidence, evaluation FROM debates WHERE question = ?",
        (question,)
    )

    result = cursor.fetchone()

    conn.close()

    return result