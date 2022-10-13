def num_to_bits(num: int, length=32):
    binary = bin(num)[2:]
    res = [int(c) for c in binary]
    for z in range(len(res), length):
        res.insert(0, 0)
    return res


def bits_to_num(nums: list):
    res = ''
    for n in nums:
        res += str(n)
    return int(res, 2)


L1, L2 = None, None


def init_register(length_1: int, length_2: int):
    global L1, L2
    L1, L2 = [0 for i in range(length_1)], [0 for i in range(length_2)]


def into_registers(bits: list):
    i = 0
    for _ in range(len(L2)):
        L2[i] = bits[i]
        i += 1
    j = 0
    for _ in range(i, len(bits)):
        L1[j] = bits[i]
        j += 1
        i += 1
    L1.reverse()


def katan32(plaintext: int):
    length = 32
    init_register(13, 19)
    bits = num_to_bits(plaintext, length)
    into_registers(bits)
    print(bits)
    print(L2)
    print(L1)
katan32(23)
