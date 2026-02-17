from openai import OpenAI

from ai_advent.config import settings

client = OpenAI(
    api_key=settings.deepseek.api_key,
    base_url=str(settings.deepseek.base_url),
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "Ты проходишь AI Advent, "
            "где каждый день выполняется задание на работу с AI.",
        },
        {
            "role": "user",
            "content": "Придумай задание для первого дня. Расскажи, как его выполнить.",
        },
    ],
    stream=False,
)

print(response.choices[0].message.content)
