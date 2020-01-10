---
interact_link: content/supply/horizontal-sum-supply.ipynb
kernel_name: python3
has_widgets: false
title: 'Horizontal Sum Supply'
prev_page:
  url: /topic-intros/supply.html
  title: 'Supply and Firm Behavior'
next_page:
  url: /supply/production.html
  title: 'Production'
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
import qgrid
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

```
</div>

</div>



This Notebook will demonstrate using QGrid - a way to interact with the data in a table.  Unfortunately Qgrid works with Pandas, so this Notebook uses a pandas Dataframe as its data source. (I used the naming convention df for dataframe)

1. First we will read in a dataframe with some Supply functions for 3 firms, they have 3 quantities they will supply at three possible prices
2. In the first part Firm C is not producing anything , and production is set at zero
3. We will create a market supply by summing the supply from Firm A and Firm B
4. When the widget is created - you can enter and edit the values of the cells




## DataFrame Widget



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
df_Market = pd.DataFrame({
    'Price' : [5, 10, 15],
    'A' : [20, 30, 40],
    'B' : [25, 35, 50], 
    'C' : [0, 0, 0],  })

df_Market['Total_Supply_ABC'] = df_Market['A'] + df_Market['B']+ df_Market['C']

qgrid_widget = qgrid.show_grid(df_Market, show_toolbar=True)
qgrid_widget

```
</div>

</div>



So go in and play around with different values for firm C

How about [12,17,55]

or how about [0,25,55}

What do we have to assume about C ( it has to increase or stay the same as Price increases) 



*Note - if you manipulate the data in the Qgrid widget - you need to save the dataframe - here we rename it as updated_df*



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
updated_df=qgrid_widget.get_changed_df()
updated_df['Total_Supply_ABC'] = updated_df['A'] + updated_df['B']+ updated_df['C']
updated_df

```
</div>

</div>



## Graphing
Now we are going to graph the individual supply curves of each firm, alongside the total Supply to crease a Market Supply



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

ax = plt.gca()
updated_df.plot(kind='line', y='Price', x='A', ax=ax)
updated_df.plot(kind='line', y='Price', x='B', ax=ax)
updated_df.plot(kind='line', y='Price', x='C', ax=ax)
updated_df.plot(kind='line', y='Price', x='Total_Supply_ABC', ax=ax)
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Market Supply')
plt.legend(("Quantity supplied by A","Quantity supplied by B","Quantity supplied by C", "Market Supply A+B"), bbox_to_anchor=(1.04,1), loc="center left")

plt.show()

```
</div>

</div>



## Thought questions

1.  Can the individual supply lines cross?

2. Can individual supply schedules = 0, at a lower price?

3. Can lines bend backwards?




##  Market Analysis - Supply Demand and new market entrant
Let's start again and add in
1. A demand function
2. A comparison of the supply with just firms A and B to with a third firm C
3. What happens to equilibrium Price and Quantity?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
qgrid_widget = qgrid.show_grid(updated_df, show_toolbar=True)
qgrid_widget

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
updated_df=qgrid_widget.get_changed_df()
updated_df['Total_Supply_AB'] = updated_df['A'] + updated_df['B'] 
updated_df['Total_Supply_ABC'] = updated_df['A'] + updated_df['B'] + updated_df['C']

```
</div>

</div>



Lets specify a Demand curve - prices and quantities - so we need Quantities demanded that correspond to a price of [5,10,15]



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Demand =[100,75,50]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
updated_df['Demand']=Demand

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
updated_df

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
ax = plt.gca()
updated_df.plot(kind='line', y='Price', x='A', ax=ax)
updated_df.plot(kind='line', y='Price', x='B', ax=ax)
updated_df.plot(kind='line', y='Price', x='C', ax=ax)
updated_df.plot(kind='line', y='Price', x='Total_Supply_AB', ax=ax)
updated_df.plot(kind='line', y='Price', x='Total_Supply_ABC', ax=ax)
updated_df.plot(kind='line', y='Price', x='Demand', ax=ax)

plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Market Supply')
plt.legend(("Quantity supplied by A","Quantity supplied by B","Quantity supplied by C", "Supply_AB","Supply_ABC", "Total Demand" ), bbox_to_anchor=(1.04,1), loc="center left")

plt.show()

```
</div>

</div>



## Thought questions 2
1. What happens to the market price and quantity?  Can you eyeball the changes?

2. What happens to each individual producer - can you tell from this graph?
3. Should firm C enter the market?



### Moving On

Click [here](Intro_to_Production.ipynb) to open the next notebook.



 

