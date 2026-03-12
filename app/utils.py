from time import strftime
import datetime
import shutil
import os
from pathlib import Path

PATH = (Path(__file__).parent / "../DATA").resolve()

month_dict = {'01': 'Январь', '02': 'Февраль', '03': 'Март', '04': 'Апрель', '05': 'Май', '06': 'Июнь',
              '07': 'Июль', '08': 'Август', '09': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}


def open_month(file_name, month, mode="r"):
    with open(PATH / file_name, mode) as f:
        month_sum, month_sum_ser = 0.0, 0.0
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[2][3:5] == f"{month:0>2}" and st0[12] == '  .  ':
                zakaz_sum = 0.0
                for j in i[2:]:
                    str_sum = 0.0
                    poz, dlina, visota, kol, pusto, vid = j.split("|")[0:6]
                    if poz == "R" or vid[0] in ("R", "К") or int(dlina) < 50 or int(visota) < 50:
                        continue
                    str_sum = (int(dlina)*2+int(visota)*2)/1000*int(kol)
                    zakaz_sum += str_sum
                print(f"{st0[0]}: {zakaz_sum:.2f} м.п.")
                if st0[1].strip() == "Сердюченко":
                    month_sum_ser += zakaz_sum
                else:
                    month_sum += zakaz_sum
        print(f"Общий метраж Сердюченко, за {month_dict.get(f'{month:0>2}')} ({month:0>2}) : {month_sum_ser:.2f} м.п.")
        print(f"Общий метраж Мы, за {month_dict.get(f'{month:0>2}')} ({month:0>2}) : {month_sum:.2f} м.п.")
        print(f"Итого за {month_dict.get(f'{month:0>2}')} ({month:0>2}): {(month_sum + month_sum_ser):.2f} м.п.")

        
def open_order(file_name, order_number, mode="r"):
    with open(PATH / file_name, mode) as f:
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[0] == order_number and st0[12] == '  .  ':
                print(st0[0])
                order_sum = 0.0
                for j in i[2:]:
                    str_sum = 0.0
                    poz, dlina, visota, kol, pusto, vid = j.split("|")[0:6]
                    if poz == "R" or vid[0] in ("R", "К") or int(dlina) < 50 or int(visota) < 50:
                        continue
                    str_sum = (int(dlina)*2+int(visota)*2)/1000*int(kol)
                    order_sum += str_sum
                    print(f"{poz:>2}|{dlina:>4}|{visota:>4}|{kol:>2}|{vid:>3}| {str_sum} м.п.")
                print(f"Общий метраж: {order_sum:.2f} м.п.")
                break
        else:
            print("Заказ не найден")


if __name__ == '__main__':
    open_month("22.txt", "01")
    # open_order("22.txt", "0809")
