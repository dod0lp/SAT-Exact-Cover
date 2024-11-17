# SAT-Exact-Cover
Python parser of graph to find out [Exact Cover](https://en.wikipedia.org/wiki/Exact_cover) problem using solver *Glucose*, with function to print result in human-readable form.

## Solve
- Select a subset of rows such that:
    - Each column is covered exactly once (i.e., each column must contain exactly one True (or 1) in the selected rows).
    - The rows that are selected form an *Exact Cover*.

## Input
- **In general**
    - You are given a *rows* x *cols* matrix (a matrix of `True`/`False` values).
    - **Matrix Representation**
        - **rows** of the matrix correspond to potential *sets*.
            - number of *rows* is number of collection of subsets of set *X*
        - **columns** correspond to the *elements that need to be covered*.
            - Number of elements in a set *X*
- **Example on how to run python code**
    1. For more info use `--help` argument

1. `cd python`
2. `./parser.py --name 2 --alias glucose --verbose 1 --cnf_save 1`


- **User input**
    - Examples in folder **data**
    - Examples of how python operates are in python script itself
    - Used by running python from directory it is in, and adding arguments.
        - For help with arguments add argument `--help`
    - In folder *data* you need to provide a new folder with name of your tests, for example *to_solve*,
    and input file named *to_solve.in*, which contains data in form of matrix in following format:
        - *first row*: *number of rows* [whitespace] *number of columns*
        - *following* **number of rows** *rows*: *number of columns* of 0 1 integers
 
## Encoding and calculation
- I will briefly explain how it is encoded here
    - Function `exact_cover_to_sat(matrix)` with comments on what exactly it is doing
- **Variables**: Each row *row* is represented by boolean variable *x_row*, and it represents a subset, element is selected such as
    - `True` - selected
    - `False` - not selected
     
- **At least one row covers each column**
    - For each column *col* create clause where we list all the rows *row* that are `True` in column *col*.

- **At most one row covers each column**
    - For eachany two rows *row_i* *row_j* that both cover the same column *col*, we ad a clause
    to ensure that no two rows can be selected to cover the same column.

### Result
- Each non-negative variable means, that this *row*/*subset* is selected.
- There is user-friendly interpretor that prints results and shows valid subsets that were selected.
    -  Or says that it is not satisfiable.
      
- *K řešení přiložte několik instancí*
    - in folder **data** with results of solver
        - *sat_human_readable*
        - *unsat_human_readable*
        - *sat_long* containing only resulting glucose file, because setup for this and file is really big,
            but script in main hidden behind *sat_VERY_long_running* bool flag contains a way to make it.
        - *n-queens* is instance of famous problem of queens, result should be SAT with all variables/row/subsets selected - each queen is on its own row and column
        - *1* & *2* are another simple human readable instances
        - *user_test* is default that I was using while testing parser, currently containing matrix from [example](https://en.wikipedia.org/wiki/Exact_cover#Detailed_example) linked at the introduction.

- Instances can be big up to 750x750 randomly-generated *subsets x items* and then it starts to get really really slow because of generation of formulas etc. 1250x1250 that is in examples that ran around 10seconds in *Glucose* was setting up using my script around 30minutes.
    - I tried many of them with different size parameters at first with multiples of 10, then moved to 100.
- Also I was doing some more simple self-made instances, but they were really simple and solved really really fast, it was bit bigger than those 1, 2 examples, but still really simple for a computer.