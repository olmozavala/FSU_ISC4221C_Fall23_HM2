# Advanced Python Assignment

The objective of this homework is to delve deeper into Python concepts along with Pandas, NumPy and Matplotlib topics.

Create a Python file named `answers_module.py` at the root folder of this repo for coding answers (except the last question).

Write a report in a file called `report.md` where you explain your answers and link to the related files.

## 1. Advanced Loops and Recursion (10 pts)

Create a function named **myrec_advanced** that computes $f(x) = 2x - f(x-1) + g(x)$ where $g(x) = x^2$ 
for $x > 0$ and $g(x) = f(x) = 0$ if $x = 0$. It should raise an exception for $ x < 0 $.

## 2. Data Manipulation with Pandas (10 pts)

Create a function named **pandas_info** that takes a CSV file path and returns a dictionary with the number 
of rows, number of columns, and the column names. You can use the attached file `data.csv` as an example.

```python
# Example output
output = {
    'num_rows': X,
    'num_cols': Y,
    'col_names': ['Name1', 'Name2', ...]
}
```

## 3. Advanced NumPy/loops (12 pts)

1. Create a function **normalize_rows** that receives a matrix and returns the matrix with its rows normalized (i.e., $\sqrt{ v_1^2 + v_2^2 +  ... + v_n^2 } = 1$ for each row).

## 4. Advanced Matplotlib (16 pts)

### Problem 1: Plotting Basic Functions (10 pts)

Plot the following three functions on the same plot from $x = -10$ to $x = 10$:

1. $f(x) = x^2$
2. $g(x) = x$
3. $h(x) = \sin(x)$

### Requirements:

1. Use different line styles for each function.
2. Add labels and a legend to distinguish each function.
3. Add grid lines to the plot.
4. Label the x-axis and y-axis appropriately.