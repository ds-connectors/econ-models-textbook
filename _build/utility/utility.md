---
interact_link: content/utility/utility.ipynb
kernel_name: python3
has_widgets: false
title: 'Utility Maximization'
prev_page:
  url: /topic-intros/utility.html
  title: 'Utility Maximization'
next_page:
  url: /topic-intros/elasticities.html
  title: 'Welfare and Elasticities'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<table style="width: 100%;">
    <tr style="background-color: transparent;"><td>
        <img src="https://d8a-88.github.io/econ-fa19/assets/images/blue_text.png" width="250px" style="margin-left: 0;" />
    </td><td>
        <p style="text-align: right; font-size: 12pt;"><strong>Economic Models</strong>, Fall 2019<br>
            Dr. Eric Van Dusen</p></td></tr>
</table>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import pandas as pd
import numpy as np
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display
import warnings
warnings.filterwarnings('ignore')
init_notebook_mode()

```
</div>

</div>



# Utility

### What is Utility?

When we consume a good, we assume that the good will have some impact on our total utility. Utility is a fundamental measure that helps economists model how consumers make decisions. An assumed rule in economics is that consumers will always act rationally, which translates to the assumption that consumers will always attempt to maximize their own utility. 

It is important to note that utility doesn't have specified units and even the face value of utility doesn't have any meaning. *What does an apple providing 5 utility units even mean?* What is valuable, however, is that utility can be compared: if an apple provides 5 utility units and an orange provides 3 utility units, then we prefer apples to oranges.

As a very simple example, say Anne has 6 dollars and she can choose to buy any combination of goods A and B. If good A costs 2 dollars and provides 5 utility units per unit of A consumed, while good B costs 3 dollars and provides 6 utility units per unit of B consumed, then Anne will buy 3 units of good A, since that maximizes her utility. 

In economics, however, our models are a little more complex than that. Typically, utility is the product of the consumption of many goods; typically having a lot of one good but not another does not provide much utility. In addition, consumption of one good faces diminishing marginal returns, i.e. holding all things equal, the consumption of one additional unit of a good will provide less utility than the utility received from the previous unit. Intuitively, imagine Bob is very hungry and decides to eat slices of pizza. The first slice of pizza will bring Bob the most utility, but the 8th slice will be much less satisfying to eat.

### Utility Functions
A consumer's utility is determined by the amount of consumption from all the goods they consume. Typically, utility functions are multivariate: they take in multiple inputs (which represent the different amounts of consumption for each good, which we call a consumption bundle), and output 1 value, the utility. Today, we'll only look at the case where consumers can only choose between 2 goods $x_1$ and $x_2$. Hence, a utility function can be represented by: $u(x_1,x_2)$. 

With that in mind, let's start graphing some utility functions!





## Cobb Douglas Utility Function
Consider the following utility function across $x_1$ and $x_2$:
$$u(x_1, x_2)=x_1^{\alpha}x_2^{1-\alpha}\quad\textrm{where $0<\alpha<1$}$$

This is known as the Cobb Douglas Utility Function. To visualize this function, we'll need a 3D plot; feel free to adjust the slider to change the value of $\alpha$. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def adjust_cd(alpha):
    def cobb_douglas(x1, x2):
        return (x1 ** alpha) * (x2 ** (1-alpha))
    x1 = np.linspace(0,10,10)
    x2 = np.linspace(0,10,10)
    X1,X2 = np.meshgrid(x1,x2)
    z = cobb_douglas(X1,X2)
    data = [go.Surface(z=z, contours=go.surface.Contours(z=go.surface.contours.Z(show=True,usecolormap=True,highlightcolor="#42f462",project=dict(z=True))))]
    layout = go.Layout(title='Cobb Douglas Utility Function',autosize=False,width=500,height=500,margin=dict(l=65,r=50,b=65,t=90),
    scene = dict(xaxis = dict(title='X1'),yaxis = dict(title='X2'),zaxis = dict(title='Utility'),))
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)

alpha_slider = widgets.FloatSlider(min=0, max=1, step=0.1,value=0.5)
display(widgets.interactive(adjust_cd, alpha=alpha_slider))



```
</div>

</div>



