from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from gerchikov.filters import CallbackTextFilter
from gerchikov.handlers import add_points, get_result, answer_result
from gerchikov.markups import get_quiz_markup
from gerchikov.states import GerchikovState
from gerchikov.texts import questions
from main.bot import bot

router = Router()


@router.message(Command("gerchikov_test"))
async def start_gerchikov_test(message: Message, state: FSMContext):
    await message.answer("Введите ФИО")
    await state.set_state(GerchikovState.name)


@router.message(StateFilter(GerchikovState.name))
async def set_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите должность")
    await state.set_state(GerchikovState.position)


@router.message(StateFilter(GerchikovState.position))
async def set_position(message: Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer("Теперь ответьте на вопросы")
    await state.set_state(GerchikovState.user_naber)
    first_question_key = questions[0]
    await state.update_data(
        max_choices=first_question_key.choices_count, question=0, answers=[]
    )
    await message.answer(
        first_question_key.text,
        reply_markup=get_quiz_markup(first_question_key.questions),
    )


@router.callback_query(
    StateFilter(GerchikovState.user_naber), CallbackTextFilter("next_question")
)
async def next_question_callback(callback: CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    current_question = state_data["question"]

    if (current_question + 1) == len(questions):
        await answer_result(callback, state_data)
        return

    next_question = questions[current_question + 1]

    add_points(state_data, current_question)

    state_data["question"] = current_question + 1
    state_data["max_choices"] = next_question.choices_count
    state_data["answers"] = []

    await state.set_data(state_data)
    await bot.delete_message(
        message_id=callback.message.message_id, chat_id=callback.message.chat.id
    )
    await bot.send_message(
        callback.message.chat.id,
        next_question.text,
        reply_markup=get_quiz_markup(next_question.questions),
    )


@router.callback_query(StateFilter(GerchikovState.user_naber))
async def question_answer(callback: CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    state_answers = state_data["answers"]
    current_question = state_data["question"]

    if int(callback.data) in state_answers:
        await bot.delete_message(
            message_id=callback.message.message_id, chat_id=callback.message.chat.id
        )
        state_answers.remove(int(callback.data))
        await state.update_data(answers=state_answers)
        await bot.send_message(
            callback.message.chat.id,
            questions[current_question].text,
            reply_markup=get_quiz_markup(
                questions[current_question].questions, state_answers
            ),
        )
        return

    state_answers.append(int(callback.data))

    if len(state_answers) == state_data["max_choices"]:
        add_points(state_data, current_question)
        current_question += 1
        state_data["question"] = current_question
        await bot.delete_message(
            message_id=callback.message.message_id, chat_id=callback.message.chat.id
        )

        if current_question == len(questions):
            await answer_result(callback, state_data)
            return

        next_question = questions[current_question]
        state_data["max_choices"] = next_question.choices_count
        state_data["answers"] = []
        await state.set_data(state_data)
        await bot.send_message(
            callback.message.chat.id,
            next_question.text,
            reply_markup=get_quiz_markup(next_question.questions),
        )
        return

    await state.set_data(state_data)
    await bot.delete_message(
        message_id=callback.message.message_id, chat_id=callback.message.chat.id
    )
    await bot.send_message(
        callback.message.chat.id,
        questions[current_question].text,
        reply_markup=get_quiz_markup(
            questions[current_question].questions, state_data["answers"]
        ),
    )
