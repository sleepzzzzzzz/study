from datetime import datetime

from bl.constants import DATE_FORMAT
from bl.users_dict import users

from bl.valid import is_valid_name_surname_action
from bl.yes_no import render_yes_now_keyboard
from bot import bot



def get_action(message):
    user_id = message.from_user.id
    action = message.text
    if is_valid_name_surname_action(action):
        users[user_id]["action"] = action.title()
        bot.send_message(user_id, "на какую дату планируем?")
        bot.register_next_step_handler(message, get_date)

    else:
        bot.send_message(user_id, "Введите корректное действие")
        bot.register_next_step_handler(message, get_action)


def get_date(message):
    user_id = message.from_user.id

    today = datetime.now()

    try:
        date = datetime.strptime(message.text, DATE_FORMAT)

        ftoday = today.strftime(DATE_FORMAT)
        formtoday = datetime.strptime(ftoday, DATE_FORMAT)

    except(ValueError, TypeError):
        bot.send_message(user_id, "Введите корректную дату")
        bot.register_next_step_handler(message, get_date)

    if date >= formtoday:
        fdate = date.strftime("%d.%m.%Y")
        action = users[user_id]["action"]
        users[user_id]["date"] = fdate

        question = f"Ты бы хотел запланировать это действие {action} на эту дату {fdate}?"
        render_yes_now_keyboard(user_id, question, "regg")

    else:
        bot.send_message(user_id, "Введите корректную дату")
        bot.register_next_step_handler(message, get_date)