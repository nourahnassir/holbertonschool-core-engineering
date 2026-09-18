#!/usr/bin/env python3
def pow(a, b):
    """Compute a to the power of b without using ** operator."""
    if b == 0:
        return 1
    
    is_negative = False
    if b < 0:
        is_negative = True
        b = -b

    result = 1
    for _ in range(b):
        result *= a

    if is_negative:
        return 1 / result
    return result
