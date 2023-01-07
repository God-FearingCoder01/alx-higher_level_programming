#!/usr/bin/python3
j = 0
i = 0
while i < 100:
    j += 1
    k = j
    while k < 10:
        if i == 8 and k == 9:
            print("{:d}{:d}".format(i, k))
        else:
            print("{:d}{:d}".format(i, k), end=", ")
        k += 1;
    i += 1
