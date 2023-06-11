#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    Roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = Roman_numerals.get(char)
        if value == 0:
            return 0
        if value < prev_value:
            result -= value
        else:
            result += value
            prev_value = value

    return result
