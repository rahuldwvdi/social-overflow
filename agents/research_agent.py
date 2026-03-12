from engine.answer_engine import generate_response


RESEARCH_PROMPT = """
You are an AI researcher working in machine learning.

Focus on:
- scientific evidence
- academic research
- current AI capabilities
- realistic limitations

Provide a balanced and research-based answer.
"""


def research_agent(question: str):

    prompt = RESEARCH_PROMPT + "\n\nQuestion: " + question

    answer = generate_response(prompt)

    return answer