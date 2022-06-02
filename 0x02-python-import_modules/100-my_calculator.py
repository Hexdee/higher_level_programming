#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = "+-*/"
    op = argv[2]
    if op in ops:
        a = int(argv[1])
        b = int(argv[3])
        if op == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif op == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif op == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
