---
interact_link: content/supply/supply.ipynb
kernel_name: python3
has_widgets: false
title: 'Supply and Firm Behavior'
prev_page:
  url: /topic-intros/supply.html
  title: 'Supply and Elasticity'
next_page:
  url: /supply/elasticity.html
  title: 'Elasticity'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# The Supply Curve



The supply of a commodity refers to the quantity for which producers or sellers are willing produce and offer for sale, at a particular price in some given period of time.



To answer questions like *\"at a given price, what will be the supply of a good in the market?\"*, we need to know the market supply curve. A supply curve is simply a curve (or graph) which shows the quantites of a good that can be produced and the prices they will be sold at.

It is good to discern between individual and market supply. **Individual supply** refers to the supply offered by a single firm or producer, while **market supply** refers to the supply offered by all the firms or producers in a market. It is the horizontal summation of the individual supply curves in the market.

The following table and graph will give an example of a market with two firm: A and B.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
market_supply = Table().with_columns("Price", make_array(2, 3, 4),
                                     "Quantity supplied by A", make_array(20, 30, 40),
                                     "Quantity supplied by B", make_array(30, 40, 50),
                                     "Market Supply", make_array(50, 70, 90))
market_supply

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Price</th> <th>Quantity supplied by A</th> <th>Quantity supplied by B</th> <th>Market Supply</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2    </td> <td>20                    </td> <td>30                    </td> <td>50           </td>
        </tr>
        <tr>
            <td>3    </td> <td>30                    </td> <td>40                    </td> <td>70           </td>
        </tr>
        <tr>
            <td>4    </td> <td>40                    </td> <td>50                    </td> <td>90           </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
plt.plot(market_supply.column(1), market_supply.column(0), marker='o')
plt.plot(market_supply.column(2), market_supply.column(0), marker='o')
plt.plot(market_supply.column(3), market_supply.column(0), marker='o')
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Market Supply')
plt.legend(make_array("Quantity supplied by A","Quantity supplied by B","Market Supply"), bbox_to_anchor=(1.04,1), loc="center left")

plt.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_5_0.png)

</div>
</div>
</div>



Market behavior relating to supply is based on the behavior of the individual firms that comprise it. Now, how does an individual firm make its decision about production?

It does so based on the costs associated with production. If the price of a good is enough to recover the costs, the firm produces. Generally, costs increase with the quantity of production. So, to induce producers to increase the quantity supplied, the prices need to increase to compensate for the increased costs.



## Costs



We will split costs into two categories: **Fixed costs** and **Variable costs**.



Fixed Costs are costs associated with fixed factors (or inputs) of production. For example, land for a factory, capital equipment like machinery, etc. The quantity of these inputs cannot be changed quickly in the short term. A factory owner cannot purchase land quickly enough to ramp up production in a week. A key point to note is that fixed costs are irrespective of the quantity, i.e., they do not change with the quantity produced.



Variable Costs are costs associated with variable factors (or inputs) of production. For example, labor, raw materials, etc. The quantity of these inputs can be changed quickly in the short term to adjust supply. A factory owner can hire more laborers or purchase more raw material to increase output. Variable costs change as the supply changes.



Below is a table with the following costs incurred by the firm:

