---
interact_link: content/utility/utility.ipynb
kernel_name: python3
has_widgets: false
title: 'Utility Maximization'
prev_page:
  url: /topic-intros/utility.html
  title: 'Utility Maximization'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
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

This is known as the Cobb Douglas Utility Function. To visualize this function, we'll need a 3D plot. 





![Cobb Douglas Utility Function](cobb-douglas.png)



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







![Indifference Curves](indifference-curves.png)



# Budget Constraints
_For the rest of the page, we will assume that $\alpha = 0.5$, i.e. the utility function is: $u(x_1, x_2) = x_1^{0.5}x_2^{0.5}$._

Now we introduce the concept of money into our model. Consumers face a budget constraint when choosing to maximize their utility. Given an income $M$ and prices $p_1$ for good $x_1$ and $p_2$ for good $x_2$, the consumer can at most spend up to $M$ for both goods:
$$M \geq p_1x_1 + p_2x_2$$

Since goods will always bring non-negative utility, consumers will try to consume as many goods as they can. Hence, we can rewrite the budget constraint as an equality instead (since if they have more income leftover, they will use it to buy more goods).
$$M = p_1x_1 + p_2x_2$$

This means that any bundle of goods $(x_1,x_2)$ that consumers choose to consume will adhere to the equality above. What does this mean on our graph? Let's examine the indifference curve plots, assuming that $M = 32$, and $p_1 =2$ and $p_2 = 4$. 






![Indifference Curves with Budget Constraint](budget-constraint.png)



The budget constraint is like a possibilities curve: moving up or down the constraint means gaining more of one good while sacrificing the other.

Let's take a look at what this budget constraint means. Because of the budget constraint, any bundle of goods $(x_1,x_2)$ that consumers ultimately decide to consume will lie on the budget constraint line. Adhering to this constraint where $M=32, p_1 = 2, p_2 = 4$, we can see that consumers will be able to achieve 2 units of utility, and can also achieve 4 units of utility. But what is the maximum amount of utility that consumers can achieve? 

Notice an interesting property about indifference curves: **the utility level of the indifference curves gets larger as we move up and to the right.**

Hence, the maximizing amount of utility in this budget constraint is the rightmost indifference curve that still touches the budget constraint line. In fact, it'll only 'touch' (and not intersect) the budget constraint and be tangential to it. 





