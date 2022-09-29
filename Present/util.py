import copy
import datetime
import math

import present
import numpy as np
import matplotlib.pyplot as plt
import Diff_Linear.util as com_util
from itertools import product
from datetime import datetime

DIFFER_APPROXIMATION_TABLE = np.zeros((16, 16))
USABLE_DIFFER = None
FILE = None
MAX_PRO = 0

SINGLE_ACTIVE_NUM_LIM = 16 / 2

ALL_ACTIVE_NUM_LIM = 5 * 16 / 2

WRITE_FILE = False
RECORD_NUM = 10 ** 1000000


# compute different distributed table
def compute_ddt():
    global DIFFER_APPROXIMATION_TABLE
    for i in range(16):
        for j in range(16):
            d_in = i ^ j
            d_out = present.S_BOX[i] ^ present.S_BOX[j]
            DIFFER_APPROXIMATION_TABLE[d_in][d_out] += 1


# draw ddt table
def draw_ddt_table():
    fig, ax = plt.subplots()
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    color_arr = list()
    for i in range(16):
        tl = list()
        for j in range(16):
            if DIFFER_APPROXIMATION_TABLE[i][j] == 2:
                tl.append("red")
            elif DIFFER_APPROXIMATION_TABLE[i][j] == 4:
                tl.append('pink')
            else:
                tl.append('yellow')
        color_arr.append(tl)
    ax.table(cellText=DIFFER_APPROXIMATION_TABLE
             , colLabels=[i for i in range(16)]
             , rowLabels=[i for i in range(16)]
             , colColours=['green' for i in range(16)]
             , rowColours=['green' for i in range(16)]
             , cellColours=color_arr
             , loc='center')
    fig.tight_layout()
    plt.show()


def convert_64bit_into_16_4bit(num: int):
    bits = com_util.convert_int_64_bits_to_bin(num)
    res = [0 for i in range(16)]
    for i in range(16):
        res[i] = com_util.convert_bits_to_int(bits[i * 4:i * 4 + 4])
    return res


# find non-zero and max different value in each row
def compute_differ_out():
    global USABLE_DIFFER
    res = list()
    res.append([0])
    for i in range(1, 16):
        out_res = list()
        num = 0
        for o in range(0, 16):
            if DIFFER_APPROXIMATION_TABLE[i][o] == 4:
                out_res.append(o)
                num += 1
        if num == 0:
            for o in range(0, 16):
                if DIFFER_APPROXIMATION_TABLE[i][o] == 2:
                    out_res.append(o)
        res.append(out_res)
    USABLE_DIFFER = res


# s-boxed bits to int
def bits_to_int_by_active_box(bits: list, active_box_num: list):
    res = 0
    rev_bx = active_box_num
    rev_bits = bits[::-1]
    ind = 0
    for b in rev_bx:
        res <<= 4
        if b == 0:
            continue
        else:
            res |= rev_bits[ind]
            ind += 1
    return res


def compute_prob(out_differ: int, round_num: int, prob: float, record_list: list, total_active_num: int):
    global MAX_PRO
    if round_num == 5:
        MAX_PRO = max(MAX_PRO, prob)
        format_print(record_list)
        return
    usable_out_differ, in_differs, active_num = compute_possible_out_differ(out_differ)
    total_active_num += active_num
    if active_num >= ALL_ACTIVE_NUM_LIM:
        return
    for out_differ_list in usable_out_differ:
        dif = list(out_differ_list)
        out_dif = bits_to_int_by_active_box(dif, in_differs)
        prob = prob * compute_single_layer_probability(in_differs, dif)
        if prob == 0:
            return
        n_l = copy.deepcopy(record_list)
        n_out_diff = present.apply_p_box(out_dif)
        n_l.append([record_list[len(record_list) - 1][1], n_out_diff, prob, total_active_num])
        compute_prob(n_out_diff, round_num + 1, prob, n_l, total_active_num)


def compute_single_layer_probability(in_differs: list, out_differs: list):
    probs = list()
    ots = out_differs[::-1]
    index = 0
    for i in range(16):
        ind = in_differs[i]
        if ind == 0:
            continue
        oud = ots[index]
        probs.append(DIFFER_APPROXIMATION_TABLE[ind][oud])
    prob = 1
    for p in probs:
        # prob = prob * (p / (2 ** 4))
        prob = prob * p
    return int(prob)


# find out_differ that is non-zero different value
def compute_possible_out_differ(in_differ):
    _4bit_int = convert_64bit_into_16_4bit(in_differ)
    possible_diff_list = list()
    active_box_num = 0
    for index, single_box_in_differ in enumerate(_4bit_int):
        if single_box_in_differ == 0:
            continue
        possible_diff_list.append(USABLE_DIFFER[single_box_in_differ])
        active_box_num += 1
    perm = product(*possible_diff_list)
    # if active box num is more than LIMIT then stop to find
    if active_box_num >= SINGLE_ACTIVE_NUM_LIM:
        return list(), list(), 0
    return list(perm), _4bit_int, active_box_num


def create_new_file():
    global FILE
    if FILE is not None:
        FILE.close()
    FILE = open(str(datetime.now()) + ".txt", 'w')


# format print
def format_print(records: list):
    for index, record in enumerate(records):
        print("round-" + str(index) + ":[", end="")
        print('input differ: %#x' % record[0], end=",")
        print('output differ(p-boxed): %#x' % record[1], end=",")
        if index == 0:
            print("w=1", end=", ")
        else:
            print('w=%d' % record[2], end=",")
        print('all active boxes:%#d' % record[3], end="] ")

    print()
    print()


# main worker
def compute_start(out_differ: int, round_num: int, prob: float, record_list: list, total_active_num: int):
    compute_ddt()
    compute_differ_out()
    compute_prob(out_differ, round_num, prob, record_list, total_active_num)
