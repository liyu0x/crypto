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
