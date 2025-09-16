import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Exercise 1: Write a recursive function that returns the nth number of the Fibonacci Series
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

## Exercise 2
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
# Test case: to_binary(10)
print(to_binary(10))

## Exercise 3: Write a function for the following tasks and name them task_i()

# Read the dataset from the URL into a DataFrame
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(df_bellevue.head())
# Display the summary statistics of the DataFrame
print(df_bellevue.describe(include='all'))
# Display the data types of each column in the DataFrame
print(df_bellevue.dtypes)
# Check for missing values in the DataFrame
print(df_bellevue.isnull().sum())

# Task 1: Return a list of all column names, sorted such that the first column has the least missing values, and the last column has the most missing values (use the raw column names)
# Define the function task_i
def task_i():
    # Calculate the number of missing values for each column
    # Convert missing values to null values
    missing_values = df_bellevue.isnull().sum()
    # Sort the columns based on the number of missing values in ascending order
    sorted_columns = missing_values.sort_values().index.tolist()
    return sorted_columns
# Test the function task_i
print(task_i())

# Task 2: Return a data frame with two columns: 'year' and 'total_admissions', where 'year' is the year of admission and 'total_admissions' is the total number of admissions for that year
# Define the function task_ii
def task_ii():
    # Extract the year from the 'admission_date' column and create a new 'year' column
    df_bellevue['year'] = pd.to_datetime(df_bellevue['date_in']).dt.year
    # Group the DataFrame by 'year' and count the number of admissions for each year
    admissions_per_year = df_bellevue.groupby('year').size().reset_index(name='total_admissions')
    return admissions_per_year
# Test the function task_ii
print(task_ii())

# Task 3: Return a series with Index: gender (M or F) and Values: average age for the indexed gender
# Define the function task_iii
def task_iii():
    # Create the series with index
    df = pd.DataFrame(df_bellevue)
    # Group the DataFrame by 'gender' and calculate the mean age for males and females using groupby.mean()
    avg_age = df_bellevue.groupby('gender')['age'].mean()
    return avg_age
# Test the function task_iii
print(task_iii())





