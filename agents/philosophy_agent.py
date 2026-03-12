from engine.answer_engine import generate_response

PROMPT = """
You are a philosopher of technology.

Focus on ethics and long term human impact.

Maximum 3 sentences.
"""


def philosophy_agent(question: str):

    prompt = PROMPT + "\nQuestion: " + question

    return generate_response(prompt)