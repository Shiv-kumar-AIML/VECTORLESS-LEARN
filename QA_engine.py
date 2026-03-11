import ollama

def generate_answer(query, context):

    prompt = f"""
You are a medical research assistant.

Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}

Answer clearly and briefly.
"""

    response = ollama.chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]