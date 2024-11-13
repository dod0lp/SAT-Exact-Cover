# SAT-Exact-Cover
Python parser of graph to find out **Exact Cover** problem using solver *Glucose*, and print result in human-readable form.

## Input
You are given a *rows* x *cols* matrix (a matrix of `True`/`False` values).
- Matrix Representation
    - **rows** of the matrix correspond to potential *sets*.
        - number of *rows* is number of collection of subsets of set *X*
    - **columns** correspond to the *elements that need to be covered*.
        - Number of elements in a set *X*


## Solve
- Select a subset of rows such that:
    - Each column is covered exactly once (i.e., each column must contain exactly one True or 1 in the selected rows).
    - The rows that are selected form an Exact Cover.
 
## Encoding and calculation
- **Variables**: Each row *row* is represented by boolean variable *x_row*
    - `True` - selected
    - `False` - not selected
     
- **At least one row covers each column**: For each column *col* create clause where we list all the rows *row* that are `True` in column *col*.

- **At most one row covers each column**: For eachany two rows *row_i* *row_j* that both cover the same column *col*, we ad a clause to ensure that no two rows can be selected to cover the same column.

### Result
- Each non-negative variable means, that this *row*/*subset* is selected.