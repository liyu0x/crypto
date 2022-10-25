import random

import numpy as np
import simple_cipher as sc
import util

linear_differ_table = np.zeros((16, 16))

max_approximation = 0

max_approximation_pair = {}


def linear_approximation_table():
    global max_approximation, linear_differ_table
    for i in range(16):
        for j in range(16):
            for k in range(16):
                if bitwise_xor(i & j) == bitwise_xor(sc.S_BOX[i] & k):
                    linear_differ_table[j][k] += 1
    for i in range(16):
        for j in range(16):
            linear_differ_table[i][j] -= 8
            if linear_differ_table[i][j] != 8:
                max_approximation = max(max_approximation, abs(linear_differ_table[i][j]))


def find_max_approximation_mask():
    global linear_differ_table, max_approximation, max_approximation_pair
    for i in range(0, 16):
        for j in range(0, 16):
            if abs(linear_differ_table[i][j]) == max_approximation:
                max_approximation_pair[i] = j


def print_linear_approximation_table():
    for row in linear_differ_table:
        for col in row:
            if col >= 0:
                print(" " + str(col), end=' ')
            else:
                print(col, end=' ')
        print()


def bitwise_xor(num):
    bits = util.convert_int_16_bits_to_bin(num)
    res = 0
    for b in bits:
        res ^= b
    return res


def crack_5_round_partial(p_list: list, c_list: list):
    res = np.zeros((16, 16))
    for i in range(16):
        for j in range(16):
            count = 0
            key = (i << 8) | j
            for k in range(10000):
                p = p_list[k] & 0x0B00
                c = sc.use_s_box_rev(c_list[k] ^ key) & 0x0505
                if util.bit_xor(p, c) == 0:
                    count += 1
            res[i][j] = abs(count - 5000) / 10000
    r, c = np.where(res == np.max(res))
    return r[0], c[0]


def generate_linear_test_data():
    p_list = []
    c_list = []
    sub_keys_list = [random.randint(0, 2 ** 16 - 1) for _ in range(5)]
    for i in range(10000):
        p = random.randint(0, 2 ** 16 - 1)
        c = sc.encrypt(p, sub_keys_list)
        p_list.append(p)
        c_list.append(c)
    return p_list, c_list, sub_keys_list
