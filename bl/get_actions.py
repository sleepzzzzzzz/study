import csv
import os
import sqlite3
from datetime import datetime

from bl.constants import DATE_FORMAT



def get_today_actions(user_id):
    now = datetime.now()
    wnow = now.strftime(DATE_FORMAT)
    user_actions = []
    csv_dir = os.path.join("test_files", "csv")
    file_path = os.path.join(csv_dir, "employ6.csv")


    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if not row["id"] == str(user_id):
                continue
            actdate = row["date"]

            if wnow == actdate:
                user_actions.append(row["action"])

    if not user_actions:

        message = "На сегодня планов нет!"

    else:
        enumerated_actions = []
        for index, action in enumerate(user_actions, start=1):
            enumerated_actions.append(f'{index}. {action};')
        greeting = "Привет,твои задачи на сегодня: \n"
        actions = "\n".join(enumerated_actions)
        message = f'{greeting}{actions}'
    return message
