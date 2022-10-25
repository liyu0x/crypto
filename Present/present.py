import Diff_Linear.util as com_util
import copy

S_BOX = [0xC, 0x5, 0x6, 0xB, 0x9, 0x00, 0xA, 0xD, 0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]
S_BOX_REV = [0x5, 0xE, 0xF, 0x8, 0xC, 0x1, 0x2, 0xD, 0xB, 0x4, 0x6, 0x3, 0x0, 0X7, 0x9]

P_BOX_BIT_POS = [[0, 0],
                 [1, 16],
                 [2, 32],
                 [3, 48],
                 [4, 1],
                 [5, 17],
                 [6, 33],
                 [7, 49],
                 [8, 2],
                 [9, 18],
                 [10, 34],
                 [11, 50],
                 [12, 3],
                 [13, 19],
                 [14, 35],
                 [15, 51],
                 [16, 4],
                 [17, 20],
                 [18, 36],
                 [19, 52],
                 [20, 5],
                 [21, 21],
                 [22, 37],
                 [23, 53],
                 [24, 6],
                 [25, 22],
                 [26, 38],
                 [27, 54],
                 [28, 7],
                 [29, 23],
                 [30, 39],
                 [31, 55],
                 [32, 8],
                 [33, 24],
                 [34, 40],
                 [35, 56],
                 [36, 9],
                 [37, 25],
                 [38, 41],
                 [39, 57],
                 [40, 10],
                 [41, 26],
                 [42, 42],
                 [43, 58],
                 [44, 11],
                 [45, 27],
                 [46, 43],
                 [47, 59],
                 [48, 12],
                 [49, 28],
                 [50, 44],
                 [51, 60],
                 [52, 13],
                 [53, 29],
                 [54, 45],
                 [55, 61],
                 [56, 14],
                 [57, 30],
                 [58, 46],
                 [59, 62],
                 [60, 15],
                 [61, 31],
                 [62, 47],
                 [63, 63]]


def apply_p_box(num: int):
    bits = com_util.convert_int_64_bits_to_bin(num)
    temp_bits = copy.deepcopy(bits)
    bits.reverse()
    temp_bits.reverse()
    for i in range(64):
        bits[P_BOX_BIT_POS[i][1]] = temp_bits[i]
    bits.reverse()
    return com_util.convert_bits_to_int(bits)
