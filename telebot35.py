import os
import csv

from bl.add_actions import get_action
from bl.get_actions import get_today_actions
from bl.registration import get_name
from bl.users_dict import users
from bl.yes_no import render_yes_now_keyboard, render_initial_keyboard, remove_initial_keyboard

from bot import bot


@bot.message_handler(content_types=["text"])
def start(message):
    user_id = message.from_user.id
    if message.text == "Регистрация":
        # create empty user
        users[user_id] = {}
        remove_initial_keyboard(user_id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == "TODO":
        users[user_id] = {}
        remove_initial_keyboard(user_id, "Чтобы бы  ты хотел запланировать ?)")
        bot.register_next_step_handler(message, get_action)
    elif message.text == "Планы сегодня":
        users[user_id] = {}
        question = f"{user_id}, хотите узнать что на сегодня запланировано ?"
        render_yes_now_keyboard(user_id, question, "plan")
    else:
        render_initial_keyboard(user_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("plan_"))
def callback_worker2(call):
    user_id = call.from_user.id
    if call.data == "plan_yes":
        actions = get_today_actions(user_id)
        bot.send_message(user_id, actions)
        render_initial_keyboard(user_id)

    elif call.data == "plan_no":
        # remove user
        users.pop(user_id, None)
        render_initial_keyboard(user_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("reg_"))
def callback_worker(call):
    user_id = call.from_user.id
    if call.data == "reg_yes":
        bot.send_message(user_id, "Спасибо, я запомню!")
        # pretend that we save in database
        csv_dir = os.path.join("test_files", "csv")
        file_path = os.path.join(csv_dir, "employ6.csv")
        first_id = not os.path.exists(csv_dir)
        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

        with open(file_path, "a") as csv_file:
            names = ["id", "name", "surname", "age"]
            writer = csv.DictWriter(csv_file, fieldnames=names)
            # записываем заголовок
            if first_id:
                writer.writeheader()
            writer.writerow({"id": user_id, "name": users[user_id]["name"], "surname": users[user_id]["surname"],
                             "age": users[user_id]["age"]})

        with open(file_path) as f:
            print(f.read())
    elif call.data == "reg_no":
        # remove user
        users.pop(user_id, None)
        render_initial_keyboard(user_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("regg_"))
def callback_worker1(call):
    user_id = call.from_user.id
    if call.data == "regg_yes":
        bot.send_message(user_id, "Спасибо, я запомню!")
        # pretend that we save in database
        csv_dir = os.path.join("test_files", "csv")
        file_path = os.path.join(csv_dir, "employ6.csv")
        first_id = not os.path.exists(csv_dir)
        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

        with open(file_path, "a") as csv_file:
            names1 = ["id", "action", "date"]
            writer1 = csv.DictWriter(csv_file, fieldnames=names1)
            if first_id:
                writer1.writeheader()
            writer1.writerow({"id": user_id, "action": users[user_id]["action"], "date": users[user_id]["date"]})

        with open(file_path) as f:
            print(f.read())
    elif call.data == "regg_no":
        users.pop(user_id, None)
        render_initial_keyboard(user_id)


if __name__ == "__main__":
    bot.polling(none_stop=True)