### Examining the Utility Function

There are 2 rules that utility functions generally follow: 
- Non-negative marginal utility: the consumption of a good will not decrease the utility. Economists generally assume that 'more is better'. If the consumption of a good decreased utility, then we would consume less of a good. 
- Diminishing marginal returns: all else equal, as consumption increases the marginal utility derived from each additional unit declines.

#### Non-negative Marginal Utility
Say we are currently consuming 2 units of $x_1$ and $x_2$ each with $\alpha = \frac{1}{2}$, providing $u(2,2)=2^{0.5}2^{0.5}=2$ utility units. One additional unit of $x_1$ will provide me a higher point of utility: we can verify this result both graphically and numerically: $u(3,2)=3^{0.5}2^{0.5}\approx2.45$. Indeed, consuming one more unit of a good should increase our utility!

#### Marginal Utility and the Law of Diminishing Returns
Now let's check for the second result: diminishing marginal returns. From above, we know that holding the consumption of $x_2$ constant at 2, going from 2 to 3 units of $x_1$ increases our utility by $2.45-2=0.45$. Going from 3 to 4 units of $x_1$ brings our utility to $u(4,2)=4^{0.5}2^{0.5}\approx 2.83$, an increase of $2.83-2.45=0.38$ utility units.

Using calculus, we can more formally define the marginal utility of a good. Since marginal utility is the change in utility that one additional unit of consumption provides (holding all others constant), the marginal utility with respect to $x_1$ is its partial derivative: $\frac{\partial u}{\partial x_1}$. In our case:
$$\textrm{Marginal Utility of $x_1$:}\quad\frac{\partial u}{\partial x_1} = \frac{1}{2}x_1^{-0.5}x_2^{0.5}$$
$$\textrm{Marginal Utility of $x_2$:}\quad\frac{\partial u}{\partial x_2} = \frac{1}{2}x_1^{0.5}x_2^{-0.5}$$

Or more generally, 
$$\textrm{Marginal Utility of $x_1$:}\quad\frac{\partial u}{\partial x_1} = \alpha x_1^{\alpha-1}x_2^{1-\alpha}$$
$$\textrm{Marginal Utility of $x_2$:}\quad\frac{\partial u}{\partial x_2} = (1-\alpha) x_1^{\alpha}x_2^{-\alpha}$$


With marginal utility defined, note that both conditions can be explained using the marginal utility function $\frac{\partial u}{\partial x}$: 
- Non-negative marginal utility: $\frac{\partial u}{\partial x} \geq 0 $
- Diminishing marginal returns: $\frac{\partial^2 u}{\partial x^2} < 0 $



### Indifference Curves
Although the utility function above in 3D is cool, you'll typically find utility graphs to be in 2D with $x_1$ and $x_2$ as the axis (eliminating the utility axis). 

To represent utility levels, we plot a set of indifference curves on the 2D graph. An indifference curve satisfies the property in which **any point on the curve has the exact same amount of utility**, so that consumers are _indifferent_ to any point on the curve. In our 3D plot, any point on the indifference curve has the exact same height, which represents the value of utility. If you're familar with contour plots, you can also think of indifference curves as following the same idea. 

If you look from the bottom up or top down on the 3D plot, you'll be able to see a few indifference curves. Let's visualize this again in 2D:





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def plot_indiff(alpha, utility_level):
    utilities = [2,4,6,8]
    x1_indiff_val = np.linspace(0,50,1000)
    x2_indiff_vals = []
    for u in utilities:
        x2_indiff_vals.append(((u/(x1_indiff_val ** alpha)) ** (1/(1-alpha))))
    traces = []
    colors = ['blue', 'red','green','purple']
    for u,c,x2 in zip(utilities,colors,x2_indiff_vals):
        traces.append(go.Scatter(
        x = x1_indiff_val,
        y = x2,
        name = 'utility = ' + str(u),
        line = dict(color = c,width = 1)))
    
    x2_indiff_val = (utility_level/(x1_indiff_val ** alpha)) ** (1/(1-alpha))
    traces.append(go.Scatter(
        x = x1_indiff_val,
        y = x2_indiff_val,
        name = 'utility = ' + str(utility_level),
        line = dict(color = 'black',width = 2)))

    data = traces

    # Edit the layout
    layout = dict(title = 'Indifference Curves for the Cobb Douglas Utility Function (alpha = ' + str(alpha) + ')',
                  xaxis = dict(title = 'X1', range = [0,10]),
                  yaxis = dict(title = 'X2', range = [0,10]),)

    fig = dict(data=data, layout=layout)
    iplot(fig)

