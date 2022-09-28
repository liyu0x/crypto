from util import *


def start():
    for index in range(1, 2 ** 64):
        pro_list = list()
        pro_list.append([-1, 1, 1])
        compute_start(index, 1, 1, pro_list, 0)
    print(MAX_PRO)


if __name__ == '__main__':
    start()
