from telebot import types

from bot import bot


def render_yes_now_keyboard(user_id: int, question: str, prefix: str):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Да", callback_data=f"{prefix}_yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Нет", callback_data=f"{prefix}_no")
    keyboard.add(key_no)
    bot.send_message(user_id, text=question, reply_markup=keyboard)

def render_initial_keyboard(user_id: int):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    register_button = types.KeyboardButton("Регистрация")
    todo_button = types.KeyboardButton("TODO")
    plan_button = types.KeyboardButton("Планы сегодня")
    keyboard.add(register_button, todo_button, plan_button)
    bot.send_message(user_id, "Выберите действие", reply_markup=keyboard)


def remove_initial_keyboard(user_id: int, message: str):
    keyboard = types.ReplyKeyboardRemove()
    bot.send_message(user_id, message, reply_markup=keyboard)