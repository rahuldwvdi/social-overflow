from engine.answer_engine import generate_response

PROMPT = """
You are a cybersecurity expert.

Focus on risk.

Rules:
- one sentence
- max 15 words
- add one emoji

Answer:
"""


def security_agent(question: str):

    prompt = PROMPT + "\nQuestion: " + question

    return generate_response(prompt)