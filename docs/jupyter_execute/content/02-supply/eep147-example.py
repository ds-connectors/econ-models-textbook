from datascience import *
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import pandas as pd
from utils import *
plt.style.use('seaborn-muted')
from matplotlib import patches
import csaps
import warnings
warnings.filterwarnings("ignore")

# An Empirical Example from EEP 147

Let's take a look at an empirical example of production. The dataset for this section comes from EEP 147: Regulation of Energy and the Environment.

ESG_table = Table.read_table('ESGPorfolios_forcsv.csv').select(
    "Group", "Group_num", "UNIT NAME", "Capacity_MW", "Total_Var_Cost_USDperMWH"
).sort("Total_Var_Cost_USDperMWH", descending = False).relabel(4, "Average Variable Cost")
ESG_table

This table shows some electricity generation plants in California and their costs. The `Capacity` is the output the firm is capable of producing. The `Average Variable Cost` shows the minimum variable cost per megawatt (MW) produced. At a price below AVC, the firm supplies nothing. At a price above the AVC, the firm can supply up to its capacity. Being a profit-maximising firm, it will try to supply its full capacity. 

First, lets look at just the Big Coal producers and understand this firm's particular behavior.

selection = 'Big Coal'
Group = ESG_table.where("Group", are.equal_to(selection))
Group

# Make the plot
plt.figure(figsize=(9,6))
plt.bar(new_x_group, height_group, width=width_group, edgecolor = "black")
# Add title and axis names
plt.title(selection)
plt.xlabel('Capacity_MW')
plt.ylabel('Variable Cost/Price')

plt.show()

We have created the Big Coal supply curve. It shows the price of electricity, and the quantity supplied at those prices, which depends on variable cost. For example, at any variable cost equal to or above 36.5, the producer `FOUR CORNERS` (the one with the lowest production costs) will supply, and so on. Notably, we observe that the supply curve is also upward sloping since we need higher prices to entice producers with higher variasble costs to produce. 

group_plot(30)

group_plot(37)

group_plot(50)

Now we will look at all the energy sources. They have been colored according to source for reference.

ESG_plot(30)

ESG_plot(50)

Look at the thin bars concentrated on the right end of the plot. These are plants with small capacities and high variable costs. Conversely, plants with larger capacities tend to have lower variable costs. Why might this be the case? Electricity production typically benefits from economies of scale: it is cheaper per unit when producing more units. Perhaps the high fixed cost required for electricity production, such as for equipment and land, is the reason behind this phenomenon. 

 