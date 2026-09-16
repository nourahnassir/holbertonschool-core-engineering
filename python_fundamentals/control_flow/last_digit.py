#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)

ld = abs(number) % 10
if number < 0:
    ld = -ld

msg = f"Last digit of {number} is {ld} and is"
if ld > 5:
    print(f"{msg} greater than 5")
elif ld == 0:
    print(f"{msg} 0")
else:
    print(f"{msg} less than 6 and not 0")
    