* **Output:** Units produced and supplied
* **Total Fixed Cost (TFC):** Cost incurred by firm on usage of all fixed factors.
* **Total Variable Cost (TVC):** Cost incurred by firm on usage of all variable factors.
* **Total Cost (TC):** Sum of the total fixed and variable costs.
* **Marginal Cost (MC):** Addition to total cost as one more unit of output is produced. It can be calculated as the difference between Total Cost at the current output level and Total Cost at the previous output level.
* **Average Fixed Cost (AFC):** Cost per unit of fixed factors. It can be calculated as the Total Fixed Cost divided by the corresponding output level. 
* **Average Variable Cost (AVC):** Cost per unit of variable factors. It can be calculated as the Total Variable Cost divided by the corresponding output level. 
* **Average Total Cost (ATC):** Total cost per unit. This is the sum of the Average Fixed Cost and the Average Variable Cost.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
individual_firm_costs = Table.read_table('supply_textbook.csv')
individual_firm_costs.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Output</th> <th>Total Fixed Cost</th> <th>Total Variable Cost</th> <th>Total Cost</th> <th>Average Fixed Cost</th> <th>Average Variable Cost</th> <th>Average Total Cost</th> <th>Marginal Cost</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0     </td> <td>50              </td> <td>0                  </td> <td>50        </td> <td>0                 </td> <td>0                    </td> <td>0                 </td> <td>0            </td>
        </tr>
        <tr>
            <td>1     </td> <td>50              </td> <td>50                 </td> <td>100       </td> <td>50                </td> <td>50                   </td> <td>100               </td> <td>50           </td>
        </tr>
        <tr>
            <td>2     </td> <td>50              </td> <td>78                 </td> <td>128       </td> <td>25                </td> <td>39                   </td> <td>64                </td> <td>28           </td>
        </tr>
        <tr>
            <td>3     </td> <td>50              </td> <td>98                 </td> <td>148       </td> <td>16.6667           </td> <td>32.6667              </td> <td>49.3333           </td> <td>20           </td>
        </tr>
        <tr>
            <td>4     </td> <td>50              </td> <td>112                </td> <td>162       </td> <td>12.5              </td> <td>28                   </td> <td>40.5              </td> <td>14           </td>
        </tr>
        <tr>
            <td>5     </td> <td>50              </td> <td>130                </td> <td>180       </td> <td>10                </td> <td>26                   </td> <td>36                </td> <td>18           </td>
        </tr>
        <tr>
            <td>6     </td> <td>50              </td> <td>150                </td> <td>200       </td> <td>8.33333           </td> <td>25                   </td> <td>33.3333           </td> <td>20           </td>
        </tr>
        <tr>
            <td>7     </td> <td>50              </td> <td>175                </td> <td>225       </td> <td>7.14286           </td> <td>25                   </td> <td>32.1429           </td> <td>25           </td>
        </tr>
        <tr>
            <td>8     </td> <td>50              </td> <td>204                </td> <td>254       </td> <td>6.25              </td> <td>25.5                 </td> <td>31.75             </td> <td>29           </td>
        </tr>
        <tr>
            <td>9     </td> <td>50              </td> <td>242                </td> <td>292       </td> <td>5.55556           </td> <td>26.8889              </td> <td>32.4444           </td> <td>38           </td>
        </tr>
        <tr>
            <td>10    </td> <td>50              </td> <td>300                </td> <td>350       </td> <td>5                 </td> <td>30                   </td> <td>35                </td> <td>58           </td>
        </tr>
        <tr>
            <td>11    </td> <td>50              </td> <td>385                </td> <td>435       </td> <td>4.54545           </td> <td>35                   </td> <td>39.5455           </td> <td>85           </td>
        </tr>
    </tbody>
</table>
</div>

</div>
</div>
</div>



Let's create some visualizations to understand the relationships of the different cost curves.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
plt.plot(individual_firm_costs.column("Output"), individual_firm_costs.column("Total Fixed Cost"), marker='o')
plt.plot(individual_firm_costs.column("Output"), individual_firm_costs.column("Total Variable Cost"), marker='o')
plt.plot(individual_firm_costs.column("Output"), individual_firm_costs.column("Total Cost"), marker='o')
plt.xlabel('Quantity')
plt.ylabel('Cost')
plt.title('TFC, TVC and TC')
plt.legend(make_array("Total Fixed Cost","Total Variable Cost","Total Cost"))

plt.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_14_0.png)

</div>
</div>
</div>



We observe the following properties:

1. The TFC is flat. This is because the fixed cost does not change regardless of quantity produced.
2. The vertical difference between the TVC and TC is the TFC. This is because TC = TVC + TFC.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Fixed Cost")[1:], marker='o')
plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Variable Cost")[1:], marker='o')
plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Total Cost")[1:], marker='o')
plt.xlabel('Quantity')
plt.ylabel('Cost')
plt.title('AFC, AVC and ATC')
plt.legend(make_array("Average Fixed Cost","Average Variable Cost","Average Total Cost"))

