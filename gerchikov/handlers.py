from aiogram.types import CallbackQuery

from gerchikov.texts import questions
from main.bot import bot

from loguru import logger

results = {
    "pa": "Патриотический тип",
    "pr": "Профессиональный тип",
    "in": "Инструментальный тип",
    "ho": "Хозяйский тип",
    "lu": "Люмпенизированный тип",
}


def get_result(data: dict):
    results_dict = {}
    for key in results.keys():
        results_dict |= {key: data[key]}

    max_key = max(results_dict, key=results_dict.get)
    return results[max_key]


def add_points(data, question):
    state_answers = data["answers"]

    for item in state_answers:
        answer = questions[question].questions[item]

        if isinstance(answer, list):
            for ans in answer:
                if ans.value != "":
                    count = data.get(ans.value, 0) + 1
                    data[ans.value] = count

            continue

        if answer.value != "":
            count = data.get(answer.value, 0) + 1
            data[answer.value] = count


async def answer_result(callback: CallbackQuery, data: dict):
    text = f"""{data['name']}, ваш тип - {get_result(data)}"""
    await bot.send_message(
        callback.message.chat.id,
        text=text,
    )
    data.pop('max_choices')
    data.pop('question')
    data.pop('answers')
    logger.info(data)
