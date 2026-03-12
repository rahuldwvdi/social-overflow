from engine.answer_engine import generate_response


def generate_critique(agent, question, arguments):

    prompt = f"""
You are {agent} participating in a debate.

Question:
{question}

Other arguments:
{arguments}

Give a short critique.
"""

    return generate_response(prompt)