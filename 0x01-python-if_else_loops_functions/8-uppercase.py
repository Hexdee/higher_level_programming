#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print("{}".format(chr(ord(i) - 32) if i >= "a"
                          and i <= "z" else i), end="")
    print()
