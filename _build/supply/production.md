---
interact_link: content/supply/production.ipynb
kernel_name: python3
has_widgets: false
title: 'Production'
prev_page:
  url: /supply/horizontal-sum-supply.html
  title: 'Horizontal Sum Supply'
next_page:
  url: /supply/supply.html
  title: 'Supply and Firm Behavior'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<table style="width: 100%;" id="nb-header">
    <tr style="background-color: transparent;"><td>
        <img src="https://d8a-88.github.io/econ-fa19/assets/images/blue_text.png" width="250px" style="margin-left: 0;" />
    </td><td>
        <p style="text-align: right; font-size: 12pt;"><strong>Economic Models</strong>, Fall 2019<br>
            Dr. Eric Van Dusen</p></td></tr>
</table>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import numpy as np  
import matplotlib.pyplot as plt  
%matplotlib inline
from datascience import *

```
</div>

</div>



## Total Output



Imagine that we have a production function is as follows: $$f(x) = -0.6x^3+20x^2+10x$$
Where $x$ is our production input and $f(x)$ is the units of output. For simplicity, we can think of both in dollar terms. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def graph(formula, x_range, title):  
    x = np.array(x_range)  
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)
    plt.xlabel("Input units")
    plt.ylabel("Output units")
    plt.title(title)
    plt.show()  

def TPP(x):
    return -0.6*x**3+20*x**2+10*x

graph(TPP, range(0, 30), "Total output with respect to inputs")

```
</div>

</div>



Here is something interesting to note: when we feed in too many inputs, production actually decreases! Typically, this does not happen, but for this example we can imagine that perhaps hiring too many laborers will reduce the overall output of our production.



## Average Output



The average production function is the average number of output for each input unit. The formula is as follows:
$$\frac{f(x)}{x} = \frac{-0.6x^3+20x^2+10x}{x} = -0.6x^2+20x+10$$



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def APP(x):
    return -0.6*x**2+20*x+10

graph(APP, range(0, 30), "Average output per unit of input")

```
</div>

</div>



## Marginal Output



The marginal production function is the marginal units of output for each additional unit of input. The formula is as follows:
$$\frac{\delta f(x)}{\delta x} = -1.8x^2+40x+10$$



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def MPP(x):
    return -1.8*x**2+40*x+10

graph(MPP, range(0, 30), "Marginal output per additional unit of input")

```
</div>

</div>



Combining all 3 functions:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fig, axs = plt.subplots(2)
fig.suptitle('Total and Average and Marginal Production')
axs[0].plot(range(0, 30), [TPP(i) for i in range(0, 30)])
axs[0].set_title('TPP')
axs[0].set_ylabel('Unit of Output')
axs[1].plot(range(0, 30), [APP(i) for i in range(0, 30)])
axs[1].plot(range(0, 30), [MPP(i) for i in range(0, 30)])
axs[1].set_title('APP and MPP')
axs[1].set_ylabel('Output per input Y/X')
axs[1].axhline(0)
plt.xlabel("Input units (X)")


fig.set_size_inches(15,15)

```
</div>

</div>



## Think Pair Share
If you were a supplier, how many input units would you use?



### Let's look at is as a data table / data set
Import a dataset that corresponds to this data...



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
TPP=Table().read_table("tableTPP.csv")
TPP.show(20)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fig, axs = plt.subplots(2)
fig.suptitle('Total and Average and Marginal Production')
axs[0].plot(TPP.column("Input (x)"),TPP.column("Output_Y"))
axs[0].set_title('TPP')
axs[0].set_ylabel('Unit of Output')

axs[1].plot(TPP.column("Input (x)"),TPP.column("Average_Product"))
axs[1].plot(TPP.column("Input (x)"),TPP.column("Marginal_Product"))
axs[1].set_title('APP and MPP')
axs[1].set_ylabel('Output per input Y/X')
axs[1].axhline(0)
plt.xlabel("Input units (X)")


fig.set_size_inches(15,15)

```
</div>

</div>



**This is the same graph as it comes from the same function! **

