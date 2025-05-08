# week-template

> This is a **TEMPLATE** repository for a weekly content including the lab and coding exercises.

This week's lab is meant to give you a very basic introduction to the Python coding environment. In particular, we will focus on the following:

- JupyterLab and Markdown
- Variables and Data Types
- Operators and Logic
- Packages, Modules, and Objects

## setup

*(As of April 2025)*

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your repository. Use this to view the lab notebook and work on your weekly coding exercise.
3. Once you're ready, commit and push your final changes to your repository.
4. Submit a URL to your (forked) repository on Canvas ([using Gradescope](https://guides.gradescope.com/hc/en-us/articles/21865616724749-Submitting-a-Code-assignment)).

## exercises

**For the exercises, only update the *apputil.py* file or the *app.py* file.** Updating any other files may affect your autograder feedback.

### exercise 1

In *apputil.py*, ...

---

**A few test cases:**

...

### exercise 2

...

---

**A few test cases:**

...

## Packages Available:

The environment for this week is built with the following environment.yml:

```yml
name: coding-exercise
dependencies:
  - python=3.11
  - pip
  - pip:
    - streamlit
    - pandas
    - numpy
```

*Note: you are welcome to install more pacakges in your codespace, but they will not be used by the autograder.*

---

**<font color='darkred'>DELETE THIS SECTION BEFORE SHARING WITH STUDENTS</font>**

## for instructors

### setup and testing on autograder

1. First, make sure you adjust the [autograder settings](https://gradescope-autograders.readthedocs.io/en/latest/autograder_settings.png) accordingly.
2. **Copy** this repository as a template for each coding exercise.
3. Uncomment the `autograder` line in the *.gitignore* file.
4. Update the tests and the app or apputil file accordingly. Create a new github repository for the exercise, and update the Dockerfiles as needed.

### other notes

- If you're running on a recent MacBook, you'll need to use [multi-platform building](https://docs.docker.com/build/building/multi-platform/#simple-multi-platform-build-using-emulation). For this, reference the command commented at the top of the *Dockerfile*.
- This repository (aside from the *autograder* directory) represents an example of a students's submission.
- The contents of the *autograder/tests* folder and the *results.json* file are only examples, and should be tailored to the exercise at hand.
  - Everything else in the *autograder* directory is meant to be generic for all exercises.
- See the [gradescope Python example](https://github.com/gradescope/autograder_samples/tree/master/python) for more on how this repo is organized.
- Use this as a *template* for actual exercises. Before sharing the template with students, delete the *autograder* directory, and uncomment the `autograder` line in the *.gitignore* file in actual exercises. This will hide the solutions for students.
- See [here](https://www.docker.com/blog/docker-best-practices-understanding-the-differences-between-add-and-copy-instructions-in-dockerfiles/) for the difference between `ADD` and `COPY` in Docker, explaining why the latter was used here.
- Note that you cannot `COPY` from a parent directory, so we need to add the environment update to the *run_autograder* file.
