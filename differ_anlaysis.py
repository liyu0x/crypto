import random

import numpy as np
import simple_cipher as sc

DIFFER_APPROXIMATION_TABLE = np.zeros((16, 16))


def get_differ_table():
    for i in range(16):
        for j in range(16):
            d_in = i ^ j
            d_out = sc.S_BOX[i] ^ sc.S_BOX[j]
            DIFFER_APPROXIMATION_TABLE[d_in][d_out] += 1


def crack_5th_round_partial(p_list: list, c_list: list):
    in_differ = 0x0B00
    out_differ = 0x0606
    res = np.zeros((16, 16))
    for i in range(16):
        for j in range(16):
            key = i << 8 | j
            for k in range(0, len(p_list) - 2, 2):
                p1 = p_list[k]
                p2 = p_list[k + 1]
                if p1 ^ p2 != in_differ:
                    raise Exception
                c1 = c_list[k] & 0x0F0F
                c2 = c_list[k + 1] & 0x0F0F
                c1 ^= key
                c2 ^= key
                c1 = sc.use_s_box_rev(c1)
                c2 = sc.use_s_box_rev(c2)
                if c1 ^ c2 == out_differ:
                    res[i][j] += 1
    for i in range(16):
        for j in range(16):
            res[i][j] /= 10000
    r, c = np.where(res == np.max(res))
    return r, c


def generate_differ_test_data():
    p_list = []
    c_list = []
    differ = 0x0B00
    fil = []
    sub_keys_list = [random.randint(0, 2 ** 16 - 1) for _ in range(5)]
    for i in range(0, 5000):
        p1 = random.randint(0, 2 ** 16 - 1)
        if p1 in fil:
            i -= 1
            continue
        fil.append(p1)
        p2 = p1 ^ differ
        c1 = sc.encrypt(p1, sub_keys_list)
        c2 = sc.encrypt(p2, sub_keys_list)
        p_list.append(p1)
        c_list.append(c1)
        p_list.append(p2)
        c_list.append(c2)
    return p_list, c_list, sub_keys_list
