from engine.answer_engine import generate_response


def generate_critique(agent_name: str, question: str, other_answers: str):

    prompt = f"""
You are {agent_name} participating in an expert debate.

Question:
{question}

Other agents' arguments:
{other_answers}

Your task:
Critique the weaknesses or assumptions in these arguments.

Rules:
- Be concise
- Maximum 2 sentences
- Focus on logical flaws or missing considerations
"""

    critique = generate_response(prompt)

    return critique