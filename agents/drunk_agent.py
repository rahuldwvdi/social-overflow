from engine.answer_engine import generate_response

PROMPT = """
You are a slightly drunk man talking in a bar.

Answer the question humorously but loosely.

Rules:
- one short funny sentence but complete
"""


def drunk_agent(question: str):

    prompt = f"{PROMPT}\nQuestion: {question}\nAnswer:"

    return generate_response(prompt)