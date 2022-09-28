import random


def convert_int_16_bits_to_bin(num: int):
    binary = bin(num)[2:]
    res = [int(c) for c in binary]
    for z in range(len(res), 16):
        res.insert(0, 0)
    return res


def convert_int_64_bits_to_bin(num: int):
    binary = bin(num)[2:]
    res = [int(c) for c in binary]
    for z in range(len(res), 64):
        res.insert(0, 0)
    return res


def convert_int_4_bits_to_bin(num: int):
    binary = bin(num)[2:]
    res = [int(c) for c in binary]
    for z in range(len(res), 4):
        res.insert(0, 0)
    return res


def convert_bits_to_int(nums: list):
    res = ''
    for n in nums:
        res += str(n)
    return int(res, 2)


def convert_16_int_to_4_int(num: int):
    bits = convert_int_16_bits_to_bin(num)
    res = []
    res[0] = convert_bits_to_int(bits[0:4])
    res[1] = convert_bits_to_int(bits[4:8])
    res[2] = convert_bits_to_int(bits[8:12])
    res[3] = convert_bits_to_int(bits[12:16])
    return res


def get_active_box(num: int):
    s_boxes = []
    num_bits = convert_int_16_bits_to_bin(num)
    if convert_bits_to_int(num_bits[0:4]) != 0:
        s_boxes.append(1)
    if convert_bits_to_int(num_bits[4:8]) != 0:
        s_boxes.append(2)
    if convert_bits_to_int(num_bits[8:12]) != 0:
        s_boxes.append(3)
    if convert_bits_to_int(num_bits[12:16]) != 0:
        s_boxes.append(4)
    return s_boxes


def get_available_int_by_active_box(boxes: list):
    num = 0xFFFF
    if 4 not in boxes:
        num &= 0xFFF0
    if 3 not in boxes:
        num &= 0xFF0F
    if 2 not in boxes:
        num &= 0xF0FF
    if 1 not in boxes:
        num &= 0x0FFF
    return num


def bit_xor(*n):
    res = 0
    for i in n:
        for b in convert_int_16_bits_to_bin(i):
            res ^= b
    return res


def write_data_to_file(p_list: list, c_list: list, sub_key_list: list, analysis_type: str):
    f1 = open('plain_' + analysis_type, 'w')
    f2 = open('cipher_' + analysis_type, 'w')
    f3 = open('key_' + analysis_type, 'w')
    [f1.write(str(p) + "\n") for p in p_list]
    [f2.write(str(c) + "\n") for c in c_list]
    [f3.write(str(key) + "\n") for key in sub_key_list]
    f1.close()
    f2.close()
    f3.close()


def load_data(analysis_type: str):
    f = open('plain_' + analysis_type, 'r')
    p_list = [int(s) for s in f.readlines()]
    f.close()
    f = open('cipher_' + analysis_type, 'r')
    c_list = [int(s) for s in f.readlines()]
    f.close()
    f = open('key_' + analysis_type, 'r')
    key_list = [int(s) for s in f.readlines()]
    f.close()
    return p_list, c_list, key_list
