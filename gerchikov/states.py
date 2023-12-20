from aiogram.fsm.state import StatesGroup, State


class GerchikovState(StatesGroup):
    name = State()
    position = State()
    user_naber = State()
