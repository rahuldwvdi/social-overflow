from groq import Groq

client = Groq(
    api_key="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"
)

MODEL = "llama-3.1-8b-instant"


def generate_response(prompt: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=40,
        temperature=0.3
    )

    text = response.choices[0].message.content

    text = text.split("\n")[0]

    return text.strip()