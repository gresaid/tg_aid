from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='💌 Бесплатные материалы')],
    [KeyboardButton(text='✍️ Записаться на диагностику', )],
    [KeyboardButton(text='📔 Контакты')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')


async def inline_contact():
    social_media = [['✅ Telegram ', 'https://t.me/gres_aid'],
                    ['✅ Youtube', 'https://www.youtube.com/@InfoCodexxx'],
                    ['✅ Дополнительные материалы на Boosty', 'https://boosty.to/gresaid']]
    keyboard = InlineKeyboardBuilder()
    for sc in social_media:
        keyboard.add(InlineKeyboardButton(text=sc[0], url=sc[1]))
    return keyboard.adjust(1).as_markup()


async def free_material():
    free_materials = [['В какие вузы поступить? ⁉️ ', ],
                      ['2 задание 😲']]

    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text=free_materials[0][0], callback_data='vuzi_free_material'))
    keyboard.add(InlineKeyboardButton(text=free_materials[1][0], callback_data='shpargalka_free_material'))
    return keyboard.adjust(1).as_markup()


async def link_to_form():
    keyboard = InlineKeyboardButton(text='Записаться! ✅', url='https://forms.gle/DgbZdwWsxL9u4ZeNA')
    return InlineKeyboardMarkup(inline_keyboard=[[keyboard]])
