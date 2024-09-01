from aiogram import Router, F
from aiogram.enums import ParseMode, ChatAction
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.utils import markdown

import app.keyboards as kb
from app.utils import path_detector

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"""Добро пожаловать, {markdown.bold(message.from_user.first_name)}!
    
Используй кнопки ниже👇 для использования бота.
    """, reply_markup=kb.main, parse_mode=ParseMode.MARKDOWN)


@router.message(F.text == '📔 Контакты')
async def get_contacts(message: Message):
    await message.answer('Мои контакты 📔', reply_markup=await kb.inline_contact())


@router.message(F.text == '✍️ Записаться на диагностику')
async def get_form_access(message: Message):
    await message.reply(text='Запишитесь через форму! ✍️', reply_markup=await kb.link_to_form())


@router.message(F.text == '💌 Бесплатные материалы')
async def get_free_materials(message: Message):
    await message.answer(f"""Какие материалы ты хочешь получить?
        """, reply_markup=await kb.free_material())


@router.callback_query(F.data == 'shpargalka_free_material')
async def get_free_material(callback_query: CallbackQuery):
    await callback_query.bot.send_chat_action(
        chat_id=callback_query.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )

    await callback_query.bot.send_document(
        chat_id=callback_query.message.chat.id,
        document=FSInputFile(path_detector("../file/pdf/Шпаргалка 2 номер ЕГЭ.pdf")),
        caption='Держи! Это твои бесплатные материалы!'
    )
    await callback_query.answer()


@router.callback_query(F.data == 'vuzi_free_material')
async def get_free_material(callback_query: CallbackQuery):
    await callback_query.bot.send_chat_action(
        chat_id=callback_query.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )

    await callback_query.bot.send_document(
        chat_id=callback_query.message.chat.id,
        document=FSInputFile(path_detector("../file/pdf/Вузы.pdf")),
        caption='Держи! Это твои бесплатные материалы! Не забудь подписаться на канал! '
    )
    await callback_query.answer()
