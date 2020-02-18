---
interact_link: content/demand/demand.ipynb
kernel_name: python3
has_widgets: false
title: 'The Demand Curve'
prev_page:
  url: /topic-intros/demand.html
  title: 'Demand and Consumer Surplus'
next_page:
  url: /topic-intros/supply.html
  title: 'Supply and Elasticity'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Demand





## Introduction



In this chapter, we will explore one of the most foundational concepts in economics: demand curves. Supply and demand makes up markets, and understanding how demand works is important for future concepts. 

The demand curve shows the graphical relationship between the price of a good or service and the quantity demanded for it over a given period of time. In other words, it shows the quantity of goods or services consumers are willing to buy at each market price. The quantity of goods or services demanded or supplied is a function of price, as in   $$\text{Quantity} = f(\text{Price})$$

The curve decreases because of the law of demand, which states that as the price of a good or service increases, the quantity demanded for it decreases, assuming all other factors are held constant. This makes intuitive sense: as prices increase, fewer people are willing to pay the higher price for the same good. Naturally, as prices decrease, more people are willing to pay the lower price for the same good. Hence, the demand of a good or service is based on the price. This relationship is usually somewhat linear and can be found as $$\text{Quantity}_{d}=a * \text{Price}_{d} + b$$

This can be interpreted as: As the price unit increases by 1, there is an a unit increase/decrease in the quantity demanded. An example is $$\text{Quantity}_{d}=2 * \text{Price}_{d} + 3$$

Another concept is when price is dependent on quantity. In this case, we use an inverse demand function, as it is an inverse function of the demand function. Thus, price is a function of quantity, as shown by $$\text{Price} = f(\text{Quantity})$$ Because it is the inverse of a demand function, the inverse demand function for the example above will be $$\text{Price}_{d}=1/2*\text{Quantity}_{d}-3/2$$



### Shifts in Demand Curve



The demand curve can shift out or in based on events happening in the real world. Some factors other than a change in price of the good/service are changes in 

*  buyer's income
*  consumer preferences
*  expectation of future price/supply/demand/etc.
* price of related goods

If any of these changes occur and causes the demand for the selected good/service to decrease, then the curve shifts to the left, as less of the good or service will be demanded at every price. During the 2008 recession, consumers' incomes decreased. Because their buying power decreased, they purchased fewer items even though the prices of the select goods stayed the same. 



## Fruits Data



We will now explore the relationship between price and quantity of oranges produced between 1924 and 1938. In this chapter, we will focus on oranges. It is important to remember that this data is from the 1920's and 1930's, so the prices are much lower than what they would be today because of inflation, competition, innovations, etc. For example, in 1924, 41,880 tons of oranges would have costed 6.63 dollars as of 1924-dollars. That same amount in 2019 is 100.78 dollars. 


The source of this dataset is S. Hoos (1941). "An Investigation on Complementarity Relations Between
Fresh Fruits," Journal of Farm Economics, Vol. 23, #2, pp. 421-433.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fruitprice = Table.read_table('fruitprice.csv')
fruitprice

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year</th> <th>Pear Price</th> <th>Pear Unloads (Tons)</th> <th>Plum Price</th> <th>Plum Unloads</th> <th>Peach Price</th> <th>Peach Unloads</th> <th>Orange Price</th> <th>Orange Unloads</th> <th>NY Factory Wages</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1924</td> <td>8.04      </td> <td>18489              </td> <td>8.86      </td> <td>6582        </td> <td>4.96       </td> <td>41880        </td> <td>6.63        </td> <td>21258         </td> <td>27.22           </td>
        </tr>
        <tr>
            <td>1925</td> <td>5.67      </td> <td>21919              </td> <td>7.27      </td> <td>5526        </td> <td>4.87       </td> <td>38772        </td> <td>9.19        </td> <td>15426         </td> <td>28.03           </td>
        </tr>
        <tr>
            <td>1926</td> <td>5.44      </td> <td>29328              </td> <td>6.68      </td> <td>5742        </td> <td>3.35       </td> <td>46516        </td> <td>7.2         </td> <td>24762         </td> <td>28.89           </td>
        </tr>
        <tr>
            <td>1927</td> <td>7.15      </td> <td>17082              </td> <td>8.09      </td> <td>5758        </td> <td>5.7        </td> <td>32500        </td> <td>8.63        </td> <td>22766         </td> <td>29.14           </td>
        </tr>
        <tr>
            <td>1928</td> <td>5.81      </td> <td>20708              </td> <td>7.41      </td> <td>6000        </td> <td>4.13       </td> <td>46820        </td> <td>10.71       </td> <td>18766         </td> <td>29.34           </td>
        </tr>
        <tr>
            <td>1929</td> <td>7.6       </td> <td>13071              </td> <td>10.86     </td> <td>3504        </td> <td>6.7        </td> <td>36990        </td> <td>6.36        </td> <td>35702         </td> <td>29.97           </td>
        </tr>
        <tr>
            <td>1930</td> <td>5.06      </td> <td>22068              </td> <td>6.23      </td> <td>7998        </td> <td>6.35       </td> <td>29680        </td> <td>10.5        </td> <td>23718         </td> <td>28.68           </td>
        </tr>
        <tr>
            <td>1931</td> <td>5.4       </td> <td>19255              </td> <td>6.86      </td> <td>5638        </td> <td>3.91       </td> <td>50940        </td> <td>5.81        </td> <td>39263         </td> <td>26.35           </td>
        </tr>
        <tr>
            <td>1932</td> <td>4.06      </td> <td>17293              </td> <td>6.09      </td> <td>7364        </td> <td>4.57       </td> <td>27642        </td> <td>4.71        </td> <td>38553         </td> <td>21.98           </td>
        </tr>
        <tr>
            <td>1933</td> <td>4.78      </td> <td>11063              </td> <td>5.86      </td> <td>8136        </td> <td>3.57       </td> <td>35560        </td> <td>4.6         </td> <td>36540         </td> <td>22.26           </td>
        </tr>
    </tbody>
