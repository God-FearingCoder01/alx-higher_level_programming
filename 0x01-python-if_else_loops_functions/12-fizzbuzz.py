#!/us/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if is_multiple_of_both(num):
            print("FizzBuzz", end=" ")
        elif is_multiple_of_3(num):
            print("Fizz", end=" ")
        elif is_multiple_of_5(num):
            print("Buzz", end=" ")
        else:
            print(f"{num}", end=" ")


def is_multiple_of_both(n):
    return (n % 5 == 0) and (n % 3 == 0)


def is_multiple_of_3(n):
    return (n % 3 == 0)


def is_multiple_of_5(n):
    return (n % 5 == 0)
