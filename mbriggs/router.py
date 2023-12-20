import re

from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from loguru import logger

import mbriggs.markups as btn
from main.db import db
from main.bot import bot
from mbriggs.helpers import result
from mbriggs.states import MBriggsState

router = Router()


####################################ОТМЕНА########################################
@router.message(Command('cancel'), StateFilter('*'))
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Выход.\n")
    await state.clear()


####################################СТАРТ########################################
@router.message(Command('start'))
async def admin(message: types.Message, state: FSMContext):
    await message.answer(btn.start, parse_mode='html')


####################################АВТОРИЗАЦИЯ########################################
@router.message(Command('mbriggs_test'))
async def admin(message: types.Message, state: FSMContext):
    await message.answer(btn.text1, parse_mode='html')
    await message.answer(btn.name)
    await state.set_state(MBriggsState.name)


@router.message(StateFilter(MBriggsState.name))
async def name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(btn.email)
    await state.set_state(MBriggsState.email)


@router.message(StateFilter(MBriggsState.email))
async def email(message: types.Message, state: FSMContext):
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    if not re.findall(pattern, message.text):
        await message.answer("Неверный емэйл, попробуйте снова")
        return
    await state.update_data(email=message.text)
    await message.answer(btn.mob_tel)
    await state.set_state(MBriggsState.mob_tel)
    await state.update_data(state=1)


@router.message(StateFilter(MBriggsState.mob_tel))
async def mob_tel(message: types.Message, state: FSMContext):
    try:
        if len(message.text) == 11 and int(message.text):
            await state.update_data(mob_tel=message.text)
            await message.answer(btn.ready)
            await message.answer(btn.user_naber_1, reply_markup=btn.choice)
            await state.set_state(MBriggsState.user_naber)
            return
    except:
        pass
    await message.answer("Неверный номер, попробуйте снова")
    return


####################################КНОПКИ ОПРОСА########################################
@router.callback_query(StateFilter(MBriggsState.user_naber))
async def user_naber(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    data = await state.get_data()
    state_user = data["state"]
    if callback.data == "⏭":
        state_user += 1
        if len(data) - state_user == 2:
            # txt='Вы ответили не на все вопросы! Для коректного теста необходимо ответить на все'
            # await bot.send_message(callback.from_user.id, txt)
            state_user -= 1

    elif callback.data == "⏮":
        if state_user != 1:
            state_user -= 1
    else:
        dic = {f"user_naber_{state_user}": callback.data}
        await state.update_data(dic)
        state_user += 1
        if state_user == 70:
            data = await state.get_data()
            await result(data, callback)
            await state.clear()
            return

    await state.update_data(state=state_user)
    txt = btn.__dict__[f"user_naber_{state_user}"]
    try:
        already_answer = data[f"user_naber_{state_user}"]
        txt += f'''
<i>Ваш ответ:{already_answer}
</i>
'''
    except:
        pass
    await bot.send_message(callback.from_user.id, txt, reply_markup=btn.choice, parse_mode='html')

    data = await state.get_data()
    logger.info(data)


####################################КЛЮЧИ########################################
@router.message(Command('listink13'), StateFilter("*"))
async def list_key(message: types.Message):
    res = db.list_key(message.from_user.id)
    if not res:
        await bot.send_message(message.from_user.id, btn.list_key_error)
        return
    keys = ''
    for rows in res:
        keys += '`' + rows[0] + '`' + '\n'
    await bot.send_message(message.from_user.id, keys, parse_mode='markdown')


@router.message(Command('add'))
async def add_key(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Укажите название закладки, которую хотите добавить!")
    await state.set_state(MBriggsState.add_key_start)


@router.message(StateFilter(MBriggsState.add_key_start))
async def add_key(message: types.Message, state: FSMContext):
    key = message.text
    if db.isMessageExists(key):
        await bot.send_message(message.from_user.id, "Такое название уже занято. Попробуйте другой!")
        return
    await bot.send_message(message.from_user.id, btn.add_key(key), parse_mode='markdown')
    await state.update_data(key=key)
    await state.set_state(MBriggsState.add_key)


@router.message(StateFilter(MBriggsState.add_key))
async def add_key2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if not db.add_key(message.from_user.id, data["key"], message.message_id):
        await bot.send_message(message.from_user.id, btn.add_key_error)
        return
    await bot.send_message(message.from_user.id, btn.add_key_successful)
    await state.clear()


@router.message(Command('get'))
async def get_key(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Укажите название закладки, которую хотите получить!")
    await state.set_state(MBriggsState.get_key)


@router.message(StateFilter(MBriggsState.get_key))
async def get_key2(message: types.Message, state: FSMContext):
    key = message.text
    res = db.get_key(message.from_user.id, key)
    if not res:
        await bot.send_message(message.from_user.id, btn.get_key_error)
        return
    try:
        await bot.copy_message(message.chat.id, message.from_user.id, res)
    except Exception as ex:
        logger.error(ex)
        await bot.send_message(message.from_user.id, btn.get_key_error2)
    await state.clear()


@router.message(Command('rm'))
async def get_key(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Укажите название закладки, которую хотите удалить!")
    await state.set_state(MBriggsState.rm_key)


@router.message(StateFilter(MBriggsState.rm_key))
async def get_key2(message: types.Message, state: FSMContext):
    key = message.text
    res = db.remove_key(message.from_user.id, key)
    if not res:
        await bot.send_message(message.from_user.id, btn.remove_key_error)
        return
    await bot.send_message(message.from_user.id, btn.remove_key(key), parse_mode='markdown')
    await state.clear()
