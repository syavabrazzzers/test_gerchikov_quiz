from aiogram.fsm.state import State, StatesGroup


class GerchikovState(StatesGroup):
    name = State()
    position = State()
    user_naber = State()
