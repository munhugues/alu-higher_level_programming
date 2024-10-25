#!/usr/bin/python3
import sys
args = sys.argv
num = len(args)
if num == 1:
    print(f"{num - 1} arguments:")

elif num == 2:
    print(f"{num - 1} argument:")
    for i, n in enumerate(sys.argv):
        if i == 0:
            continue
        print(f"{i}: {n}")

else:
    print(f"{num - 1} arguments:")
    for i, n in enumerate(sys.argv):
        if i == 0:
            continue
        print(f"{i}: {n}")
