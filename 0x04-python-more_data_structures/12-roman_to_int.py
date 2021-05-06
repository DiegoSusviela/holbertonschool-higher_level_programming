#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        n_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        suma = 0
        encontro = 0
        for i in range(len(roman_string)):
            if encontro:
                encontro = 0
                continue
            for key in n_r:
                if roman_string[i] == key and i != len(roman_string) - 1:
                    if roman_string[i] == 'I' and roman_string[i + 1] == 'V':
                        suma += 4
                        encontro = 1
                    elif roman_string[i] == 'I' and roman_string[i + 1] == 'X':
                        suma += 9
                        encontro = 1
                    elif roman_string[i] == 'X' and roman_string[i + 1] == 'L':
                        suma += 40
                        encontro = 1
                    elif roman_string[i] == 'X' and roman_string[i + 1] == 'C':
                        suma += 90
                        encontro = 1
                    elif roman_string[i] == 'C' and roman_string[i + 1] == 'D':
                        suma += 400
                        encontro = 1
                    elif roman_string[i] == 'C' and roman_string[i + 1] == 'M':
                        suma += 900
                        encontro = 1
                    else:
                        suma += n_r[key]
                elif roman_string[i] == key:
                    suma += n_r[key]
        return suma
    return 0