![Indifference Curves with Budget Constraint and Maximized Utility](maximized-utility.png)



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

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>


            <div id="dc1b513c-7a2a-4938-b42c-b56b69f24cf6" class="plotly-graph-div" style="height:500px; width:500px;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("dc1b513c-7a2a-4938-b42c-b56b69f24cf6")) {
                    Plotly.newPlot(
                        'dc1b513c-7a2a-4938-b42c-b56b69f24cf6',
                        [{"contours": {"z": {"highlightcolor": "#42f462", "project": {"z": true}, "show": true, "usecolormap": true}}, "type": "surface", "z": [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.1111111111111112, 1.5713484026367723, 1.9245008972987527, 2.2222222222222223, 2.4845199749997664, 2.721655269759087, 2.939723678960657, 3.1426968052735447, 3.333333333333334], [0.0, 1.5713484026367723, 2.2222222222222223, 2.721655269759087, 3.1426968052735447, 3.5136418446315325, 3.849001794597505, 4.157397096415491, 4.444444444444445, 4.714045207910317], [0.0, 1.9245008972987527, 2.721655269759087, 3.3333333333333335, 3.8490017945975055, 4.303314829119352, 4.714045207910317, 5.091750772173157, 5.443310539518174, 5.773502691896258], [0.0, 2.2222222222222223, 3.1426968052735447, 3.8490017945975055, 4.444444444444445, 4.969039949999533, 5.443310539518174, 5.879447357921314, 6.285393610547089, 6.666666666666668], [0.0, 2.4845199749997664, 3.5136418446315325, 4.303314829119352, 4.969039949999533, 5.555555555555556, 6.085806194501846, 6.573421981221797, 7.027283689263065, 7.4535599249993], [0.0, 2.721655269759087, 3.849001794597505, 4.714045207910317, 5.443310539518174, 6.085806194501846, 6.666666666666666, 7.200822998230956, 7.69800358919501, 8.16496580927726], [0.0, 2.939723678960657, 4.157397096415491, 5.091750772173157, 5.879447357921314, 6.573421981221797, 7.200822998230956, 7.7777777777777795, 8.314794192830982, 8.81917103688197], [0.0, 3.1426968052735447, 4.444444444444445, 5.443310539518174, 6.285393610547089, 7.027283689263065, 7.69800358919501, 8.314794192830982, 8.88888888888889, 9.428090415820634], [0.0, 3.333333333333334, 4.714045207910317, 5.773502691896258, 6.666666666666668, 7.4535599249993, 8.16496580927726, 8.81917103688197, 9.428090415820634, 10.000000000000002]]}, {"colorscale": [[0.0, "rgb(23, 28, 66)"], [0.09090909090909091, "rgb(41, 58, 143)"], [0.18181818181818182, "rgb(11, 102, 189)"], [0.2727272727272727, "rgb(69, 144, 185)"], [0.36363636363636365, "rgb(142, 181, 194)"], [0.45454545454545453, "rgb(210, 216, 219)"], [0.5454545454545454, "rgb(230, 210, 204)"], [0.6363636363636364, "rgb(213, 157, 137)"], [0.7272727272727273, "rgb(196, 101, 72)"], [0.8181818181818182, "rgb(172, 43, 36)"], [0.9090909090909091, "rgb(120, 14, 40)"], [1.0, "rgb(60, 9, 17)"]], "contours": {"z": {"highlightcolor": "#42f462", "project": {"z": true}, "show": true, "usecolormap": false}}, "showscale": false, "type": "surface", "z": [[-320000.0, -297777.7777777778, -275555.55555555556, -253333.3333333333, -231111.1111111111, -208888.8888888889, -186666.66666666666, -164444.44444444444, -142222.22222222222, -120000.0], [-275555.55555555556, -253333.3333333333, -231111.1111111111, -208888.8888888889, -186666.66666666666, -164444.44444444444, -142222.22222222222, -120000.0, -97777.77777777778, -75555.55555555558], [-231111.1111111111, -208888.8888888889, -186666.66666666666, -164444.44444444444, -142222.22222222222, -120000.0, -97777.77777777778, -75555.55555555553, -53333.33333333332, -31111.111111111106], [-186666.66666666666, -164444.44444444444, -142222.22222222222, -120000.0, -97777.77777777778, -75555.55555555558, -53333.33333333332, -31111.111111111073, -8888.888888888858, 13333.333333333358], [-142222.22222222222, -120000.0, -97777.77777777778, -75555.55555555553, -53333.33333333332, -31111.111111111106, -8888.888888888858, 13333.333333333358, 35555.55555555557, 57777.77777777779], [-97777.77777777778, -75555.55555555558, -53333.33333333336, -31111.111111111106, -8888.888888888892, 13333.333333333287, 35555.55555555557, 57777.77777777779, 80000.0, 102222.22222222222], [-53333.33333333332, -31111.111111111106, -8888.888888888858, 13333.333333333358, 35555.55555555557, 57777.77777777779, 80000.0, 102222.22222222229, 124444.44444444442, 146666.66666666672], [-8888.888888888858, 13333.333333333358, 35555.55555555557, 57777.77777777779, 80000.0, 102222.22222222229, 124444.4444444445, 146666.66666666672, 168888.88888888893, 191111.11111111115], [35555.55555555557, 57777.77777777779, 80000.0, 102222.22222222222, 124444.44444444442, 146666.66666666672, 168888.88888888893, 191111.11111111115, 213333.33333333334, 235555.55555555556], [80000.0, 102222.22222222222, 124444.44444444442, 146666.66666666666, 168888.88888888885, 191111.11111111115, 213333.33333333334, 235555.55555555556, 257777.77777777778, 280000.0]]}],
                        {"autosize": false, "height": 500, "margin": {"b": 65, "l": 65, "r": 50, "t": 90}, "scene": {"xaxis": {"range": [0, 10], "title": {"text": "X1"}}, "yaxis": {"title": {"text": "X2"}}, "zaxis": {"nticks": 4, "range": [0, 10], "title": {"text": "Utility"}}}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Cobb Douglas Utility Function w/ BC"}, "width": 500},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('dc1b513c-7a2a-4938-b42c-b56b69f24cf6');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>
</div>

</div>
</div>
</div>



![3D Cobb Douglas with Budget Constraint](cobb-douglas-budget-contraint.png)



 

