from engine.answer_engine import generate_response

PROMPT = """
You are an AI researcher.

Focus on research evidence.

Maximum 3 sentences.
"""


def research_agent(question: str):

    prompt = PROMPT + "\nQuestion: " + question

    return generate_response(prompt)