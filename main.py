import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Стартовая команда
@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("💵 Купить BTC"), KeyboardButton("💱 Продать BTC"))
    await msg.answer("Добро пожаловать в *REELION TRADE* 🔥\n\nВыберите, что хотите сделать:", reply_markup=kb, parse_mode="Markdown")

# Обработка кнопки "Купить BTC"
@dp.message_handler(lambda message: message.text == "💵 Купить BTC")
async def buy_btc(msg: types.Message):
    await msg.answer("Введите сумму в рублях, на которую хотите купить BTC:")

# Обработка кнопки "Продать BTC"
@dp.message_handler(lambda message: message.text == "💱 Продать BTC")
async def sell_btc(msg: types.Message):
    await msg.answer("Введите сумму в рублях, которую хотите продать:")

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
