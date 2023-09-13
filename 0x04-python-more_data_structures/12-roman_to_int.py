#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    previous = 'Z'
    if isinstance(roman_string, str) == False or roman_string == None:
        return (0)
    else:
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for letter in roman_string:
            number = numerals.get(letter)

            if letter == 'V' or letter == 'X':
                if previous == 'I':
                    total = total - numerals.get(previous)
                    number = number - numerals.get(previous)
            elif letter == 'L' or letter == 'C':
                if previous == 'X':
                    total = total - numerals.get(previous)
                    number = number - numerals.get(previous)
            elif letter == 'D' or letter == 'M':
                if previous == 'C':
                    total = total - numerals.get(previous)
                    number = number - numerals.get(previous)

            total += number
            previous = letter

        return (total)
