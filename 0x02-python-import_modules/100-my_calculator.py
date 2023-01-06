#!/usr/bin/python3
def calc(argc):
    from calculator_1 import add, sub, mul, div
    if argc < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        return 1    
    return 0

if __name__ == "__main__":
    import sys
    print(calc(len(sys.argv)))
