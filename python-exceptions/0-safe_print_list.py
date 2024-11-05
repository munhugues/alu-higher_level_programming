#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    t = 0
    try:
        for i, n in enumerate(my_list):
            t += 1
            print("{:d}".format(n), end="")
            if i == x:
                break
        print()
        return t

    except ValueError:
        pass
