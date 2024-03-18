import psycopg2 as ps


class DB:
    db = ps.connect(dbname="Study_department",
                    user="postgres",
                    password="kali",
                    host="localhost",
                    port="5433")

    # Метод вывода данных
    @classmethod
    def view_data(cls, table, request):
        try:
            cursor = cls.db.cursor()
            # Проверка существования таблицы
            cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_name = '{table}';")
            if cursor.fetchone():
                cursor.execute(request)
                res = cursor.fetchall()
                if res != None:
                    return res
            else:
                print("Таблица не найдена.")
            cursor.close()

        except ps.Error as e:
            print("Ошибка при работе с базой данных:", e)

    @classmethod
    def add_edit_data(cls, table, request):
        try:
            cursor = cls.db.cursor()
            # Проверка существования таблицы
            cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_name = '{table}';")
            if cursor.fetchone():
                cursor.execute(request)
                cls.db.commit()
                cursor.close()
            else:
                print("Таблица не найдена.")
            cursor.close()

        except ps.Error as e:
            print("Ошибка при работе с базой данных:", e)

