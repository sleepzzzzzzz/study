import telebot
from telebot import types
import csv
import os
from datetime import datetime

API_TOKEN = ""

bot = telebot.TeleBot(API_TOKEN)

users = {}


def is_valid_name_surname_action(name_surname_action):
    return not (" " in name_surname_action or len(name_surname_action) < 2)


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
        now=datetime.strptime("24.08.2021", "%d.%m.%Y")
        wnow=now.strftime( "%d.%m.%Y")
        myDict={}
        csv_dir = os.path.join("test_files", "csv")
        file_path = os.path.join(csv_dir, "employ.csv")

        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                myDict=row
        
        if wnow== myDict["date"]:
            bot.send_message(user_id,(myDict["action"]))
        else:
            bot.send_message(user_id, "На сегодня планов нет!")
            users.pop(user_id, None)
            render_initial_keyboard(user_id)
            
            
        
        
        
    

    elif call.data == "plan_no":
        # remove user
        users.pop(user_id, None)
        render_initial_keyboard(user_id)
    
    
def get_action(message):
    user_id = message.from_user.id
    action=message.text
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
       date = datetime.strptime(message .text, "%d.%m.%Y")
       formdate=date.strftime("%d.%m.%Y")
    except ( ValueError) :
       bot.send_message(user_id, "Введите корректную дату")
       bot.register_next_step_handler(message, get_date)
    
    if date>today:
        action=users[user_id]["action"] 
        users[user_id]["date"]=formdate
            
        question = f"Ты бы хотел запланировать это действие {action} на эту дату {formdate}?"
        render_yes_now_keyboard(user_id, question, "regg")
   
        
    
    else :
        bot.send_message(user_id, "Введите корректную дату")
        bot.register_next_step_handler(message, get_date)
         
   
   
            
            
   
   


def get_name(message):
    user_id = message.from_user.id
    name = message.text.title()
    if is_valid_name_surname_action(name):
        users[user_id]["name"] = name.title()
        bot.send_message(user_id, "Какая у тебя фамилия?")
        bot.register_next_step_handler(message, get_surname)
        
    else:
        bot.send_message(user_id, "Введите корректное имя")
        bot.register_next_step_handler(message, get_name)


def get_surname(message):
    surname = message.text
    user_id = message.from_user.id
    if is_valid_name_surname_action(surname):
        users[user_id]["surname"] = surname.title()
        bot.send_message(user_id, "Сколько тебе лет?")
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(user_id, "Введите корректную фамилию")
        bot.register_next_step_handler(message, get_surname)


def get_age(message):
    age_text = message.text
    user_id = message.from_user.id
    if age_text.isdigit():
        age = int(age_text)
        if not 10 <= age <= 100:
            bot.send_message(user_id, "Введите реальный возраст, пожалуйста")
            bot.register_next_step_handler(message, get_age)
        else:
            users[user_id]["age"] = int(age)
            name = users[user_id]["name"]
            surname = users[user_id]["surname"]
            question = f"Тебе {age} лет и тебя зовут {name} {surname}?"
            render_yes_now_keyboard(user_id, question, "reg")
    else:
        bot.send_message(user_id, "Введите цифрами, пожалуйста")
        bot.register_next_step_handler(message, get_age)


@bot.callback_query_handler(func=lambda call: call.data.startswith("reg_"))
def callback_worker(call):
    user_id = call.from_user.id
    if call.data == "reg_yes":
        bot.send_message(user_id, "Спасибо, я запомню!")
        # pretend that we save in database
        csv_dir = os.path.join("test_files", "csv")
        file_path = os.path.join(csv_dir, "employeess12231.csv")

        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

        with open(file_path, "a") as csv_file:
            names = ["id", "name", "surname","age"]
            writer = csv.DictWriter(csv_file, fieldnames=names)
            # записываем заголовок
            writer.writeheader()
            writer.writerow({"id": user_id, "name": users[user_id]["name"], "surname": users[user_id]["surname"], "age": users[user_id]["age"] })
       
    

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
        file_path = os.path.join(csv_dir, "employ.csv")

        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)
        with open(file_path, "a") as csv_file:
            names1=["id","action","date"]
            writer1 = csv.DictWriter(csv_file, fieldnames=names1)
            writer1.writeheader()
            writer1.writerow({"id": user_id,"action": users[user_id]["action"],"date": users[user_id]["date"] })
    

        with open(file_path) as f:
           print(f.read())
    elif call.data == "regg_no":
        # remove user
        users.pop(user_id, None)
        render_initial_keyboard(user_id)


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


if __name__ == "__main__":
    bot.polling(none_stop=True)


