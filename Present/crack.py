import json
import present

IN_DIFF = 0x0000D00D00000000
OUT_DIFF = 0x0000040400000404

DATA_SIZE = 12

ROUND_NUM = 5
SUB_KEY_SIZE = 64


def load_data():
    sub_keys = json.load(open('sub_keys.json', 'r'))
    ori_data = json.load(open('ori_data.json', 'r'))
    diff_data = json.load(open('diff_data.json', 'r'))
    return sub_keys, ori_data, diff_data


def crack():
    sub_keys, ori_data, diff_data = load_data()
    counter = [0 for _ in range(2 ** 16)]
    for i in range(len(ori_data)):
        ori_pair = ori_data[i]
        diff_pair = diff_data[i]
        if (ori_pair[0] ^ diff_pair[0]) != IN_DIFF:
            print("ERROR")
            continue
        for vir_sub_key in range(2 ** 16):
            subkey = ((((vir_sub_key >> 12) & 0xf) << 40) | (((vir_sub_key >> 8) & 0xf) << 32) | (
                    (vir_sub_key >> 4 & 0xf) << 8) | vir_sub_key & 0xf)
            ori_c = present.decrypt(ori_pair[1], subkey) & 0x00000F0F00000F0F
            diff_c = present.decrypt(diff_pair[1], subkey) & 0x00000F0F00000F0F
            if (ori_c ^ diff_c) == OUT_DIFF:
                counter[vir_sub_key] += 1
    max_key = max(counter)
    print(counter.index(max_key))
    print(sub_keys[ROUND_NUM - 1])


crack()
