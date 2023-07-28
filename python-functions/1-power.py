#!/usr/bin/env python3
def pow(a, b):
    # Handle the special case for b=0 (a^0 = 1)
    if b == 0:
        return 1

    # If b is negative, convert a^b to 1/(a^(-b))
    if b < 0:
        a = 1 / a
        b = -b

    # Initialize the result to 1
    result = 1

    # Perform the power calculation using a loop
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    return result

