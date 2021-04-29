#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    num1 = int(argv[1])
    num2 = int(argv[3])
    operator = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    funcs = [add, sub, mul, div]
    for i, j in enumerate(operator):
        if argv[2] == j:
            print("{} {} {} = {}".format(num1, j, num2, funcs[i](num1, num2)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
