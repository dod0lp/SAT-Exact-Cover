# SAT-Exact-Cover
Python parser of graph to find out **Exact Cover** problem using solver *Glucose*, and print result in human-readable form.

## Input
You are given an *m* x *n* matrix (a matrix of 1/0 values).
- Matrix Representation
    - **rows** of the matrix correspond to potential *sets*.
    - **columns** correspond to the *elements that need to be covered*.


## Solve
- Select a subset of rows such that:
    - Each column is covered exactly once (i.e., each column must contain exactly one True or 1 in the selected rows).
    - The rows that are selected form an Exact Cover.
 
## Encoding
- **Variables**: Each row *i* is represented by boolean variable *x_i*
    - `True` - selected
    - `False` - not selected
     
- **At least one row covers each column**: For ecah column *j* ew create clause where we list all the rows *i* that are `True` in column *j*.

- **At most one row covers each column**: For eachany two rows *i_1* *i_2* that both cover the same column *j*, we ad a clause to ensure that no two rows can bes elected to cover the same column.