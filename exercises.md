
--- 
There are two types of exercise in this course:

- autograded
- exploratory *(optional)*

**You are expected to complete all of the autograded exercises**, as these are the only ones that will be checked by the autograder and reviewed by the TA. **Exploratory exercises (or "explorations") are optional**, and responses for these will only be reviewed upon request.

Only update the files listed in the exercises themselves. Changing any other file may affect your autograder feedback.

---

# autograded exercises

For these exercises, add your functions to the *apputil\.py* file. If you like, you're welcome to adjust the *app\.py* file, but it is not required. The autograder will only check the *apputil\.py* file.

A [recursive function](https://www.w3schools.com/python/gloss_python_function_recursion.asp) is one which calls itself.

1. When the function is called, your CPU runs through each line of code until the function needs to be called again.
2. At that point, all variables are saved in memory, and the function runs through each line of code again until the function is called (again, but with a different passed argument), and so on.
3. Eventually, this process will stop at the "bottom of the **stack**", where the function doesn't get a chance to call itself again (likely because of some condition un/met by the latest passed argument).
4. Then, your CPU will work its way back up the stack to the final result. For example, take a look at [this visual example](https://realpython.com/python-recursion/#calculate-factorial) of calculating 4!.

When you write these functions, keep two things in mind:

- You will need a built-in stopping point (i.e., the "bottom"), where your function returns some result before it calls itself.
- **Don't think too hard about this.** Recursion can be perplexing to conceptualize when writing the code. So, <font color="darkblue">when you call the function inside the function, think about it as a magical "hidden" function that has already done what you want it to do.</font>
- [Python Tutor](https://pythontutor.com/) ([editor](https://pythontutor.com/visualize.html#mode=edit)) can be a helpful resource for this exercise!

## exercise 1

We write "`n` factorial" as `n!`. It is the product of all the numbers up to, and including `n`:

`8! = 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 = 40320`

Use recursion to write a function `factorial(n)` that calculates the factorial of a given integer.

*Test your function using Google or any other tool that can calculate factorials.*

## exercise 2

The Fibonacci Series (`fib`) starts with 0 and 1. Each of the following numbers are the sum of the previous two numbers in the series:

`0 1 1 2 3 5 8 13 21 34 ...`

So, `fib(9) = 34`.

Write a recursive function that, given `n`, will return the `n`th number of the Fibonacci Series.

*Again, test your function using Google or any other tool that can calculate the Fibonacci Series.*

## supplemental information

- Check out [pythonfibonacci](https://www.pythonfibonacci.com/) for more solutions!
- If the sequence starts with $\{2,\ 1\}$, it is then the [Lucas Sequence](https://en.wikipedia.org/wiki/Lucas_number)
- This sequence is credited to Leonardo Bonacci (filius Bonacci, 'son of Bonacci'), but can be traced back to early Indian mathematicians (circa 400BC)

---

# exploratory exercises

For these explorations, you'll only need to add to the bottom of the lab notebook. If you like, you can also explore Streamlit by incorporating functions into the *app\.py* file.

*Note: the following explorations are completely optional.*

## instructions

For each of the following, **use visualizations** to address the question. Write a short "takeaway" message for each plot, and share any caveats. Also, for each plot, try to get creative with themes, colors, formatting, titles, etc.

## exploration 1

How did the (apparently known) sales of children slaves change over time? Are these changes consistent across national interests?

## exploration 2

What is going on with the difference between `total_embarked` and `total_disembarked`?

> Hint: A "tidy" DataFrame is one where each row represents a **single and unique** observation (or entity), and each column represents a particular attribute of each observation. So, for example, if we think of a "voyage" as a trip which starts in some place, makes a few stops, and then ends, then any stops should be (somehow) represented in a single row. Alternatively, each stop could be its own row, etc. ... Consider the tidiness of this data.