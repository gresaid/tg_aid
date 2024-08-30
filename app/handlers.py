from aiogram import Router, F, html
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"""Добро пожаловать, {message.from_user.first_name}!
Используй кнопки ниже👇 для использования бота.
    """, reply_markup=kb.main)


@router.message(F.text == '📔 Контакты')
async def get_contacts(message: Message):
    await message.answer('Мои контакты 📔', reply_markup=await kb.inline_contact())


@router.message(F.text == '✍️ Записаться на занятие')
async def get_link_access(message: Message):
    await message.reply(text='Запишитесь через форму! ✍️', reply_markup=await kb.link_to_form())
