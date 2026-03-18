from pathlib import Path
from colorama import init, Fore, Style

PATH = (Path(__file__).parent / "../DATA").resolve()

month_dict = {'01': 'Январь', '02': 'Февраль', '03': 'Март', '04': 'Апрель', '05': 'Май', '06': 'Июнь',
              '07': 'Июль', '08': 'Август', '09': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}

init()


def input_color(prompt, color=Fore.WHITE):
    return input(f"{color}{prompt}{Style.RESET_ALL}")


def print_color(text, color=Fore.WHITE):
    print(f"{color}{text}{Style.RESET_ALL}")


def open_month(file_name, month, mode="r"):
    with open(PATH / file_name, mode) as f:
        sum_pm, sum_pm_ser, sum_km, sum_km_ser = 0.0, 0.0, 0.0, 0.0
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[2][3:5] == f"{month:0>2}" and st0[12] == '  .  ':
                zakaz_sum_pm, zakaz_sum_km = 0.0, 0.0
                for j in i[2:]:
                    poz, dlina, visota, kol, pusto, vid = j.split("|")[0:6]
                    if poz == "R" or vid[0] in ("R", "К") or int(dlina) < 50 or int(visota) < 50:
                        continue
                    str_sum_pm = (int(dlina) * 2 + int(visota) * 2) / 1000 * int(kol)
                    str_sum_km = int(dlina) * int(visota) / 1000000 * int(kol)
                    zakaz_sum_pm += str_sum_pm
                    zakaz_sum_km += str_sum_km
                print_color(f"{st0[0]}: {zakaz_sum_pm:.2f} пм {zakaz_sum_km:.2f} км", Fore.YELLOW)
                if st0[1].strip() == "Сердюченко":
                    sum_pm_ser += zakaz_sum_pm
                    sum_km_ser += zakaz_sum_km
                else:
                    sum_pm += zakaz_sum_pm
                    sum_km += zakaz_sum_km

        print_color(
            f"Общий метраж Сердюченко, за {month_dict.get(f'{month:0>2}')} ({month:0>2}) : {sum_pm_ser:.2f} пм {sum_km_ser:.2f} км",
            Fore.GREEN)
        print_color(f"Общий метраж Мы, за {month_dict.get(f'{month:0>2}')} ({month:0>2}) : {sum_pm:.2f} пм {sum_km:.2f} км",
                    Fore.GREEN)
        print_color(f"Итого за {month_dict.get(f'{month:0>2}')} ({month:0>2}): {(sum_pm + sum_pm_ser):.2f} пм {(sum_km + sum_km_ser):.2f} км",
                    Fore.RED)


def open_order(file_name, order_number, mode="r"):
    with open(PATH / file_name, mode) as f:
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[0] == order_number and st0[12] == '  .  ':
                print_color(f"Заказ %: {st0[0]}", Fore.MAGENTA)
                order_sum_pm, order_sum_km = 0.0, 0.0
                for j in i[2:]:
                    str_sum_pm, str_sum_km = 0.0, 0.0
                    poz, dlina, visota, kol, pusto, vid = j.split("|")[0:6]
                    if poz == "R" or vid[0] in ("R", "К") or int(dlina) < 50 or int(visota) < 50:
                        continue
                    str_sum_pm = (int(dlina) * 2 + int(visota) * 2) / 1000 * int(kol)
                    str_sum_km = int(dlina) * int(visota) / 1000000 * int(kol)
                    order_sum_pm += str_sum_pm
                    order_sum_km += str_sum_km
                    print_color(f"{poz:>2}|{dlina:>4}|{visota:>4}|{kol:>2}|{vid:>3}| {str_sum_pm:.2f} пм {str_sum_km:.2f} км", Fore.YELLOW)
                print_color(f"Общий метраж: {order_sum_pm:.2f} пм {order_sum_km:.2f} км", Fore.GREEN)
                break
        else:
            print("Заказ не найден")


if __name__ == '__main__':
    open_month("22.txt", "01")
    # open_order("22.txt", "0809")
