import seaborn as sns
import pandas as pd

# Exercise 1: Write a recursive function that returns the nth number of the Fibonacci Series
'''Define the fibonacci function
fibonacci = fib_recursive'''
def fib_recursive(n):
# Using an if-elif-else statement, find fib_recursive starting with 0 and 1
# If n is 0, return 0; if n is 1, return 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
# Test the function by printing the 5th and 9th number in the Fibonacci Series
print(fib_recursive(5))
print(fib_recursive(9))

# Exercise 2
# Write a single recursive function, to_binary, that converts an integer into its binary representation
# define the function to_binary
def to_binary(w):
    # Base case: if w is 0, return the string '0'; if w is 1, return the string '1'
        if w == 0:
            return '0'
        elif w == 1:
            return '1'
    # Build recursive case: Call the function recursively with the integer divided by 2 and append the remainder of the integer divided by 2
        else:
            return to_binary(w // 2) + str(w % 2)
# Test the function to_binary to return a string of the binary representation of the integer
print(to_binary(2))