indiff_curve_slider = widgets.IntSlider(min=0, max=10,step=1,value=3)
alpha_slider = widgets.FloatSlider(min=0, max=1,step=0.1,value=0.5)
display(widgets.interactive(plot_indiff, alpha = alpha_slider, utility_level=indiff_curve_slider))

```
</div>

</div>



# Budget Constraints
_For the rest of the notebook, we will assume that $\alpha = 0.5$, i.e. the utility function is: $u(x_1, x_2) = x_1^{0.5}x_2^{0.5}$._

Now we introduce the concept of money into our model. Consumers face a budget constraint when choosing to maximize their utility. Given an income $M$ and prices $p_1$ for good $x_1$ and $p_2$ for good $x_2$, the consumer can at most spend up to $M$ for both goods:
$$M \geq p_1x_1 + p_2x_2$$

Since goods will always bring non-negative utility, consumers will try to consume as many goods as they can. Hence, we can rewrite the budget constraint as an equality instead (since if they have more income leftover, they will use it to buy more goods).
$$M = p_1x_1 + p_2x_2$$

This means that any bundle of goods $(x_1,x_2)$ that consumers choose to consume will adhere to the equality above. What does this mean on our graph? Let's first examine the indifference curve plots, assuming that $M = 32$, and $p_1 =2$ and $p_2 = 4$. You can also play around and adjust the sliders for $M$, $p_1$, and $p_2$.




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Plot default indifference curves
utilities = [2,4,6,8]
x1_indiff_val = np.linspace(0,50,1000)
x2_indiff_vals = []
for u in utilities:
    x2_indiff_vals.append(((u/(x1_indiff_val ** (1/2))) ** (2)))
traces = []
colors = ['blue', 'red','green','purple']
for u,c,x2 in zip(utilities,colors,x2_indiff_vals):
    traces.append(go.Scatter(
    x = x1_indiff_val,
    y = x2,
    name = 'utility = ' + str(u),
    line = dict(color = c,width = 1)))
    
def plot_bc(M, p_1, p_2):
    for i in range(len(traces) - 4):
        del traces[-1] # This is a hacky method to not continually append to TRACES upon an update from the slider.
    x2_bc_val = (M - (p_1*x1_indiff_val))/p_2
    traces.append(go.Scatter(
        x = x1_indiff_val,
        y = x2_bc_val,
        name = 'Budget Constraint',
        line = dict(color = 'black',width = 1,dash="dot")))
    data = traces
    layout = dict(title = 'Budget Constraint and Indifference Curves for the Cobb Douglas Utility Function (alpha = 0.5)',
                  xaxis = dict(title = 'X1', range = [0,20]),
                  yaxis = dict(title = 'X2', range = [0,15]),)
    fig = dict(data=data, layout=layout)
    iplot(fig)
budget_slider = widgets.IntSlider(min=0, max=50,step=1,value=32)
p1_slider = widgets.IntSlider(min=1, max=10,step=1,value=2)
p2_slider = widgets.IntSlider(min=1, max=10,step=1,value=4)
display(widgets.interactive(plot_bc, M=budget_slider, p_1=p1_slider, p_2=p2_slider))


```
</div>

</div>



The budget constraint is like a possibilities curve: moving up or down the constraint means gaining more of one good while sacrificing the other.

Let's take a look at what this budget constraint means. Because of the budget constraint, any bundle of goods $(x_1,x_2)$ that consumers ultimately decide to consume will lie on the budget constraint line. Adhering to this constraint where $M=32, p_1 = 2, p_2 = 4$, we can see that consumers will be able to achieve 2 units of utility, and can also achieve 4 units of utility. But what is the maximum amount of utility that consumers can achieve? 