</table>
<p>... (5 rows omitted)</p>
</div>


</div>
</div>
</div>



Because we are only examining the relationship between prices and quantity for oranges, we can create a new table with the relevant columns: Year, Orange Price, and Orange Unloads. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
oranges = fruitprice.select(["Year", "Orange Price", "Orange Unloads"])
oranges

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year</th> <th>Orange Price</th> <th>Orange Unloads</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1924</td> <td>6.63        </td> <td>21258         </td>
        </tr>
        <tr>
            <td>1925</td> <td>9.19        </td> <td>15426         </td>
        </tr>
        <tr>
            <td>1926</td> <td>7.2         </td> <td>24762         </td>
        </tr>
        <tr>
            <td>1927</td> <td>8.63        </td> <td>22766         </td>
        </tr>
        <tr>
            <td>1928</td> <td>10.71       </td> <td>18766         </td>
        </tr>
        <tr>
            <td>1929</td> <td>6.36        </td> <td>35702         </td>
        </tr>
        <tr>
            <td>1930</td> <td>10.5        </td> <td>23718         </td>
        </tr>
        <tr>
            <td>1931</td> <td>5.81        </td> <td>39263         </td>
        </tr>
        <tr>
            <td>1932</td> <td>4.71        </td> <td>38553         </td>
        </tr>
        <tr>
            <td>1933</td> <td>4.6         </td> <td>36540         </td>
        </tr>
    </tbody>
</table>
<p>... (5 rows omitted)</p>
</div>


</div>
</div>
</div>



We can also rename columns. In this case, let's rename "Orange Unloads" to "Orange Quantity" for simplicity and comprehensibility. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
orangesRenamed = oranges.relabeled(["Orange Unloads", "Orange Price"], ["Quantity", "Price"])
orangesRenamed

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year</th> <th>Price</th> <th>Quantity</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1924</td> <td>6.63 </td> <td>21258   </td>
        </tr>
        <tr>
            <td>1925</td> <td>9.19 </td> <td>15426   </td>
        </tr>
        <tr>
            <td>1926</td> <td>7.2  </td> <td>24762   </td>
        </tr>
        <tr>
            <td>1927</td> <td>8.63 </td> <td>22766   </td>
        </tr>
        <tr>
            <td>1928</td> <td>10.71</td> <td>18766   </td>
        </tr>
        <tr>
            <td>1929</td> <td>6.36 </td> <td>35702   </td>
        </tr>
        <tr>
            <td>1930</td> <td>10.5 </td> <td>23718   </td>
        </tr>
        <tr>
            <td>1931</td> <td>5.81 </td> <td>39263   </td>
        </tr>
        <tr>
            <td>1932</td> <td>4.71 </td> <td>38553   </td>
        </tr>
        <tr>
            <td>1933</td> <td>4.6  </td> <td>36540   </td>
        </tr>
    </tbody>
</table>
<p>... (5 rows omitted)</p>
</div>


</div>
</div>
</div>



To construct the demand curve, let's first see what the relationship between price and quantity is. We want a downward-sloping line between price and quantity, because the demand curve is a downward-sloping curve that shows that if a product's prices increase, consumers will purchase less, and if a product's prices decrease, then consumers will purchase more. 

