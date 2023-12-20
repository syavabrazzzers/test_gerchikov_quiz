from aiogram.filters import Filter
from aiogram.types import CallbackQuery


class CallbackTextFilter(Filter):
    def __init__(self, text: str):
        self.text = text

    async def __call__(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, CallbackQuery):
                return arg.data in self.text
