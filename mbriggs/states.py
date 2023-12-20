from aiogram.fsm.state import State, StatesGroup


class MBriggsState(StatesGroup):
    name = State()
    email = State()
    mob_tel = State()
    user_naber = State()
    add_key_start = State()
    add_key = State()
    get_key = State()
    rm_key = State()
