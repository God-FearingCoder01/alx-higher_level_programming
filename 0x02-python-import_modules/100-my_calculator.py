#!/usr/bin/python3
def calc(argc):
    if argc < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == "+":
        print(f"{a} + {b} = {a + b}")
    elif operator == "-":
        print(f"{a} - {b} = {a - b}")
    elif operator == "*":
        print(f"{a} * {b} = {a * b}")
    elif operator == "/":
        print(f"{a} / {b} = {a / b}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        return 1    
    return 0

if __name__ == "__main__":
    import sys
    print(calc(len(sys.argv)))
