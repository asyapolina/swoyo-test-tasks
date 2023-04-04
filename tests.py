import json
import pytest

from prime_numbers import prime_numbers
from text_statistics import text_stat
from convert_numerals import roman_numerals_to_int

class TestPrimeNumbers:
    @pytest.mark.parametrize("low, high, expected_result", [
        (1, 7, [2, 3, 5, 7]),
        (22, 30, [23, 29]),
        (0, 1, []),
    ])
    def test_prime_numbers(self, low, high, expected_result):
        assert prime_numbers(low, high) == expected_result

    @pytest.mark.parametrize("low, high", [
        (10, 0),
        (-5, -1),
    ])
    def test_correct_input(self, low, high):
        with pytest.raises(IndexError):
            assert prime_numbers(low, high)

    @pytest.mark.parametrize("low, high", [
        ("a","b"),
        (2, "b"),
        ("a", 5),
        ("\n","\n"),
        (" "," "),
    ])
    def test_no_numbers(self, low, high):
        with pytest.raises(TypeError):
            assert prime_numbers(low, high)


class TestTextStat:
    @staticmethod
    def compare_text_stats(result: dict, expected: dict) -> bool:
        equal = True
        for key, val in result.items():
            if isinstance(val, tuple) and isinstance(expected[key], list):
                actual_wc, actual_wshare = val
                expected_wc, expected_wshare = expected[key]
                equal = actual_wc == expected_wc and actual_wshare == expected_wshare
            elif isinstance(val, int) and isinstance(expected[key], int):
                actual_count = val
                expected_count = expected[key]
                equal = actual_count == expected_count
            else:
                return False
            if not equal:
                return False
        return True

    prefix = "test_data/"

    @pytest.mark.parametrize("text_input, expected_result_json", [
        ("empty.txt", "empty.json"),
        ("mixed_text.txt", "mixed_text.json"),
        ("one_bilingual_word.txt", "one_bilingual_word.json"),
        ("plain_text_cyr.txt", "plain_text_cyr.json"),
        ("plain_text_lat.txt", "plain_text_lat.json"),
        ("text_with_nums_and_punctuation.txt", "text_with_nums_and_punctuation.json"),
        ("two_paragraphs.txt", "two_paragraphs.json"),
        ("simple_sentences.txt", "simple_sentences.json"),
    ])
    def test_text_stat(self, text_input, expected_result_json):
        result = text_stat(TestTextStat.prefix + text_input)
        with open(TestTextStat.prefix + expected_result_json, 'r') as fp:
            expected = json.load(fp)
        assert TestTextStat.compare_text_stats(result, expected)


class TestRomanNumbersToInt:
    @pytest.mark.parametrize("roman_numeral, expected_result", [
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("IV", 4),
        ("V", 5),
        ("VI", 6),
        ("VII", 7),
        ("VIII", 8),
        ("IX", 9),
        ("X", 10),
        ("XI", 11),
        ("XII", 12),
        ("XIII", 13),
        ("XV", 15),
        ("XVIII", 18),
        ("XIX", 19),
        ("XX", 20),
        ("XXII", 22),
        ("XXX", 30),
        ("XL", 40),
        ("XLV", 45),
        ("L", 50),
        ("LV", 55),
        ("LVII", 57),
        ("XCVI", 96),
        ("XCIX", 99),
        ("C", 100),
        ("CV", 105),
        ("CX", 110),
        ("CXIII", 113),
        ("CD", 400),
        ("CDX", 410),
        ("D", 500),
        ("DC", 600),
        ("CML", 950),
        ("CMXC", 990),
        ("MC", 1100),
        ("MCCVII", 1207),
        ("MD", 1500),
        ("MMXXIII", 2023),
        ("MMMDCCCLXXXVIII", 3888),
        ("MMMCMXCIX", 3999),
    ])
    def test_roman_numerals_to_int(self, roman_numeral, expected_result):
        assert roman_numerals_to_int(roman_numeral) == expected_result

    @pytest.mark.parametrize("roman_numeral, expected_result", [
        ("IIII", None),
        ("VV", None),
        ("LL", None),
        ("DD", None),
        ("XXXX", None),
        ("CCCC", None),
        ("MMMM", None),
        ("IVI", None),
        ("IIX", None),
    ])
    def test_correct_roman_numerals(self, roman_numeral, expected_result):
        assert roman_numerals_to_int(roman_numeral) == expected_result

if __name__ == "__main__":
    pytest.main()