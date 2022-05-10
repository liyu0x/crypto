import copy
import random
import util

S_BOX = [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7]

S_BOX_REV = [0xE, 0x3, 0x4, 0x8, 0x1, 0xC, 0xA, 0xF, 0x7, 0xD, 0x9, 0x6, 0xB, 0x2, 0x0, 0x5]

P_BOX = [0x0, 0x4, 0x8, 0xC, 0x1, 0x5, 0x9, 0xD, 0x2, 0x6, 0xA, 0xE, 0x3, 0x7, 0xB, 0xF]

A_ROUND_S_BOX_NUM = 4


def encrypt(num: int, sub_keys: list):
    if not checks_params(num, sub_keys):
        raise Exception
    plain_bit_list = util.convert_int_16_bits_to_bin(num)
    keys_num = len(sub_keys)
    for i in range(keys_num - 2):
        key_mixing(plain_bit_list, util.convert_int_16_bits_to_bin(sub_keys[i]))
        use_s_box_or_rev(plain_bit_list, S_BOX)
        p_box_inner(plain_bit_list)
    key_mixing(plain_bit_list, util.convert_int_16_bits_to_bin(sub_keys[keys_num - 2]))
    use_s_box_or_rev(plain_bit_list, S_BOX)
    key_mixing(plain_bit_list, util.convert_int_16_bits_to_bin(sub_keys[keys_num - 1]))
    return util.convert_bits_to_int(plain_bit_list)


def decrypt(num: int, sub_keys: list):
    cipher_bit_list = util.convert_int_16_bits_to_bin(num)
    keys_num = len(sub_keys)
    key_mixing(cipher_bit_list, util.convert_int_16_bits_to_bin(sub_keys[keys_num - 1]))
    use_s_box_or_rev(cipher_bit_list, S_BOX_REV)
    key_mixing(cipher_bit_list, util.convert_int_16_bits_to_bin(sub_keys[keys_num - 2]))
    for i in range(keys_num - 3, -1, -1):
        p_box_inner(cipher_bit_list)
        use_s_box_or_rev(cipher_bit_list, S_BOX_REV)
        key_mixing(cipher_bit_list, util.convert_int_16_bits_to_bin(sub_keys[i]))
    return util.convert_bits_to_int(cipher_bit_list)


def use_s_box_or_rev(bit_list: list, substitution: list):
    for i in range(0, A_ROUND_S_BOX_NUM * 4, 4):
        n = util.convert_bits_to_int(bit_list[i: i + 4])
        n = substitution[n]
        n_bin = util.convert_int_16_bits_to_bin(n)
        bit_list[i] = n_bin[-4]
        bit_list[i + 1] = n_bin[-3]
        bit_list[i + 2] = n_bin[-2]
        bit_list[i + 3] = n_bin[-1]


def key_mixing(bit_list: list, keys_bit_list: list):
    for i in range(16):
        bit_list[i] = bit_list[i] ^ keys_bit_list[i]


def p_box_inner(byte_bit_list: list):
    temp = copy.deepcopy(byte_bit_list)
    for i in range(16):
        ni = P_BOX[i]
        byte_bit_list[i] = temp[ni]


def checks_params(num: int, sub_keys: list):
    if num > (2 ** 16 - 1) or len(sub_keys) != 5:
        return False
    for sub_key in sub_keys:
        if sub_key > (2 ** 16 - 1):
            return False

    return True


def use_s_box_rev(num):
    bits = util.convert_int_16_bits_to_bin(num)
    res = 0
    res |= (S_BOX_REV[util.convert_bits_to_int(bits[0:4])] << 12)
    res |= (S_BOX_REV[util.convert_bits_to_int(bits[4:8])] << 8)
    res |= (S_BOX_REV[util.convert_bits_to_int(bits[8:12])] << 4)
    res |= S_BOX_REV[util.convert_bits_to_int(bits[12:16])]
    return res


def use_p_box(num):
    bits = util.convert_int_16_bits_to_bin(num)
    p_box_inner(bits)
    return util.convert_bits_to_int(bits)


def asdfdsafdasfdfs():
    f1 = open('plain', 'w')
    f2 = open('cipher', 'w')
    f3 = open('key', 'w')
    key_list = [random.randint(0, 2 ** 16 - 1) for _ in range(5)]
    [f3.write(str(key) + "\n") for key in key_list]
    for i in range(10000):
        p = random.randint(0, 2 ** 16 - 1)

        c = encrypt(p, key_list)
        re = decrypt(c, key_list)
        assert re == p
        f1.write(str(p) + "\n")
        f2.write(str(c) + "\n")
    f1.close()
    f2.close()
    f3.close()
