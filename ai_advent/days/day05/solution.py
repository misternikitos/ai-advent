import time

from openai import OpenAI

from ai_advent.config import settings

PRICE_IN = 0.028
PRICE_OUT = 0.42

client = OpenAI(
    api_key=settings.deepseek.api_key,
    base_url=str(settings.deepseek.base_url),
)

prompt = """
На столе два стакана: один с вином, другой — с водой.
Из стакана с вином взяли одну ложку вина и добавили в стакан с водой.
Содержимое последнего тщательно перемешали.
После этого набрали одну ложку из этого стакана и перелили обратно в стакан с вином.

Чего в результате больше: вина в стакане с водой или воды в стакане с вином?
"""


models = [
    ("Weak Model", "deepseek-chat"),
    ("Strong Model", "deepseek-reasoner"),
]

print(f"Промпт:\n{prompt}\n")

for label, model_name in models:
    print(f"--- {label}: {model_name} ---\n")

    start_time = time.time()

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt},
        ],
        stream=False,
    )
    end_time = time.time()
    duration = end_time - start_time

    content = response.choices[0].message.content
    usage = response.usage

    print(f"Время выполнения: {duration:.2f} сек")
    if usage:
        print(
            f"Токены: {usage.total_tokens} (prompt: {usage.prompt_tokens}, "
            f"completion: {usage.completion_tokens})",
        )

        # Примерная стоимость (замените цены на актуальные для используемых моделей)
        cost = (
            usage.prompt_tokens * PRICE_IN + usage.completion_tokens * PRICE_OUT
        ) / 1000000
        print(f"Стоимость: ${cost:.6f}")

    print(f"\nОтвет:\n{content}\n")

# Вывод в консоль при запуске решения доступен в ai_advent/days/day05/console_output.md
#
# --- Анализ и выводы ---

# Сравнение моделей (заполните после запуска с реальными моделями):
#
# 1. Время ответа (Speed):
#    - Слабая модель: примерно 15 секунд
#    - Сильная модель: примерно 30 секунд
#
# 2. Качество ответов (Quality):
#    - Слабая модель: начала рассуждать в ответе, но, в целом, справилась.
#    - Сильная модель: сразу дала точный ответ, не стала сильно расписывать.
#      Вероятно, это из-за внутренних размышлений.
#
# 3. Ресурсоёмкость (Tokens/Cost):
#    - Слабая модель: имеет хорошее соотношение цены/качества
#    - Сильная модель: требует намного больше ресурсов, чем слабая
#
# Вывод:
#    - Для простых задач лучше использовать deepseek-chat
#    - Для сложных задач, требующих креативности или глубокого анализа,
#      лучше deepseek-reasoner. Однако время ответа сильно увеличивается.