plt.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_16_0.png)

</div>
</div>
</div>



Notice the following:

1. The AFC is decreasing throughout. This is because at higher levels of production, the fixed cost is divided amongst more units. This implies that the difference between the ATC and AVC decreases as we increase production, since ATC = AVC + AFC.
2. The AVC and ATC slope down initially and then slope up. This represents decreasing and then increasing marginal cost. Marginal cost initially decreases due to efficiencies in producing at scale, but then increases due to the law of variable proportions. 



Now we introduce the marginal cost curve:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
output = individual_firm_costs.column("Output")[1:]
mc = individual_firm_costs.column("Marginal Cost")[1:]
avc = individual_firm_costs.column("Average Variable Cost")[1:]
atc = individual_firm_costs.column("Average Total Cost")[1:]

sp_mc = csaps.UnivariateCubicSmoothingSpline(output, mc, smooth=0.85)
sp_avc = csaps.UnivariateCubicSmoothingSpline(output, avc, smooth=0.85)
sp_atc = csaps.UnivariateCubicSmoothingSpline(output, atc, smooth=0.85)

output_s = np.linspace(output.min(), output.max(), 150)
mc_s = sp_mc(output_s)
avc_s = sp_avc(output_s)
atc_s = sp_atc(output_s)

plt.plot(output, mc, marker = 'o', color = 'tab:blue')
plt.plot(output_s, mc_s, alpha=0.7, lw = 2, label='_nolegend_', color = 'tab:blue')
plt.plot(output, avc, marker = 'o', color = 'tab:green')
plt.plot(output_s, avc_s, alpha=0.7, lw = 2, label='_nolegend_', color = 'tab:green')
plt.plot(output, atc, marker = 'o', color = 'tab:orange')
plt.plot(output_s, atc_s, alpha=0.7, lw = 2, label='_nolegend_', color = 'tab:orange')
plt.hlines(y=min(avc), xmin = 6, xmax = 8, lw=3, color='r', zorder = 10)
plt.hlines(y=min(atc), xmin = 7.5, xmax = 9.5, lw=3, color='r', zorder = 10)
plt.xlabel('Quantity')
plt.ylabel('Cost')
plt.title('MC, AVC and ATC')
plt.legend(make_array("Marginal Cost","Average Variable Cost","Average Total Cost"))

plt.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_19_0.png)

</div>
</div>
</div>



Notice that the MC curve intersects the ATC and AVC curves at their minima. This is because when MC is below the AVC and ATC, it brings down the average since it costs less to produce an additional unit. But as MC begins to increase and surpasses the ATC and AVC cost curves, it will surpass the intersection, and pulls up the AVC and ATC curves. Therefore, it intersects at the minima.



## Production and Firm Behavior



A company decides to produce if it the price is greater than or equal to its Average Variable Cost.



There are 3 different scenarios: 
   - A firm does not produce at all
   - It produces at a loss minimising quantity
   - It produces at a profit
   
Profits are Total Revenue minus Total Costs, where Total Revenue is Price times Quantity.



For any price that is less than AVC, the firm will not produce at all. This is because for any amount of production, they will lose money. In this case, they shut down and the loss is limited to its fixed costs. In this example, we can see this for prices 24 and below.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
firm_behaviour(24, individual_firm_costs)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
No production
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_25_1.png)

</div>
</div>
</div>



For any price that lies above the AVC curve but below the ATC curve, the firm will produce at a loss-minimising quantity. This is because for some levels of production, they will make revenue that is more than the Total Variable Cost of production but is still less than the Total Cost, which includes the fixed cost. While they still lose money, they have offset some of the losses they would have incurred from the fixed cost. In our example, we see this for prices between 25 and 31. The red patch in the plot shows the loss.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
firm_behaviour(28, individual_firm_costs)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Production at loss minimising quantity
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_27_1.png)

