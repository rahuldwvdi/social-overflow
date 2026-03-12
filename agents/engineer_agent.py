from engine.answer_engine import generate_response

PROMPT = """
You are a senior software engineer.

Answer the question in a concise way.

Rules:
- Respond with only the answer.
- Do NOT repeat the question.
- Do NOT explain instructions.
- Maximum 3 sentences.
"""


def engineer_agent(question: str):

    prompt = f"{PROMPT}\nQuestion: {question}\nAnswer:"

    return generate_response(prompt)