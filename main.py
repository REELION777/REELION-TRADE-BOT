from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = '7914641054:AAFKxsihjUxiLf9m3smWyP06JnyNoLKSmgs'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('💸 Купить BTC'), KeyboardButton('💵 Продать BTC'))
    await msg.answer(
        'Добро пожаловать в *REELION TRADE* 💰\n\nВыберите, что хотите сделать:',
        reply_markup=kb,
        parse_mode="Markdown"
    )

# Обработка кнопок
@dp.message_handler(lambda message: message.text == '💸 Купить BTC')
async def buy_btc(msg: types.Message):
    await msg.answer('Введите сумму в рублях, на которую хотите купить BTC:')

@dp.message_handler(lambda message: message.text == '💵 Продать BTC')
async def sell_btc(msg: types.Message):
    await msg.answer('Введите сумму BTC, которую хотите продать:')

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
if name == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
