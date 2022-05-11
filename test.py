import time

import differ_anlaysis as da
import util
import linear_analysis as la


def generate_data():
    print("staring")
    p_list, c_list, sub_keys_list = la.generate_linear_test_data()
    util.write_data_to_file(p_list, c_list, sub_keys_list, 'linear')
    p_list, c_list, sub_keys_list = da.generate_differ_test_data()
    util.write_data_to_file(p_list, c_list, sub_keys_list, 'differ')
    print("done")


def test_linear():
    p_list, c_list, key_list = util.load_data('linear')
    real_key5_bits = util.convert_int_16_bits_to_bin(key_list[4])
    key1 = util.convert_bits_to_int(real_key5_bits[4:8])
    key2 = util.convert_bits_to_int(real_key5_bits[12:16])
    start = time.time()
    re_key1, re_key2 = la.crack_5_round_partial(p_list, c_list)
    print(time.time() - start)
    assert re_key1 == key1 and re_key2 == key2


def test_differ():
    p_list, c_list, key_list = util.load_data('differ')
    real_key5_bits = util.convert_int_16_bits_to_bin(key_list[4])
    key1 = util.convert_bits_to_int(real_key5_bits[4:8])
    key2 = util.convert_bits_to_int(real_key5_bits[12:16])
    print("k52:" + str(key1) + "|k52:" + str(key2))
    re_key1, re_key2 = da.crack_5th_round_partial(p_list, c_list)
    assert re_key1 == key1 and re_key2 == key2


def test():
    test_linear()
    test_differ()
