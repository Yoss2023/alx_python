#!/usr/bin/env python3
def fibonacci_sequence(n):
    # Handle the special case for n=0
    if n == 0:
        return []
    # Handle the special case for n=1
    elif n == 1:
        return [0]

    # Initialize the Fibonacci sequence with the first two numbers
    sequence = [0, 1]

    # Generate the remaining Fibonacci numbers up to n
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

