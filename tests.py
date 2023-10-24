import pytest

import tasks


def test_pn_normal_out():
    assert tasks.prime_numbers(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_pn_bad_arguments_low():
    assert tasks.prime_numbers(-5, 15) == []


def test_pn_bad_arguments_high():
    assert tasks.prime_numbers(5, -2) == []


def test_pn_bad_arguments_low_high_negative_value():
    assert tasks.prime_numbers(-11, -2) == []


def test_pn_bad_arguments_low_high_positive_value():
    assert tasks.prime_numbers(11, 2) == []


def test_ts_normal_out():
    assert tasks.text_stat('Test.txt')['paragraph_amount'] == 3


def test_ts_bad_filename():
    assert tasks.text_stat('tst') == {'error': 'file not found'}


def test_ts_bad_filename():
    assert tasks.text_stat('tst') == {'error': 'file not found'}


def test_ts_invalid_argument():
    assert tasks.text_stat(5) == {'error': 'filename not a string'}


def test_rn_normal_out():
    assert tasks.roman_numerals_to_int('MCXIX') == 1119


def test_rn_bad_input():
    assert tasks.roman_numerals_to_int('IMVX') == None


if __name__ == '__main__':
    pytest.main()
