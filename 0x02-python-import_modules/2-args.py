#!/usr/bin/python3
def get_number_of_arguments(num):
	num -= 1
	if num == 1:
		str = "argument"
	else:
		str = "arguments"
	if num == 0:
		ch = '.'
	else:
		ch = ':'
	print(f"{num} {str}{ch}")
	for i in range(1, num+1):
		print(f"{i}: {sys.argv[i]}")
	print(f"The number of arguments entered is {num}")

if __name__ == "__main__":
	import sys
	get_number_of_arguments(len(sys.argv))
