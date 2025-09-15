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