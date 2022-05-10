import sys
import time

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


def crack_5_round(p_list: list, c_list: list):
    # last round
    # res = np.zeros((16, 16))
    # for i in range(16):
    #     for j in range(16):
    #         count = 0
    #         key = (i << 8) | j
    #         for k in range(10000):
    #             p = p_list[k] & 0x0B00
    #             c = sc.use_s_box_rev(c_list[k] ^ key) & 0x0505
    #             if util.bit_xor(p, c) == 0:
    #                 count += 1
    #         res[i][j] = abs(count - 5000) / 10000
    # r, c = np.where(res == np.max(res))

    res = np.zeros((16, 16))
    for i in range(16):
        for j in range(16):
            count = 0
            key = (i << 4) | j
            for k in range(10000):
                p = p_list[k] & 0x0001
                c = sc.use_s_box_rev(c_list[k] ^ key) & 0x0077
                if util.bit_xor(p, c) == 0:
                    count += 1
            res[i][j] = abs(count - 5000) / 10000
    r1, c1 = np.where(res == np.max(res))
    print(r1[0])
    print(c1[0])


def crack_4_round(sub_key_5: int, p_list: list, c_list: list):
    res = np.zeros((16, 16))
    for i in range(16):
        for j in range(16):
            count = 0
            count = 0
            key = (i << 8) | j & 0x0505
            for k in range(10000):
                p = p_list[k] & 0x0B00
                c = sc.use_s_box_rev(c_list[k] ^ sub_key_5)
                c = sc.use_p_box(c ^ key)
                c = sc.use_s_box_rev(c) & 0x0404
                if util.bit_xor(p, c) == 0:
                    count += 1
            res[i][j] = abs(count - 5000) / 10000
    r, c = np.where(res == np.max(res))
    print(np.max(res))
    key4 = r << 8 | c
    print(res[c[0]][r[0]])
    print(r[0])
    print(c[0])


all_res = []


def recursive(num, i, res: list):
    global all_res
    if num == 0:
        return
    if i == 4:
        all_res.append(res)
    active_boxes = util.get_active_box(num)
    mask = util.get_available_int_by_active_box(active_boxes)
    res.append(active_boxes)
    for i in range(256):
        n_res = res[:]
        n = i & mask
        n = sc.use_p_box(n)
        recursive(n, i + 1, n_res)


def test():
    f = open('plain', 'r')
    p_list = [int(s) for s in f.readlines()]
    f.close()
    f = open('cipher', 'r')
    c_list = [int(s) for s in f.readlines()]
    f.close()
    f = open('key', 'r')
    key_list = [int(s) for s in f.readlines()]
    f.close()

    real_key5_bits = util.convert_int_16_bits_to_bin(key_list[4])
    real_key4_bits = util.convert_int_16_bits_to_bin(key_list[3])
    key1 = util.convert_bits_to_int(real_key5_bits[4:8])
    key2 = util.convert_bits_to_int(real_key5_bits[12:16])
    key3 = util.convert_bits_to_int(real_key5_bits[0:4])
    key4 = util.convert_bits_to_int(real_key5_bits[8:12])
    print("key52:" + str(key1) + "   key54:" + str(key2))
    print("key42:" + str(key3) + "   key44:" + str(key4))

    start = time.time()
    crack_5_round(p_list, c_list)
    linear_approximation_table()
    print()
    print(time.time() - start)


sys.setrecursionlimit(256 * 256 * 256)
recursive(1, 1, [])

print(sys.getrecursionlimit())
