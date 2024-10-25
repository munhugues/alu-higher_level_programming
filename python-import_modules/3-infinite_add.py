#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for n in sys.argv[1:]:
        num = int(n)
        result += num
    print(result)
