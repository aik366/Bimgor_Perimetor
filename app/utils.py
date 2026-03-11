from time import strftime
import datetime
import shutil
import os
from pathlib import Path

PATH = (Path(__file__).parent / "../DATA").resolve()


def open_file(file_name, month, mode="r"):
    with open(PATH / file_name, mode) as f:
        for i in [i.strip().split('\n') for i in f.read().split('#@#')[1:]]:
            st0, st1 = i[0].split('|'), i[1].split('|')
            if st0[2][3:5] == month and st0[12] == '  .  ':
                print(st0[0])
                for j in i[2:]:
                    poz, dlina, visota, kol, pusto, vid = j.split("|")[0:6]
                    if poz == "R":
                        continue
                    print(dlina, visota, kol, vid, f"{(int(dlina)*2+int(visota)*2)/1000*int(kol)}")


if __name__ == '__main__':
    open_file("22.txt", "03")
