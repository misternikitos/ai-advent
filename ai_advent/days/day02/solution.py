from openai import OpenAI

from ai_advent.config import settings

client = OpenAI(
    api_key=settings.deepseek.api_key,
    base_url=str(settings.deepseek.base_url),
)

prompt = "Explain the concept of 'recursion' in programming."
print(f"Using one user prompt: {prompt}")

# 1. Unconstrained Request
print("--- Unconstrained Request ---")
response_unconstrained = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    stream=False,
)
print(response_unconstrained.choices[0].message.content)

# 2. Constrained Request
# - Explicit format description: "Provide a definition in a single sentence."
# - Length limitation: max_tokens=50
# - Stop condition: stop=["."]
print("\n--- Constrained Request ---")
response_constrained = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. "
                "Provide a definition in a single sentence."
            ),
        },
        {"role": "user", "content": prompt},
    ],
    max_tokens=50,
    stop=["."],
    stream=False,
)
print(
    f"{response_constrained.choices[0].message.content}.",
)  # Add the period back for display
