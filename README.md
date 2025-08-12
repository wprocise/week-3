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