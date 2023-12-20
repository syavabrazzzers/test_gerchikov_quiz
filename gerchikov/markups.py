from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_quiz_markup(data: dict, selected=None):
    if selected is None:
        selected = []

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{key} !" if key in selected else str(key), callback_data=str(key)
            )
        ]
        for key, value in data.items()
    ]

    if selected:
        buttons.append(
            [InlineKeyboardButton(text="Продолжить", callback_data="next_question")]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons)
