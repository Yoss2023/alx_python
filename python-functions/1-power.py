#!/usr/bin/env python3
def pow(a, b):
    # Initialize the result to 1
    result = 1

    # Handle the special case when b is 0 (a^0 = 1)
    if b == 0:
        return result

    # If b is negative, convert a^b to 1/(a^(-b))
    if b < 0:
        a = 1 / a
        b = -b

    # Perform the power calculation using a loop
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    return result

