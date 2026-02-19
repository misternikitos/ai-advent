from openai import OpenAI

from ai_advent.config import settings

client = OpenAI(
    api_key=settings.deepseek.api_key,
    base_url=str(settings.deepseek.base_url),
)

problem_description = (
    "Крестьянину нужно перевезти через реку волка, козу и капусту. "
    "У него есть лодка, в которой может поместиться только он сам и еще один пассажир "
    "(волк, коза или капуста). "
    "Если оставить волка с козой без присмотра, волк съест козу. "
    "Если оставить козу с капустой, коза съест капусту. "
    "Как перевезти всех на другой берег в целости и сохранности?"
)

print(f"Задача:\n{problem_description}\n")

# 1. Прямой ответ
print("--- 1. Прямой ответ ---")
response_direct = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": problem_description},
    ],
    stream=False,
)
print(response_direct.choices[0].message.content)
print("\n")


# 2. Пошаговое решение
print("--- 2. Пошаговое решение ---")
response_step = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": f"{problem_description}\nРеши эту задачу пошагово.",
        },
    ],
    stream=False,
)
print(response_step.choices[0].message.content)
print("\n")


# 3. Мета-промптинг (Prompt Engineering)
print("--- 3. Мета-промптинг ---")
meta_instruction = (
    "Создай подробный и оптимальный промпт для решения следующей логической задачи. "
    "Промпт должен направлять ИИ на четкое рассуждение и нахождение правильного "
    "решения.\n\n"
    f"Задача: {problem_description}"
)

response_meta = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": meta_instruction},
    ],
    stream=False,
)
generated_prompt = str(response_meta.choices[0].message.content)
print(f"Сгенерированный промпт:\n{generated_prompt}\n")

print("Решаем с использованием сгенерированного промпта...")
response_using_meta = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": generated_prompt},
    ],
    stream=False,
)
print(response_using_meta.choices[0].message.content)
print("\n")


# 4. Группа экспертов
print("--- 4. Группа экспертов ---")
expert_instruction = (
    "Вы — группа из трех экспертов, решающих логическую задачу:\n"
    "1. Аналитик: Разберите ограничения задачи и начальное состояние.\n"
    "2. Инженер: Предложите последовательность действий для решения.\n"
    "3. Критик: Проверьте предложенное решение на предмет нарушения правил.\n\n"
    "Пожалуйста, предоставьте мнение каждого эксперта, а затем итоговое согласованное "
    " решение.\n\n"
    f"Задача: {problem_description}"
)

response_experts = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": expert_instruction},
        {"role": "user", "content": "Начните обсуждение."},
    ],
    stream=False,
)
print(response_experts.choices[0].message.content)
print("\n")

# Вывод в консоль при запуске решения доступен в ai_advent/days/day03/console_output.md
#
# Сравнение результатов:
#
# Точность: Все четыре метода дали верное решение. Это классическая задача,
# и модель (DeepSeek) хорошо справляется с ней во всех конфигурациях.
#
# Различия:
#  - Прямой метод дал повествовательное решение, смешивая рассуждения с шагами.
#  - Пошаговый метод был более структурированным, явно перечисляя «Рейс 1», «Рейс 2».
#  - Метод мета-промптинга дал объяснение «учебного» качества, так как
#    сгенерированный промпт явно требовал структуры и проверки.
#  - Метод группы экспертов обеспечил лучшую верификацию, так как «Критик» явно
#    проверял нарушения правил после предложения «Инженера».
