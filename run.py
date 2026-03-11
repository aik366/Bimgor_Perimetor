from app.utils import open_month, open_order
import shutil
from config import PATH_FILE
from datetime import datetime

now = datetime.now()

def main():
    shutil.copyfile(f"{PATH_FILE}\\Заказы{now:%y}.RSB", "DATA\\22.txt")
    while True:
        my_input = input('Для выборо месяца введите 1:\nДля выбора заказа введите 2:\nДля выхода введите 0: ')
        if my_input == '1':
            input_month = input("Введите месяц (в формате 1, 2, ..., 12): ")
            open_month("22.txt", input_month)
        elif my_input == '2':
            input_order = input("Введите номер заказа: ")
            open_order("22.txt", input_order)
        elif my_input == '0':
            print("Выход из программы")
            exit()
        else:
            print("Неверный ввод")

main()