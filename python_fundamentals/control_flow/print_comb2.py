#!/usr/bin/env python3
for i in range(100):
    print("{:02}".format(i) if i == 99 else "{:02}, ".format(i), end="")
print()