To find this, we will create a scatterplot and draw a regression line (`fit_line = True`) between the points. Regression lines are helpful because they consolidate all the datapoints into a single line, helping us better understand the relationship between the two variables. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
orangesRenamed.scatter("Quantity", "Price", fit_line = True)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/demand/demand_14_0.png)

</div>
</div>
</div>



We can see that there is a negative relationship between the two variables. Perfect! It is important to note that scatterplots only show positive, negative, or neutral correlations among two variables. If two variables have a positive correlation, then as one variable increases, the other increases too. If two variables have a negative correlation, then as one variable increass, the other decreases. If two variables have a neutral correlation, then if one varible increases, the other variable stays constant. Scatterplots do not show or prove causation between two variables-- it is up to the data scientists to prove any causation. 

We will now quantify our demand curve using NumPy's polyfit function. `np.polyfit` returns an array of size 2, where the 0th index is the slope and 1st index is the $y$-intercept.

The general template for the demand curve is $y = mx + b$, where $m$ is the slope and $b$ is $y$-intercept. In economic terms, $m$ is the demand curve's slope that shows how the good's price affects the quantity demanded, and $b$ encompasses the effects of all of the factors that are not price that affect demand. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
np.polyfit(orangesRenamed.column("Quantity"),orangesRenamed.column("Price"),1)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
array([-2.14089690e-04,  1.33040264e+01])
```


</div>
</div>
</div>



This shows that the demand curve is $y = -0.000214x+ 13.3$. The slope is -0.000214 and $y$-intercept is 13.3. That means that as quantity increases by 1 unit (in this case, 1 ton), price decreases by 0.000214 units (in this case, \\$0.000214). 

We will now use SymPy to write out this demand curve. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Q = sympy.Symbol("Q")
demand = -0.000214 * Q + 13.3
demand

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
-0.000214*Q + 13.3
```


</div>
</div>
</div>



Let's now assume that the supply curve is given by $y = 0.00023x + 0.8$. The supply curve is not based on data. Supply curves show how much of a good suppliers are willing and able to supply at different prices.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
supply = 0.00023 * Q + 0.8
supply

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.00023*Q + 0.8
```


</div>
</div>
</div>



Quantity equilibrium is the quantity at which the supply curve and demand curve intersect. The quantity of the good that consumers desire to purchase is equivalent to the quantity of the good that producers supply. There is no shortage or surplus of the product at this quantity. 

Let's find the quantity equilibrium for this exercise.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
solve = lambda x,y: sympy.solve(x-y)[0] if len(sympy.solve(x-y))==1 else "Not Single Solution"

Q_star = solve(demand, supply)
Q_star

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
28153.1531531532
```


</div>
</div>
</div>



This means that the number of tons of oranges that consumers want to purchase and producers want to provide are about 28,153 tons of oranges. 



Price equilibrium is the price at which the supply curve and demand curve intersect. The price of the good that consumers desire to purchase at is equivalent to the price of the good that producers want to sell at. There is no shortage of surplus of the product at this price.

Let's find the price equilibrium. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
demand.subs(Q, Q_star)
supply.subs(Q, Q_star)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
7.27522522522523
```


</div>
</div>
</div>



This means that the price of oranges in tons that consumers want to purchase at and producers want to provide is about \\$7.27. 

Now that we have our demand and supply curves and price and quantity equilibriums, we can visualize them on a graph to see what they look like. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def plot_equation(equation, price_start, price_end, label=None):
    plot_prices = [price_start, price_end]
    plot_quantities = [equation.subs(list(equation.free_symbols)[0], c) for c in plot_prices]
    plt.plot(plot_prices, plot_quantities, label=label)
    
def plot_intercept(eq1, eq2):
    ex = sympy.solve(eq1-eq2)[0]
    why = eq1.subs(list(eq1.free_symbols)[0], ex)
    plt.scatter([ex], [why])
    return (ex, why)
    
plot_equation(demand, 5000, 50000, label = "Demand")
plot_equation(supply, 5000, 50000, label = "Supply")
plt.ylim(0,13)
plt.title("Orange Supply and Demand in 1920's and 1930's")
plt.xlabel("Quantity (Tons)")
plt.ylabel("Price")
plot_intercept(supply, demand)
plt.legend(loc = "upper right")
plt.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/demand/demand_27_0.png)

</div>
</div>
</div>



You can also practice on your own and download additional data sets here: http://users.stat.ufl.edu/~winner/datasets.html, courtesy of the University of Flordia's Statistics Department. 

