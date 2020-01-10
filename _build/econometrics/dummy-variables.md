---
interact_link: content/econometrics/dummy-variables.ipynb
kernel_name: python3
has_widgets: false
title: 'Dummy Variables'
prev_page:
  url: /econometrics/econometrics.html
  title: 'Econometrics and Data Science'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<table style="width: 100%;">
    <tr style="background-color: transparent;"><td>
        <img src="https://d8a-88.github.io/econ-fa19/assets/images/blue_text.png" width="250px" style="margin-left: 0;" />
    </td><td>
        <p style="text-align: right; font-size: 12pt;"><strong>Economic Models</strong>, Fall 2019<br>
            Dr. Eric Van Dusen</p></td></tr>
</table>



# Lecture 12 - Dummy Variables



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from datascience import *
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
plt.style.use("seaborn-muted")
%matplotlib inline

```
</div>

</div>



**Why do we need dummary variables?**

Two cases:

* variable has non-numeric values, e.g. the `sex`, `education`, `marital_status` variables in `defaults`
* variable has categorical numeric values, e.g. a Likert scale (1 to $n$ are possible values) or the `age` variable

In the first case, the reason is obvious: How can we model a variable that has text as its value?

In the second, the reason is more subtle. Let's build two models on data from a Likert scale with values 1 to 7. The first model will leave the values as-is, and the second will use dummy variables for each possible value of the variable.

In this section, we'll use a completely **deterministic** model, wherein $y$ will be a nonlinear function of $x$, with a bit of randomness introduced in the model constants. Our function for $y$ will be

$$\Large 
f(x) = a e^x + bx + c
$$

with $a,b \sim U(0, 100)$ for each value of $x$.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def f(x):
    a = np.random.uniform(0, 100, len(x))
    b = np.random.uniform(0, 100, len(x))
    c = np.random.uniform(0, 100, len(x))
    return a * np.exp(x) + b * x + c

x = np.random.choice(np.arange(1, 8), 1000)
y = f(x)
x[:5], y[:5]

```
</div>

</div>



Let's build an OLS model based on `x` and `y` _without_ creating dummies for $x$.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
y_hat_1 = sm.OLS(y, sm.add_constant(x)).fit().fittedvalues

```
</div>

</div>



Our RMSE for this model is calculated in the cell below.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def rmse(y, y_hat):
    return np.sqrt(mean_squared_error(y, y_hat))

rmse(y, y_hat_1)

```
</div>

</div>



Now let's create some dummy variables for `x`; we'll store these in `X` (note the switch to capitals, since we are now in the multivariate case).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
X = pd.get_dummies(pd.DataFrame({"x" : x}), columns=["x"]).values
X

```
</div>

</div>



Let's now fit a model and look at our RMSE.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
y_hat_2 = sm.OLS(y, sm.add_constant(X)).fit().fittedvalues
rmse(y, y_hat_2)

```
</div>

</div>



We can see a drop in the RMSE when we use dummy variables for age because age is not a continuous variable, but a categorical one. With numerical categorical variables, values that are larger in magnitude that others cause greater shifts in model weights due only to their magnitude. This also helps to reveal nonlinear patterns between variables and a categorical variables.



## How to Get Dummy Variables for a Table

You may have noticed that the code above uses the library `pandas`, which you will learn about in Data 100. However, if we want to use the `datascience` library, we need to define our own function to create dummy variables. Let's start by thinking about the intuition of creating dummy variables using a one-column table with only two possible values: `H` or `T`, for the flip of a coin.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
flips = Table().with_column("flip", np.random.choice(["H", "T"], 200))
flips

```
</div>

</div>



Thinking about our problem, what's the first thing that we need to know? I propose that we need to know all of the **unique** values of our variable, since we will need to create one new column for each of these. Although we already know our variable has only 2 possible values, "H" and "T", let's practice anyway. The function `np.unique` will give you an array of the unique values of the array passed to it.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
unique_vals = np.unique(flips.column("flip"))
unique_vals

```
</div>

</div>



Now that we know these values, we want to create a column for each value with a 1 if the value for that row equals the column value, and a 0 otherwise. To do this, we'll need to use a function that tells us if some value is equal to another pre-specified value. Luckily, you already know these! The predicate functions you use in `Table.where` will do this for us. So let's now look at how we can use these functions to create the columns we want:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for val in unique_vals:
    dummy_vals = flips.apply(are.equal_to(val), "flip")
    flips = flips.with_column("flip_" + val, dummy_vals)

flips

```
</div>

</div>



Notice that we've created columns with names of the format `flips_{value}`. However, we still have a problem: these columns have boolean values, not integers!

Recall now that we can **typecast** a `bool` to an `int` by calling the `int` function on it. This will map `True` to 1 and `False` to 0. Let's now do this with `Table.apply`. Notice in the cell below that we have added logic to apply this function to _our new columns_ using the format of their name.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for val in unique_vals:
    int_vals = flips.apply(int, "flip_" + val)
    flips = flips.with_column("flip_" + val, int_vals)
    
flips

```
</div>

</div>



Now we're almost there! The last thing we want to do is get rid of the original column, so that it doesn't muck up any analysis we do later on. Let's drop it with `Table.drop`.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
flips = flips.drop("flip")
flips

```
</div>

</div>



Congratulations, you've now created dummy variables for a categorical variable! Notice that our choice to iterate through the unique values means that we can use this same logic for any arbitrarily large number of unique values. The function `get_dummies` defined below encapsulates this logic that we've built, albeit with a simplified encoding step. This function will be provided for you in the project.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def get_dummies(tbl, col, drop=True):
    """Creates dummy variables for a column of a table"""
    values = np.unique(tbl.column(col))
    for val in values:
        encoding = tbl.apply(lambda s: int(s == val), col)
        tbl = tbl.with_column(col + "_" + str(val), encoding)
    if drop:
        tbl = tbl.drop(col)
    return tbl

```
</div>

</div>



To illustrate this function and its flexibility, let's imagine that we were rolling an icosahedron (a 20-sided die).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rolls = Table().with_column("roll", np.random.choice(np.arange(1, 21), 400))
rolls

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
get_dummies(rolls, "roll")

```
</div>

</div>



 

