#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        for i in range(97, 123):
            if letter == chr(i):
                print("{}".format(chr(i - 32)), end="")
                break
            else:
                print(letter, end="")
   print()
