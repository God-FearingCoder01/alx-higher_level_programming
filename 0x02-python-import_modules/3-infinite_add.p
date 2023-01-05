#!/usr/bin/python3
def get_argv_sum(argc):
        sum = 0
        for i in range(1, argc):
                sum += int(sys.argv[i])
        return (sum)

if __name__ == "__main__":
        import sys
        print(get_argv_sum(len(sys.argv)))
