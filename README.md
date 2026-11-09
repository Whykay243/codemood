# CodeMood - Python Code Personality Analyzer

CodeMood is a simple Python command-line tool I'm building to analyze Python code and give feedback on coding style.

The idea is to look at how someone writes their code, identify areas that could be improved, and eventually assign a coding personality based on their style.

## What CodeMood Will Do

The goal is to have CodeMood check a few things:

- How well functions and classes are documented.
- Whether lines of code are too long.
- How readable and organized the code is.
- Whether functions are too long or complicated.
- How well functions are named.
- Give an overall score from 0 to 100.
- Assign a coding personality based on the results.
- Suggest ways to improve the code.

I'll be using Python's built-in `ast` module to help analyze the code.

## Tools Used

- Python 3.10+
- Python standard library
- unittest for testing

## How to Run

Clone the repository and navigate to the project folder.

Run CodeMood on a Python file:

```bash
python3 codemood.py sample.py
```

To run the tests:

```bash
python3 -m unittest discover -s tests -v
```

## Current Progress

This is the first version of CodeMood. I've set up the basic project structure, added a sample Python file, and written a simple test to make sure the program runs.

The actual code analysis features are still in development.

I'll continue adding features as the project progresses.