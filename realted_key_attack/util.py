import random


def convert_int_to_32_bin(num: int):
    binary = bin(num)[2:]
    res = [int(c) for c in binary]
    for z in range(len(res), 32):
        res.insert(0, 0)
    return res


def convert_bits_to_int(nums: list):
    res = ''
    for n in nums:
        res += str(n)
    return int(res, 2)


def split_64_bits_to_groups(num: int):
    l_b = num & 0x00000000FFFFFFFF
    res = list()
    res.append(l_b)
    r_b = num & 0xFFFFFFFF00000000
    r_b >>= 32
    res.append(r_b)
    return res


def merge_group_to_64_bits(groups: list):
    return (groups[0] << 32) | groups[1]


def generate_perm():
    flag = [0 for i in range(32)]

    result = [i for i in range(32)]

    for i in range(32):
        if flag[i]:
            continue
        n = 0
        while True:
            n = random.randint(0, 31)
            if not flag[n]:
                break
        temp = result[i]
        result[i] = result[n]
        result[n] = temp
        flag[i] = 1
        flag[n] = 1
    print(result)
