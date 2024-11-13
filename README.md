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