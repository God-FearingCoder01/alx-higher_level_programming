#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    argc -= 1
    if argc == 1:
        strng = "argument"
    else:
        strng = "arguments"
    if argc == 0:
        ch = "."
    else:
        ch = ":"
    print("{:d} {}{}".format(argc, strng, ch))
    for i in range(1, argc+1):
        print("{:d}: {}".format(i, argv[i]))