</div>
</div>
</div>



If the price is above the ATC curve, the firm produces at a profit. In this example, it is at prices 32 and above. The green patch shows the profit.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
firm_behaviour(36, individual_firm_costs)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Production at a profit
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_29_1.png)

</div>
</div>
</div>



So, we have seen that a firm produces if the price is above the AVC. The question now is, what is the level of production, i.e., do they produce 8 or 9 units or some other level?

A profit-maximising will produce until price is less than or equal to marginal cost. In the above example, the firm produces 8 units. At the 8th unit, the marginal cost to produce that unit is 28, which is less than the price of 36. Thus the firm gets more revenue for the 8th unit than the cost to produce that unit. But the 9th unit costs an additional 38 to produce. The price of 36 is not enough to cover it. Thus it does not produce the 9th unit.



Therefore, based on the price, each firm looks at its costs and makes a decision to produce. At low prices, only the firms with the lowest production costs produce. As the price increases, firms with higher production costs find it feasible to produce and begin to supply. Thus, the market supply rises with higher prices. Firms with lower costs make extra profits. 



### Let's look at a real life example!
The dataset comes from **EEP 147 Regulation of Energy and the Environment**. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ESG_table = Table.read_table('ESGPorfolios_forcsv.csv').select(
    "Group", "Group_num", "UNIT NAME", "Capacity_MW", "Total_Var_Cost_USDperMWH").sort(
    "Total_Var_Cost_USDperMWH", descending = False).relabel(4, "Average Variable Cost")

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ESG_table

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Group</th> <th>Group_num</th> <th>UNIT NAME</th> <th>Capacity_MW</th> <th>Average Variable Cost</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Old Timers  </td> <td>7        </td> <td>BIG CREEK      </td> <td>1000       </td> <td>0                    </td>
        </tr>
        <tr>
            <td>Fossil Light</td> <td>8        </td> <td>HELMS          </td> <td>800        </td> <td>0.5                  </td>
        </tr>
        <tr>
            <td>Fossil Light</td> <td>8        </td> <td>DIABLO CANYON 1</td> <td>1000       </td> <td>11.5                 </td>
        </tr>
        <tr>
            <td>Bay Views   </td> <td>4        </td> <td>MOSS LANDING 6 </td> <td>750        </td> <td>32.56                </td>
        </tr>
        <tr>
            <td>Bay Views   </td> <td>4        </td> <td>MOSS LANDING 7 </td> <td>750        </td> <td>32.56                </td>
        </tr>
        <tr>
            <td>Old Timers  </td> <td>7        </td> <td>MOHAVE 1       </td> <td>750        </td> <td>34.5                 </td>
        </tr>
        <tr>
            <td>Old Timers  </td> <td>7        </td> <td>MOHAVE 2       </td> <td>750        </td> <td>34.5                 </td>
        </tr>
        <tr>
            <td>Big Coal    </td> <td>1        </td> <td>FOUR CORNERS   </td> <td>1900       </td> <td>36.5                 </td>
        </tr>
        <tr>
            <td>Bay Views   </td> <td>4        </td> <td>MORRO BAY 3&4  </td> <td>665        </td> <td>36.61                </td>
        </tr>
        <tr>
            <td>East Bay    </td> <td>6        </td> <td>PITTSBURGH 5&6 </td> <td>650        </td> <td>36.61                </td>
        </tr>
    </tbody>
</table>
<p>... (32 rows omitted)</p>
</div>


</div>
</div>
</div>



This table shows some electricity generation plants in California and their costs. The Capacity is the output the firm is capable of producing. The Average Variable Cost shows the minimum variable cost per MW produced. At a price below AVC, the firm supplies nothing. At a price above the AVC, the firm can supply up to its capacity. Being a profit-maximising firm, it will try to supply its full capacity.



