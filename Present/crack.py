import json
import present

IN_DIFF = 0x0000D00D00000000
OUT_DIFF = 0x0000040400000404

DATA_SIZE = 6

ROUND_NUM = 5
SUB_KEY_SIZE = 64

BLOCK_SIZE = 64
S_BOX_SIZE = 4

ACTIVE_S_BOX_NUM = 0

MASK = None


def gen_mask():
    global MASK, ACTIVE_S_BOX_NUM
    mask = 0
    active_num = 0
    for i in range(int(BLOCK_SIZE / S_BOX_SIZE)):
        mask |= (0x0 if ((OUT_DIFF >> (i * S_BOX_SIZE)) & 0xF) == 0 else 0xF) << (i * S_BOX_SIZE)
        active_num += (0 if ((OUT_DIFF >> (i * S_BOX_SIZE)) & 0xF) == 0 else 1)
    MASK = mask
    ACTIVE_S_BOX_NUM = active_num


def generate_sub_key(key: int):
    n_key = 0
    for i in range(int(BLOCK_SIZE / S_BOX_SIZE)):
        if ((OUT_DIFF >> (i * S_BOX_SIZE)) & 0xF) != 0:
            n_key |= (key & 0xF) << (i * S_BOX_SIZE)
            key >>= 4
    return n_key


def load_data():
    sub_keys = json.load(open('sub_keys.json', 'r'))
    ori_data = json.load(open('ori_data.json', 'r'))
    diff_data = json.load(open('diff_data.json', 'r'))
    return sub_keys, ori_data, diff_data


def crack():
    gen_mask()
    sub_keys, ori_data, diff_data = load_data()
    counter = [0 for _ in range(2 ** 16)]
    for i in range(len(ori_data)):
        ori_pair = ori_data[i]
        diff_pair = diff_data[i]
        if (ori_pair[0] ^ diff_pair[0]) != IN_DIFF:
            print("ERROR")
            continue
        for vir_sub_key in range(2 ** 16):
            subkey = generate_sub_key(vir_sub_key)
            ori_c = present.decrypt(ori_pair[1], subkey) & MASK
            diff_c = present.decrypt(diff_pair[1], subkey) & MASK
            if (ori_c ^ diff_c) == OUT_DIFF:
                counter[vir_sub_key] += 1
    max_key = max(counter)
    print(hex(generate_sub_key(counter.index(max_key))))
    print(hex(sub_keys[ROUND_NUM - 1]))


if __name__ == "__main__":
    crack()
