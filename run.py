from app.utils import open_month, open_order, input_color, print_color
import shutil
from config import PATH_FILE
from datetime import datetime
from colorama import init, Fore, Style

now = datetime.now()


def main():
    shutil.copyfile(f"{PATH_FILE}\\Заказы{now:%y}.RSB", "DATA\\22.txt")
    while True:
        my_input = input_color('Для выборо месяца введите 1:\nДля выбора заказа введите 2:\nДля выхода введите 0: ',
                               Fore.CYAN)
        if my_input == '1':
            input_month = input_color("Введите месяц (в формате 1, 2, ..., 12): ", Fore.CYAN)
            open_month("22.txt", input_month)
        elif my_input == '2':
            input_order = input_color("Введите номер заказа: ", Fore.CYAN)
            open_order("22.txt", input_order)
        elif my_input == '0':
            print_color("Выход из программы", Fore.CYAN)
            exit()
        else:
            print_color("Неверный ввод", Fore.CYAN)


main()
