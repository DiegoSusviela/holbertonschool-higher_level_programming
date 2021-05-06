#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerador = 0
        denominador = 0
        for x in my_list:
            numerador += x[0] * x[1]
            denominador += x[1]
        return numerador/denominador
    return 0
