import sqlite3

db_file = "todo.db"

try:
    sqlite_connection = sqlite3.connect(db_file)
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "SELECT sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
    raise

com = """
                                    CREATE TABLE IF NOT EXISTS "todo"(
                                        id INTEGER PRIMARY KEY,
                                        action VARCHAR(255)  NOT NULL,
                                        date DATETIME  NOT NULL,

                                    );
                                """

sqlite_connection.commit()