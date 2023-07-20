#!/usr/bin/env python3
def fibonacci_sequence(n):
    fib_nums = [0, 1]
    while len(fib_nums) < n:
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)
    return fib_nums

# Test the function
#n = 10
#fibonacci_numbers = fibonacci_sequence(n)
#print(fibonacci_numbers)
#print(fibonacci_sequence(6))

#In this function, we start with the first two Fibonacci numbers (0 and 1) in the list fib_nums. We then use a while loop to continue generating Fibonacci numbers and appending them to the list until the list contains n elements.

