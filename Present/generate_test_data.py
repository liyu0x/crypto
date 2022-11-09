import present
import crack
import random
import json


def generate_sub_key():
    sub_keys = []
    for i in range(crack.ROUND_NUM):
        sub_keys.append(random.randint(0, 2 ** crack.SUB_KEY_SIZE))
    return sub_keys


def generate_test_data():
    sub_keys = generate_sub_key()
    ori_p = []
    ori_data = []
    diff_data = []
    for i in range(2 ** crack.DATA_SIZE):
        p = random.randint(0, 2 ** 64)
        if p in ori_p:
            i -= 1
            continue
        ori_p.append(p)
        ori_pair = []
        diff_pair = []
        dp = p ^ crack.IN_DIFF
        ori_pair.append(p)
        diff_pair.append(dp)
        c = p
        dc = dp
        for j in range(crack.ROUND_NUM):
            c = present.encrypt(c, sub_keys[j])
            dc = present.encrypt(dc, sub_keys[j])
        ori_pair.append(c)
        diff_pair.append(dc)
        ori_data.append(ori_pair)
        diff_data.append(diff_pair)
    with open('ori_data.json', 'w') as fp:
        json.dump(ori_data, fp)
    with open('diff_data.json', 'w') as fp:
        json.dump(diff_data, fp)
    with open('sub_keys.json', 'w') as fp:
        json.dump(sub_keys, fp)


generate_test_data()
