from app.utils import open_month, open_order
2
# open_month("22.txt", "03")

def main():
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