First, lets look at just the Big Coal producers and understand this firm's particular behavior.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
selection = 'Big Coal'
Group = ESG_table.where("Group", selection)
Group

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Group</th> <th>Group_num</th> <th>UNIT NAME</th> <th>Capacity_MW</th> <th>Average Variable Cost</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Big Coal</td> <td>1        </td> <td>FOUR CORNERS        </td> <td>1900       </td> <td>36.5                 </td>
        </tr>
        <tr>
            <td>Big Coal</td> <td>1        </td> <td>HUNTINGTON BEACH 1&2</td> <td>300        </td> <td>40.5                 </td>
        </tr>
        <tr>
            <td>Big Coal</td> <td>1        </td> <td>REDONDO 5&6         </td> <td>350        </td> <td>41.94                </td>
        </tr>
        <tr>
            <td>Big Coal</td> <td>1        </td> <td>REDONDO 7&8         </td> <td>950        </td> <td>41.94                </td>
        </tr>
        <tr>
            <td>Big Coal</td> <td>1        </td> <td>HUNTINGTON BEACH 5  </td> <td>150        </td> <td>66.5                 </td>
        </tr>
        <tr>
            <td>Big Coal</td> <td>1        </td> <td>ALAMITOS 7          </td> <td>250        </td> <td>73.72                </td>
        </tr>
    </tbody>
</table>
</div>


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Make the plot
plt.figure(figsize=(9,6))
plt.bar(new_x_group, height_group, width=width_group, edgecolor = "black")
# Add title and axis names
plt.title(selection)
plt.xlabel('Capacity_MW')
plt.ylabel('Variable Cost/Price')

plt.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_38_0.png)

</div>
</div>
</div>



We have created the Big Coal Supply curve. It shows the price of electricity, and the quantity supplied at those prices, which depends on Variable Cost. For example, at any Variable Cost equal to or above 36.5, the producer FOUR CORNERS	(the one with the lowest production costs) will supply, and so on.

Notably, we observe that the supply curve is also upward sloping since we need higher prices to entice producers with higher variasble costs to produce. 




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
group_plot(30)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
No production
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_40_1.png)

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
group_plot(37)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Total Production/Market Supply:  1900

Suppliers:  ['FOUR CORNERS']
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_41_1.png)

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
group_plot(50)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Total Production/Market Supply:  3500

Suppliers:  ['FOUR CORNERS' 'HUNTINGTON BEACH 1&2' 'REDONDO 5&6' 'REDONDO 7&8']
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_42_1.png)

</div>
</div>
</div>



Now we will look at all the energy sources. They have been colored according to source for reference.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ESG_plot(30)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Total Production/Market Supply:  2800

Suppliers:  ['BIG CREEK' 'HELMS' 'DIABLO CANYON 1']
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_44_1.png)

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_44_2.png)

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ESG_plot(50)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Total Production/Market Supply:  18650

Suppliers:  ['BIG CREEK' 'HELMS' 'DIABLO CANYON 1' 'MOSS LANDING 6' 'MOSS LANDING 7'
 'MOHAVE 1' 'MOHAVE 2' 'FOUR CORNERS' 'MORRO BAY 3&4' 'PITTSBURGH 5&6'
 'ORMOND BEACH 1' 'ORMOND BEACH 2' 'MORRO BAY 1&2' 'MANDALAY 1&2'
 'CONTRA COSTA 6&7' 'HUNTINGTON BEACH 1&2' 'PITTSBURGH 1-4'
 'EL SEGUNDO 3&4' 'ENCINA' 'REDONDO 5&6' 'REDONDO 7&8' 'COOLWATER'
 'ETIWANDA 1-4' 'SOUTH BAY' 'EL SEGUNDO 1&2' 'HUMBOLDT'
 'HUNTERS POINT 1&2' 'HIGHGROVE']
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_45_1.png)

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/supply/supply_45_2.png)

</div>
</div>
</div>



Look at the thin bars concentrated on the right end of the plot. These are plants with small capacities and high variable costs. Conversely, plants with larger capacities have lower variable costs. 

Why might this be the case? Electricity production typically benefits from economies of scale: it is cheaper per unit when producing more units. Perhaps the high fixed cost required for electricity production, such as for equipment and land, is the reason behind this phenomenon. 

