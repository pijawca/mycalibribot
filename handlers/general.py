from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from misc import bot, dp
from handlers.keyboard import kb_client, kb_webbrowsers
from handlers import ids


link = "<a href='{}'>{}</a>"

async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text='Привет, {}'.format(message.from_user.full_name),
        reply_markup=kb_client)

async def webbrowsers(message: types.Message):
    await message.answer(
        text='Выберите приложение',
        reply_markup=kb_webbrowsers)

# @dp.callback_query_handler(lambda c: c.data == 'googlechrome')
# async def callbackWebBrowsers(callback_query: types.CallbackQuery,):
#     await bot.send_message(chat_id=callback_query.from_user.id, 
#                            text=f'Скачивание возможно только по альтернативной ссылке\n\n{link}'.format(ids.webbrowsers['googlechrome'], 'Google Drive'),
#                            parse_mode='HTML')

@dp.callback_query_handler(lambda c: c.data == 'googlechrome')
async def callbackWebBrowsers(callback_query: types.CallbackQuery,):
    await bot.send_message(chat_id = callback_query.from_user.id,
                           text=f'Скачать можно снизу, либо использовать альтернативную ссылку\n\n{link}'.format(ids.webbrowsers['googlechrome'], 'Google Drive'))
    with open('soft/google-chrome-117-0-5938-92.exe', 'rb') as document:
        await bot.send_document(chat_id=callback_query.from_user.id, document=document)

@dp.callback_query_handler(lambda c: c.data == 'chromium')
async def callbackWebBrowsers(callback_query: types.CallbackQuery,):
    await bot.send_message(chat_id = callback_query.from_user.id,
                           text=f'Файл больше 50 мб. Используйте только альтернативную ссылку\n\n{link}'.format(ids.webbrowsers['chromium'], 'Google Drive'))
    
@dp.callback_query_handler(lambda c: c.data == 'opera')
async def callbackWebBrowsers(callback_query: types.CallbackQuery,):
    await bot.send_message(chat_id = callback_query.from_user.id,
                           text=f'Скачать можно снизу, либо использовать альтернативную ссылку\n\n{link}'.format(ids.webbrowsers['opera'], 'Google Drive'))
    with open('soft/OperaSetup.exe', 'rb') as document:
        await bot.send_document(chat_id=callback_query.from_user.id, document=document)


    

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start, Text(equals=['/start']))
    dp.register_message_handler(webbrowsers, Text(equals=['/webbrowsers', 'Веб Браузеры']))