from engine.answer_engine import generate_response

PROMPT = """
You are a startup founder.

Focus on disruption and innovation.

Maximum 3 sentences.
"""


def startup_agent(question: str):

    prompt = PROMPT + "\nQuestion: " + question

    return generate_response(prompt)