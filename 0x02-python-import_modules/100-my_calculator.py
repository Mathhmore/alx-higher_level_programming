#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    op = argv[2]
    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if op == '+':
        result = add(int(argv[1]), int(argv[3]))
    elif op == '-':
        result = sub(int(argv[1]), int(argv[3]))
    elif op == '*':
        result = mul(int(argv[1]), int(argv[3]))
    elif op == '/':
        result = div(int(argv[1]), int(argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], result))
    exit(0)
