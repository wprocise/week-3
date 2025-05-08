# Week 3: Basic Pandas

This week is meant to give you an introductory experience with manipulating data. In particular, we will focus on the following:

- basic data manipulation
- working with missing data
- aggregating data
- basic plotting
- EDA

## setup

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your repository. Use this to view the lab notebook and work on your weekly coding exercise.
3. Once you're ready, commit and push your final changes to your repository.
4. Submit a URL to your (forked) repository on Canvas ([using Gradescope](https://guides.gradescope.com/hc/en-us/articles/21865616724749-Submitting-a-Code-assignment)).

## exercises

**For the exercises, only update the *apputil.py* file or the *app.py* file.** Updating any other files may affect your autograder feedback.

A [recursive function](https://www.w3schools.com/python/gloss_python_function_recursion.asp) is one which calls itself.

1. When the function is called, your CPU runs through each line of code until the function needs to be called again.
2. At that point, all variables are saved in memory, and the function runs through each line of code again until the function is called (again, but with a different passed argument), and so on.
3. Eventually, this process will stop at the "bottom of the **stack**", where the function doesn't get a chance to call itself again (likely because of some condition un/met by the latest passed argument).
4. Then, your CPU will work its way back up the stack to the final result. For example, take a look at [this visual example](https://realpython.com/python-recursion/#calculate-factorial) of calculating 4!.

When you write these functions, keep two things in mind:
- You will need a built-in stopping point (i.e., the "bottom"), where your function returns some result before it calls itself.
- **Don't think too hard about this.** Recursion can be perplexing to conceptualize when writing the code. So, <font color="darkblue">when you call the function inside the function, think about it as a magical "hidden" function that has already done what you want it to do.</font>
- [Python Tutor](https://pythontutor.com/) ([editor](https://pythontutor.com/visualize.html#mode=edit)) can be a helpful resource for this exercise!

### exercise 1

We write "`n` factorial" as `n!`. It is the product of all the numbers up to, and including `n`:

`8! = 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 = 40320`

In *apputil.py*, use recursion to write a function `factorial(n)` that calculates the factorial of a given integer.

*Test your function using Google or any other tool that can calculate factorials.*

### exercise 2

The Fibonacci Series (`fib`) starts with 0 and 1. Each of the following numbers are the sum of the previous two numbers in the series:

`0 1 1 2 3 5 8 13 21 34 ...`

So, `fib(9) = 34`.

Write a recursive function that, given `n`, will return the `n`th number of the Fibonacci Series.

*Again, test your function using Google or any other tool that can calculate the Fibonacci Series.*

### exercise 3

TBD ...

## Packages Available:

The environment for this week is built with the following environment.yml:

```yml
name: week-3
dependencies:
  - python=3.11
  - pip
  - pip:
    - ipykernel  # for Jupyter Notebook
    - streamlit
    - seaborn
    - pandas
    - numpy
```

*Note: you are welcome to install more pacakges in your codespace, but they will not be used by the autograder.*

# supplemental information

- Check out [pythonfibonacci](https://www.pythonfibonacci.com/) for more solutions!
- If the sequence starts with $\{2,\ 1\}$, it is then the [Lucas Sequence](https://en.wikipedia.org/wiki/Lucas_number)
- This sequence is credited to Leonardo Bonacci (filius Bonacci, 'son of Bonacci'), but can be traced back to early Indian mathematicians (circa 400BC)