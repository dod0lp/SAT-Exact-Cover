# SAT-Exact-Cover
Python parser of graph to find out **Exact Cover** problem using solver *Glucose*, with function to print result in human-readable form.

## Input
- **In general**
    - You are given a *rows* x *cols* matrix (a matrix of `True`/`False` values).
    - **Matrix Representation**
        - **rows** of the matrix correspond to potential *sets*.
            - number of *rows* is number of collection of subsets of set *X*
        - **columns** correspond to the *elements that need to be covered*.
            - Number of elements in a set *X*

- **User input**
    - Examples are in python script if you run it as **main**
    - Or in folder **data**
    - Used by running python from directory it is in, and adding arguments.
        For help with arguments add argument **--help**
    - In folder *data* you need to provide a new folder with name of your tests, for example *to_solve*,
    and input file named *to_solve.in*, which contains data in form of matrix in following format:
        - *first row*: *number of rows* [whitespace] *number of columns*
        - *following* **number of rows** *rows*: *number of columns* of 0 1 integers

## Solve
- Select a subset of rows such that:
    - Each column is covered exactly once (i.e., each column must contain exactly one True or 1 in the selected rows).
    - The rows that are selected form an *Exact Cover*.
 
## Encoding and calculation
- **Variables**: Each row *row* is represented by boolean variable *x_row*
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