from engine.answer_engine import generate_response

PROMPT = """
You are a cybersecurity expert.

Focus on risks and vulnerabilities.

Maximum 3 sentences.
"""


def security_agent(question: str):

    prompt = PROMPT + "\nQuestion: " + question

    return generate_response(prompt)