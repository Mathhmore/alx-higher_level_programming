#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    if i % 2 != 0:
        j = chr(i - 32)
    else:
        j = chr(i)
    print(j, end="")