Notice an interesting property about indifference curves: **the utility level of the indifference curves gets larger as we move up and to the right.**

Hence, the maximizing amount of utility in this budget constraint is the rightmost indifference curve that still touches the budget constraint line. In fact, it'll only 'touch' (and not intersect) the budget constraint and be tangential to it. You can adjust the budget constraint and see how the maximum utility level (i.e. the indifference curve that is tangent to the budget constraint) changes.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def plot_bc_max_util(M, p_1, p_2):
    # PLOT BC
    for i in range(len(traces) - 4):
        del traces[-1]
    x2_bc_val = (M - (p_1*x1_indiff_val))/p_2
    traces.append(go.Scatter(
        x = x1_indiff_val,
        y = x2_bc_val,
        name = 'Budget Constraint',
        line = dict(color = 'black',width = 1,dash="dot")))
    
    
    # PLOT MAX UTIL INDIFF CURVE
    max_utility = ((1/2*M/p_1) ** (1/2)) * ((1/2*M/p_2) ** (1/2))
    x2_max_util = (max_utility/(x1_indiff_val ** (1/2))) ** 2
    x2_max_util = (max_utility/(x1_indiff_val ** (1/2))) ** 2
    traces.append(go.Scatter(
        x = x1_indiff_val,
        y = x2_max_util,
        name = 'Maximized Utility = ' + str(round(max_utility, 2)),
        line = dict(color = 'black',width = 2)))
    data = traces
    
    layout = dict(title = 'Budget Constraint and Indifference Curves for the Cobb Douglas Utility Function (alpha = 0.5)',
                  xaxis = dict(title = 'X1', range = [0,20]),
                  yaxis = dict(title = 'X2', range = [0,15]),)
    fig = dict(data=data, layout=layout)
    iplot(fig)
    
budget_slider = widgets.IntSlider(min=0, max=50,step=1,value=32)
p1_slider = widgets.IntSlider(min=1, max=10,step=1,value=2)
p2_slider = widgets.IntSlider(min=1, max=10,step=1,value=4)
display(widgets.interactive(plot_bc_max_util, M=budget_slider, p_1=p1_slider, p_2=p2_slider))

```
</div>

</div>



Notice that as the price of one good increases, the indifference curve that represents the maximum attainable utility shifts towards the left (i.e. the max utility decreases). Intuitively, this makes sense. As the price of one good increases, consumers have to make adjustments to their consumption bundles and buy less of one, or both, goods. Hence, their maximum utility will decrease.

Let's revisualize the budget constraint in 3D where $M=32, p_1=2, p_2=4$. Here, any point along the curve in which the 2 planes intersect represents an amount of utility in which the budget constraint holds true (i.e. where we've spent all our income). The utility maximizing quantity is a point on this intersecting curve at which the utility level is the highest.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def cobb_douglas(x1, x2):
    return (x1 ** (1/2)) * (x2 ** (1/2))
x1 = np.linspace(0,10,10)
x2 = np.linspace(0,10,10)
X1,X2 = np.meshgrid(x1,x2)
z = cobb_douglas(X1,X2)

def budget_constraint(x1, x2):
    return 10000*(2*x1 + 4*x2 - 32) # We multiply this by 10000 to get a very steep plane, which should be similar to the actual BC, a vertical plane.
z2 = budget_constraint(X1, X2)

data = [go.Surface(z=z, contours=go.surface.Contours(z=go.surface.contours.Z(show=True,usecolormap=True,highlightcolor="#42f462",project=dict(z=True)))),
       go.Surface(z=z2, contours=go.surface.Contours(z=go.surface.contours.Z(show=True,usecolormap=False,highlightcolor="#42f462",project=dict(z=True))),showscale=False, colorscale="balance")]
layout = go.Layout(
    title='Cobb Douglas Utility Function w/ BC', autosize=False,width=500, height=500, margin=dict(l=65,r=50,b=65,t=90),
    scene = dict(xaxis = dict(title='X1', range = [0,10]), yaxis = dict(title='X2'),
    zaxis = dict(title = 'Utility', nticks=4, range = [0,10],)))
fig = go.Figure(data=data, layout=layout)
iplot(fig)

```
</div>

</div>



 

