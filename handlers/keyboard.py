from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


c1 = KeyboardButton(text='Веб Браузеры')
c2 = KeyboardButton(text='Безопасность')
c3 = KeyboardButton(text='Мессенджеры')
c4 = KeyboardButton(text='Облачные хранилища')
c5 = KeyboardButton(text='Медиа')
c6 = KeyboardButton(text='Графический софт')
c7 = KeyboardButton(text='Утилиты')
c8 = KeyboardButton(text='Документы')
c9 = KeyboardButton(text='Другое')
c10 = KeyboardButton(text='Скачать пакет приложений')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.insert(c1).insert(c2).insert(c3).insert(c4).insert(c5).insert(c6).insert(c7).insert(c8).insert(c9).add(c10)

kb_webbrowsers = InlineKeyboardMarkup()
item1 = InlineKeyboardButton("Google Chrome", callback_data='googlechrome')
item2 = InlineKeyboardButton("Chromium", callback_data='chromium')
item3 = InlineKeyboardButton("Opera", callback_data='opera')
item4 = InlineKeyboardButton("Mozilla Firefox", callback_data='mozillafirefox')
kb_webbrowsers.add(item1, item2, item3, item4)
