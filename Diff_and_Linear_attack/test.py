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
    print("-----------------------------------")
    print("starting linear cryptanalysis")
    p_list, c_list, key_list = util.load_data('linear')
    real_key5_bits = util.convert_int_16_bits_to_bin(key_list[4])
    key1 = util.convert_bits_to_int(real_key5_bits[4:8])
    key2 = util.convert_bits_to_int(real_key5_bits[12:16])
    start = time.time()
    re_key1, re_key2 = la.crack_5_round_partial(p_list, c_list)
    print("correct key1:{}     correct key2:{}".format(key1, key2))
    print("recovered key1:{}     recovered key2:{}".format(re_key1, re_key2))
    print("time: {} s".format(time.time() - start))


def test_differ():
    print("-----------------------------------")
    print("starting linear cryptanalysis")
    p_list, c_list, key_list = util.load_data('differ')
    real_key5_bits = util.convert_int_16_bits_to_bin(key_list[4])
    key1 = util.convert_bits_to_int(real_key5_bits[4:8])
    key2 = util.convert_bits_to_int(real_key5_bits[12:16])
    start = time.time()
    re_key1, re_key2 = da.crack_5th_round_partial(p_list, c_list)
    print("correct key1:{}     correct key2:{}".format(key1, key2))
    print("recovered key1:{}     recovered key2:{}".format(re_key1, re_key2))
    print("time: {} s".format(time.time() - start))


def test():
    #test_linear()
    test_differ()


if __name__ == '__main__':
    test()
