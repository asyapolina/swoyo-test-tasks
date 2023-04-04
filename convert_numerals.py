import re

def roman_numerals_to_int(roman_numeral:str) -> int:
    """Convert a number consisting of Roman numerals to an integer."""
    # checking for valid input
    if re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman_numeral) is None:
        return None
    roman_to_int_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res = 0
    # finding the answer
    for num in reversed(roman_numeral):
        n = roman_to_int_map[num]
        if 3 * n < res:
            res -= n
        else:
            res += n
    return res

if __name__ == "__main__":
    roman_num = input()
    print(roman_numerals_to_int(roman_num))