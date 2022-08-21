import util
import copy

SIZE = 256
MSB = 0x80000000

P = [
    31, 23, 15, 7, 30, 22, 14, 6,
    29, 21, 13, 5, 28, 20, 12, 4,
    27, 19, 11, 3, 26, 18, 10, 2,
    25, 17, 9, 1, 24, 16, 8, 0
]

sfn = [  # [gen, exp]
    [375, 31],  # 101110111
    [379, 31],  # 101111011
    [391, 31],  # 110000111
    [395, 31],  # 110001011
    [397, 31],  # 110001101
    [415, 31],  # 110011111
    [419, 31],  # 110100011
    [425, 31],  # 110101001
    [433, 31],  # 110110001
    [445, 31],  # 110111101
    [451, 31],  # 111000011
    [463, 31],  # 111001111
    [471, 31],  # 111010111
    [477, 31],  # 111011101
    [487, 31],  # 111100111
    [499, 31],  # 111110011
    [00, 00]
]


def rol12(b):
    return (b << 12) | (b >> 20)


def ror12(b):
    return (b >> 12) | (b << 20)


def perm32(num: int):
    num_bits = util.convert_int_to_32_bin(num)
    temp = copy.deepcopy(num_bits)
    for i in range(32):
        num_bits[i] = temp[P[i]]
    return util.convert_bits_to_int(num_bits)


def exp8(base: int, exponent: int, gen: int):
    accum = base
    result = 1

    if base == 0:
        return 0

    while exponent != 0:
        if (exponent & 0x0001) == 0x0001:
            result = mult8(result, accum, gen)
        exponent >>= 1
        accum = mult8(accum, accum, gen)
    return result


def mult8(a: int, b: int, gen: int):
    product = 0
    while b != 0:
        if b & 1:
            product ^= a
            product &= 0xFFFF
        a <<= 1
        if a >= 256:
            a ^= gen
            a &= 0xFFFF
        b >>= 1
    return product


def s(i: int):
    r = ((i >> 8) & 0xc) | (i & 0x3)
    c = (i >> 2) & 0xff
    t = c ^ r
    v = exp8(t, sfn[r][0], sfn[r][1])
    length = (len(bin(v)) - 2)
    if length > 16:
        print("s function result bits:" + str(length))
    return v


MASK12 = 0x0fff


def f(r, k):
    # a = r ^ k
    # b = (s((a & MASK12)) & 0xFFFFFFFF) | \
    #     (0xFFFFFFFF & (s(((a >> 8) & MASK12)) << 8)) | \
    #     (0xFFFFFFFF & (s(((a >> 16) & MASK12)) << 16)) | \
    #     (0xFFFFFFFF & (s((((a >> 24) | (a << 8)) & MASK12))) << 24)
    # # return perm32(b)
    return r ^ k


def en_loki(block: list, keys: list):
    k_l = keys[0]
    k_r = keys[1]

    l_b = block[0] ^ k_l
    r_b = block[1] ^ k_r

    for i in range(8):
        l_b ^= f(r_b, k_l)
        rol12(k_l)
        r_b ^= f(l_b, k_r)
        rol12(k_r)

    block[0] = r_b ^ k_r
    block[1] = l_b ^ k_l


def de_loki(block: list, keys: list):
    k_l = keys[0]
    k_r = keys[1]

    r_b = block[0] ^ k_r
    l_b = block[1] ^ k_l

    for i in range(8):
        ror12(k_r)
        r_b ^= f(l_b, k_r)
        ror12(k_l)
        l_b ^= f(r_b, k_l)

    block[0] = l_b ^ k_l
    block[1] = r_b ^ k_r


def test():
    # 43297fad38e373fe 4c974f1caa59f5d4 ea676b2cb7db2b7a
    key = 0x43297fad38e373fe
    plaintext = 0xc974f1caa59f5d4
    ciphertext = 0xea676b2cb7db2b7a

    keys = util.split_64_bits_to_groups(key)
    pls = util.split_64_bits_to_groups(plaintext)
    print(pls)
    en_loki(pls, keys)

    de_loki(pls, keys)
    print(pls)
    res = util.merge_group_to_64_bits(pls)

test()
