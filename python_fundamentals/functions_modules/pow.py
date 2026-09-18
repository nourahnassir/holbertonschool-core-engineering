#!/usr/bin/env python3
def pow(a, b):
    """Compute a to the power of b without using ** operator."""
    result = 1
    # تكرار عملية الضرب b من المرات
    for _ in range(b):
        result *= a
    return result
