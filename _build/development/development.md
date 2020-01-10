---
interact_link: content/development/development.ipynb
kernel_name: python3
has_widgets: false
title: 'Economic Development: Africa'
prev_page:
  url: /topic-intros/development.html
  title: 'Economic Development: Africa'
next_page:
  url: /topic-intros/finance.html
  title: 'Finance and Time Series Data'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<table style="width: 100%;">
    <tr style="background-color: transparent;"><td>
        <img src="https://d8a-88.github.io/econ-fa19/assets/images/blue_text.png" width="250px" style="margin-left: 0;" />
    </td><td>
        <p style="text-align: right; font-size: 12pt;"><strong>Economic Models</strong>, Fall 2019<br>
            Dr. Eric Van Dusen</p></td></tr>
</table>



# Lab 8: Water Guard Promotion Study

This lab is an adaptation from a set of notebooks developed for a full semester Data Science Connector Course taught in Fall 2017, entitled "Behind the Curtain in Economic Development".  This dataset come from a randomized controlled trial household survey carried out in Eastern Kenya in 2007 - 2008. 

The purpose of the study was to understand how to promote the use of WaterGuard, a dilute sodium hypochlorite solution that was promoted for Point-of-use household water disinfection.  There were seven arms in the study - which will be more fully described in the following Table:




<img src="Slide1.png"  />



Within this table you can see the seven treatments arms -  control plus three treatments -  in the bolded boxes in the middle with the number of springs and households. The study was carried out as a part of a study of households who gather drinking water from springs in a rural area.  The three boxes at the bottom describe the three rounds of data collection - a baseline before the treatment, and a short term and long term follow-up.  



**Notebook Outline**

1. [Mapping](#Mapping)
2. [Balance Check](#Balance)
3. [Baseline and a Randomly Selected Compound](#Baseline)
4. [Chlorine Usage outcome variables](#Chlorine)
5. [Graph of outcomes by Treatment Arm](#Graph)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from datascience import *
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
from pandas import read_stata

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#! jupyter labextension install @jupyter-widgets/jupyterlab-manager

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#! pip install gmaps

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#! jupyter lab build


```
</div>

</div>



# Mapping

<div id="Mapping"></div>




This first section works with a package in Jupyter called Gmaps, 
the documentation is [here](http://jupyter-gmaps.readthedocs.io/en/latest/gmaps.html)
and it is worth a short read through if you are interested

For Data 8 users, a basic mapping program is included in the datascience module
it is called Folium and makes open source maps from python data
the documentation is [here](http://folium.readthedocs.io/en/latest/index.html)

In rural Kenya there are few roads and very limited coverage with Open Street Map base layer that works in Folium.  Therefore we will use the satellite layer which is avialable from Google Maps.




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# if you want to run this on a local machine you may need to do the following
# at the terminal prompt need to do $ pip install gmaps
# at the terminal prompt need to do $ jupyter nbextension enable --py gmaps
# may have to quite jupyter and restart terminal and then do the above prompt
# need a GMAPS API token  - mine is (new Nov 2018)  AIzaSyCw6FrENSBnz8T_dHRiPSaNw299bIuYA-g
# This code is following along from http://jupyter-gmaps.readthedocs.io/en/latest/gmaps.html

import gmaps
import gmaps.datasets
gmaps.configure(api_key="AIzaSyCw6FrENSBnz8T_dHRiPSaNw299bIuYA-g") # Fill in with your API key

```
</div>

</div>



We will start by reading in a dataset of the GPS coordinates of the springs that are used in the WaterGuard Promotion (WGP) study.  These springs were randomized into seven different treatment arms.  The springs are identified by a unique numerical id tag, and the common name in the local language.  




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
springsGPS = Table.read_table('WGPgps_forData8.csv')
springsGPS

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#make a table with just the North and East Gps columns 

locations = springsGPS.select("gpsn1", "gpse1")
locations

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

# once the map is displayed, click the tab to display the satellite view

fig = gmaps.figure()
markers = gmaps.marker_layer(locations.to_df())
fig.add_layer(markers)
fig

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Let's change the color of the symbols 

fig = gmaps.figure()
symbols = gmaps.symbol_layer(locations.to_df(),fill_color="red")
fig.add_layer(symbols)
fig

```
</div>

</div>



Now the most interesting bit of data is still not being used, the Treatment Arm
Lets assign different colors to the different treatment arms
So that when we map it we can look and see if the arms appear to be randomly distributed

The following is function, that assigns the 1-7 of the treatment arms to a set of colors

Here is the colors reference if you are interested!  
https://www.w3.org/TR/css3-color/#html4




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def color(arm):
    if arm == 1:
        return 'fuschia'
    elif arm == 2:
        return 'red'
    elif arm == 3:
        return 'purple'
    elif arm == 4:
        return 'green'
    elif arm == 5:
        return 'blue'
    elif arm == 6:
        return 'olive'
    elif arm == 7:
        return 'teal'

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Using the .apply method, you can apply any function to a data frame
colors = springsGPS.apply(color, "treatment_arm")
springsGPS = springsGPS.with_column("color", colors)
springsGPS

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
fig = gmaps.figure()
symbols = gmaps.symbol_layer(locations.to_df(),
                             stroke_color=list(springsGPS.column("color")),#['color'].tolist(),
                             fill_color=list(springsGPS.column("color"))#['color'].tolist()
                            )
fig.add_layer(symbols)
fig

```
</div>

</div>



**Visual inspection of the map:**
Do the colors seem randomly distributed ?
In fact the randomization was performed on just a list of the springs using a random number generator.  It did not take spatial distribution into effect.  




## Question 1  - Thought Experiment - Spatial Randomization
1.1 What could you do to test whether the Treatment arms are spatially distributed.

1.2 What could you do to randomize the treatment arms over space.



<div id="Balance"></div>

# Balance Check and Variable Names






## Baseline Survey
This is our first look at the survey dataset.  These are a limited set of questions/answers from a simple and short baseline survey. However it is a lot bigger and messier than the datasets we have been seeing in Data8. 

Data variable names follow along with the survey below, referred to by the section, a,b,c... number, 1,2,3... and a few words about the question. 

The purpose of this section will be: 
* to get a familiarity with the dataset, 
* to look at some background descriptor variables of the households, 
* to start to think about missing values and coding of subsets of the data.  
* to checking the randomization of households by seeeing if the different arms of the study are balanced across some of the key baseline variables.  

**The surveys that illustrate the raw data names are in a Box folder linked here -  You have to go and look through this survey to understand the variables**
https://goo.gl/TzzvLb  or  https://drive.google.com/open?id=1UVoiVn7LJ4rn7WEb-9BJ96jmdJ2FBk60


*A note on Pandas vs datascience/tables*
- The main Data8 class is taught mostly using a Python package designed specifically for the class called `datascience`.  The more popular package for statistical analysis is called `pandas`. 
- Throughout this Lab, there are some commands mostly in `Pandas`




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Option to allow Pandas to display many columns
# there are 200 something columns in this dataset
pd.set_option('display.max_columns', 500)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
WGP_baseline = pd.DataFrame(pd.read_stata('WGP_baseline_Data8.dta'))
WGP_baseline

```
</div>

</div>



## Misssing values ~ NaN
if you look through the dataset above, and scroll to the right a ways to some of the last variables, you will notice that that there are a lot of cells with NaN, which means a missing value. For these cells no data was entered at the time of data entry. In some cases it may be appropriate to enter a zero and carry on with the analyis.  





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# There are a lot of missing values in the data, so we can make a copy of the dataset/dataframe
# that has zeros in the place of 'nan' - mising data values
WGP_base_dfna = WGP_baseline.fillna(0)
# this is a second dataframe that we can call with a different name
WGP_base_dfna.head(10)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Lets make a datascience table at the same time
WG_basetable= Table.from_df(WGP_baseline)
# this is a table that we can use with the data8/datascience commands
WG_basetable

```
</div>

</div>



 Look at the variable names, and then look at the survey form to find the concordance of codes



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Here is a list of all of the possible categories / columns
list(WGP_baseline)

```
</div>

</div>



## What are some Variables that we want to specifically look at?




### Front Page information - A variables
 - household id, 
 - spring id, 
 - interviewer id

### Information about respondent - B variables
- tribe
 - education
 - age
 - gender 
 - group membership
 
### Water Guard Use - C variables
for Waterguard (WG),(survey questions on other chlorine not in this dataset) 

- c1a - have you ever heard of WG
- c2a - have you ever used WG
- c3a - is your water currently treated with WG
- c4a - have you used WG in past month

### Durable / Capital Goods - D variables
 - electricity  / latrine / iron roof  ( yes / no) 
 - bicycle/ radio / hoe / beds ( number of items owned)
 - number of animals (number)
 
### Child Health - E variables
 -  number of kids under 5 =  e1_num_kids_under_5
 
e2_ This table becomes tricky because it has a different format 
Each kid in the table is numbered 01, 02 etc
and then the subsequent questions keyed to that child number
e2e_01_d_diarrhea, e2e_02_d_diarrhea, e2e_03_d_diarrhea
for four diseases:

 - cough
 - Diarrhea
 - fever_malaria
 - vomiting
 


 



### Treatment Arm -  There is an additional variable called treatment arm
### Arm 1 is control, and Arms 2-7 are different types of treatment interventions
 
- Arm 1 - Control
- Arm 2 - Household Script
- Arm 3 - Community Script
- Arm 4 - HH + Community Script
- Arm 5 - Flat-Fee Promoter + Coupons
- Arm 6 - Incentivized Promoter + Coupons
- Arm 7 - Incentivized Promoter + Dispenser at Spring

*How many households are in each Treatment Arm?*




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
WG_basetable.group("treatment_arm")

```
</div>

</div>



## Baseline Check - Exposure to Water Guard Use



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### Using a variable for if the Household has ever used WaterGuard
WGP_baseline.groupby("c2a_wg_used_ever").size()

```
</div>

</div>



The data is currently Coded as 1 = Yes and 2 = No 

So we cant really make sense of the Mean of the variable in its current form

Make a new column/variable with 1/2 answers translated into Yes/NO



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

WGP_baseline["WG Ever Use"] = WGP_baseline["c2a_wg_used_ever"].astype("category")
WGP_baseline["WG Ever Use"].cat.categories = ["Yes", "No" ]
WGP_baseline.groupby("WG Ever Use").size()

```
</div>

</div>



## Crosstab - in `pandas`

Now we will use a command called a `Crosstab` - that is an abbreviation for cross-tabulation - that is easy to call in `pandas` but we would need to program in `datascience` 

We can first use it to do a  balance check for Water Guard use across Arms 






<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#Table of treatment arm vs Water Guard Use but with Percentages
WGUsec2VStreatment = pd.crosstab(index=WGP_baseline["WG Ever Use"], 
                            columns=WGP_baseline["treatment_arm"],
                             margins=True)   # Include row and column totals
WGUsec2VStreatment/WGUsec2VStreatment.loc["All"]



```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Now lets check and see how many households are currently using WG -
# Variable name is c3a_wg_water_currently_treat

WGP_baseline.groupby("c3a_wg_water_currently_treat").size()

```
</div>

</div>



*Do you notice a problem here? Look at the total numbers reported in the output above*

 We can do the same percentage tables for the balance check 
 
 but maybe there's a problem?  ( look at the total number of hhs answering the question!)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Table of treatment arm vs Water Guard Use but with Percentages
WG_c3VStrt = pd.crosstab(index=WGP_baseline["c3a_wg_water_currently_treat"], 
                            columns=WGP_baseline["treatment_arm"],
                             margins=True)   # Include row and column totals
WG_c3VStrt/WG_c3VStrt.loc["All"]
# In this case the 1's represent the percent  answering yes, out of all those who answered the question


```
</div>

</div>



**Seems like a really high usage ... maybe this is due to missing values**

Earlier we created a dataset where the missing values "nan" were replaced with zeros

If we use this dataset we would have percents over the total population surveyed





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#Table of treatment arm vs Water Guard Use,  Percentages, with missing values substituted with zeros
WG_c3VStrt = pd.crosstab(index=WGP_base_dfna["c3a_wg_water_currently_treat"], 
                            columns=WGP_base_dfna["treatment_arm"],
                             margins=True)   # Include row and column totals
WG_c3VStrt/WG_c3VStrt.loc["All"]
# In this case the 1's represent the percent  answering yes, out of all those who were surveyed


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#Lets make this Crosstab Table look a little nicer, by rounding and multiplying by 100
np.round(100*WG_c3VStrt/WG_c3VStrt.loc["All"],2)

```
</div>

</div>



##  Question 2
- 2.1 Explain the previous table clearly and concisely, as if you were explaining it to someone who didnt know the back story
- 2.2What are the rows, what are the columns, why are we doing this?  ( Rows - What does the 0 mean, what does the 1 mean and what does the 2 Mean? )
- 2.3 Balance Check - How does the randomization look?



<div id="Baseline"></div>

# Baseline and a Randomly Selected Compound






### Lets have you describe a household selected at Random

Step 1) Lets extract the household / compound id into an array of all the possible values



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
hhld_array=WG_basetable.column('a1_cmpd_id')

hhld_array

```
</div>

</div>



Step 2) Lets draw randomly from this array



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
randomhh=np.random.choice(hhld_array)
print("My randomly selected household is" , randomhh)

```
</div>

</div>



Step 3)  Lets Look at the data for my randomly selected HH:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myfamily = WG_basetable.where("a1_cmpd_id",np.random.choice(WG_basetable.column('a1_cmpd_id')))
myfamily

```
</div>

</div>



Some of the variables may need some manipulation - Lets start with the age of the respondant:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
birthyear=  myfamily.column("b3_birth_year")  # find the variable
surveyyear= myfamily.column("a5_date_interview_year") # find the variable
agecalc =surveyyear-birthyear  # 
agecalc

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#  code the answer for Tribe
print("Survey respondent Tribe",myfamily.select("b5_tribe"))
print("Respondent Spouse Tribe",myfamily.select("b7_tribe_spouse"))

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("Does the household have a latrine?",myfamily.select("d3_latrine"))

```
</div>

</div>



Remember in the answer above it is coded so that 1=Yes and 2=No



# Question 3 - Describe your randomly selected household and the respondent who is answering the survey.

1. Age
2. Tribe
3. Education - 
4. Member of any groups b11-b15?
5. Occupation - 
6. Religion - 
7. A summary of D variables, iron roof, floor materials, latrine, cattle, others..
8. Have they ever used WG?
9. Treatment Arm - what was the assignment
10. How many children do they have  
11. Gender and Age of children
12. Have any of the children been sick?




<div id="Chlorine"></div>

# Chlorine Usage outcome variables






## WGP Followup - Variability
The purpose of this section will be to continue on with the follow-up rounds of the Water Guard Promotion study.   In this section we have both the household reported use, and the use validated by checking the chlorine content of the water using a test kit.  

To present this outcome data we need to program the following
1. Graphing Data by treatment arm
2. Confidence Interval - standard deviation  - error bars




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
WGP3rds_df = pd.DataFrame(pd.read_stata('WGP_3waves_Data8.dta'))
WGP3rds_table= Table.from_df(WGP3rds_df)
#WGP_df.head(10)

```
</div>

</div>



##### This is a large dataset, basically three datasets merged together, one for baseline, one for short term follow up and one for long term followup
 - Round = 1 : baseline
 - Round = 2 : 3 week followup
 - Round = 3 : 3 month followup
 
Many of the variables are only asked in one of the three rounds




 - The variable for self_reported chlorine use was "c6n" in Round 2, and 'c5n' in Round 3
 - The variable for chlorine use is "c12n21pnk" in Round 2 and 'c15npt2or1pnk' in Round3
 
 
**The following variables have been combined across rounds for the ease of programming**
 - 'Selfrptpct' is self reported chlorine use in both round 2 and round 3
 - 'Vldclpct'  is validated chlorine use in both rounds
 
 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Here is a list of all of the possible categories / columns
#list(WGP3rds_df)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#WGP_baseline.groupby('e1_num_kids_under_5').size()
WGP3rds_df.groupby('treatment_arm').size()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
WGP3rds_df.groupby('round').size()

```
</div>

</div>





**Groupby**

Another really nice `pandas` feature is the ability to group by two different variables. In this calse we want to group by survey round, and by treatment arm.  




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
WGP3rds_df.groupby([ 'round', 'treatment_arm',]).size()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Which brings us to a new  way to look at the outcome data - grouping by two variables in Pandas an calling for means
# Make a smaller df with just the outcome variables
WGP_3rds_outcomesonly= pd.DataFrame(WGP3rds_df,columns=['round','treatment_arm','Selfrptpct','Vldclpct'])
# Then call for the means
WGP_3rds_outcomesonly.groupby([ 'round','treatment_arm']).mean()

```
</div>

</div>



### Making a smaller dataset

Lets break out a smaller dataset of the variables we want to focus on - just for Round 2, just for the outcome variables





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
WGPRd2 = WGP3rds_table.where("round",2).select("a1_cmpd_id","treatment_arm",
                                           "c6_current_water_treated_wg", 
                                           'c6_curr_water_treat_other_c',
                                           'c12_chlorine_meter_reading',
                                           'c11_chlorine_color','c12n21pnk', 'c6n'
                                          )
WGPRd2

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# make a pandas dataframe df for Round 2
WGP_rnd2df= WGP3rds_df.where(WGP3rds_df['round'] ==2)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# we can start by looking at the estimate of WG use in Round 2 across all treatment arms ( for the entire sample) 
np.mean(WGPRd2.column('c12n21pnk'))

```
</div>

</div>



## Confidence Interval

Lets compute a confidence interval for the percent of households using Chlorine ( Validated by a Chlorine measurement) 

1. Compute the proportion
2. Number in each population
3. Standard Errors following a formula
4. Confidence Interval




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Compute Standard Error of a proportion
# We can do this the first time for the entire sample
# Save the followng values
p_all=np.mean(WGPRd2.column('c12n21pnk'))
N_all=WGPRd2.num_rows

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#  The formula for the SE of a proportion is sqrt((p1(1-p1))/N)
se_all=((p_all*(1-p_all))/N_all)**0.5
se_all

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Upper bound of CI
# Using Z = 1.96
Z=1.96
upper_all = p_all+Z*se_all
lower_all = p_all-Z*se_all
CI_all=(upper_all,lower_all)
CI_all

```
</div>

</div>



## Using this technique we can look at the Confidence Intervals for each of the treatment arms




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Here is the code for just arm 1
p_1=np.mean(WGPRd2.where("treatment_arm",1).column('c12n21pnk'))
N_1=WGPRd2.where("treatment_arm",1).num_rows
N_1
print("In Round 2, the number of households in arm 1 Control is:", N_1)
print("The share of households with Validated WG use is: ", p_1)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
se_1=((p_1*(1-p_1))/N_1)**0.5
print("The standard error of the Validated WG estimate is: ", se_1)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Upper bound of CI
# Using Z = 1.96
Z=1.96
upper_1 = p_1+Z*se_1
lower_1 = p_1-Z*se_1
CI_1=(upper_1,lower_1)
print("The 95% Confidence Interval for Validated WG use is: ", CI_1)

```
</div>

</div>



** Repeating for Arm 2 **




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Here is the code for just arm 2
p_2=np.mean(WGPRd2.where("treatment_arm",2).column('c12n21pnk'))
N_2=WGPRd2.where("treatment_arm",2).num_rows
N_2
print("In Round 2, the number of households in arm 1 Control is:", N_2)
print("The share of households with Validated WG use is: ", p_2)
se_2=((p_2*(1-p_2))/N_2)**0.5
print("The standard error of the Validated WG estimate is: ", se_2)
# Upper bound of CI
# Using Z = 1.96
Z=1.96
upper_2 = p_2+Z*se_2
lower_2 = p_2-Z*se_2
CI_2=(upper_2,lower_2)
print("The 95% Confidence Interval for Validated WG use is: ", CI_2)


```
</div>

</div>



## Question 4.1 - What can we tell by comparing the confidence intervals for Arm 1 and Arm 2.  Do they overlap?  What does that mean?



***type your answer here***



## Question 4.2 - Propose an additional hypothesis to test with this data?  Program the confidence interval for another treatment arm and see if it is different than the control arm.



***written answer proposing a hypothesis test ***



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# coding section

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# coding section

```
</div>

</div>



<div id="Graph"></div>

# Graph of outcomes by Treatment Arm






## WGP Followup Round 2, Round 3, and across rounds

Now we will work on making a make a summary graph for the WGP study. This graph should show the seven treatment arms with the levels of our outcomes, and include error bars.  In addition, we can work on customizing and saving our graph.  





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
WGPRd2 = WGP3rds_table.where("round",2).select("a1_cmpd_id",'treatment_arm','Selfrptpct', 'Vldclpct')
WGPRd2

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Lets group by treatment_arm take the means of each group
# This corresponds to the summary stats in Lab 5
round2_means = WGPRd2.group('treatment_arm', np.mean)
round2_means

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# We have the means in a table, let's also make an array of these outcomes
# Save the means into an array for later use
round2_means_self_array = round2_means.column('Selfrptpct mean')
round2_means_vld_array = round2_means.column('Vldclpct mean')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# first graph - bar chart 
round2_means.bar('treatment_arm','Selfrptpct mean') 

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Round 2 - bar chart with both self and validated 
round2_means.bar('treatment_arm',make_array(2, 3)) 

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# redoing it for round 3
WGPRd3 = WGP3rds_table.where("round",3).select("a1_cmpd_id",'treatment_arm','Selfrptpct', 'Vldclpct')
round3_means = WGPRd3.group('treatment_arm', np.mean)

# array of means
round3_means_array = round3_means.column('Selfrptpct mean')
print(round3_means_array)


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Round 3 Graph
round3_means.bar('treatment_arm',make_array(2, 3)) 

```
</div>

</div>



## Practice with pyplot & Matplotlib
Now we can make a graph that compares round 2 and round 3 

This is a more complicated graphing using Matplotlib

**references at:**
1. https://matplotlib.org/gallery/api/barchart.html
2. https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
plt.style.use('seaborn')  # You can try changing the style 

N = 7
ind = np.arange(N)  # the x locations for the groups
width = 0.5       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, round2_means_self_array, width, color='g')
rects2 = ax.bar(ind + width, round3_means_array, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Percent of HH using WG')
ax.set_title('Self reported WG use')
ax.set_xlabel('Treatment Arm')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('1', '2', '3', '4', '5', '6','7'))
ax.legend((rects1[0], rects2[0])
          ,('3 Week Visit', '3 Month Visit')  # relabeling Round 2 and Round 3
          ,bbox_to_anchor=(0.5, 1.0))  # placing the legend in the graph 
plt.show()

# If you want to save the figure into an image file
#plt.savefig("test.png")




```
</div>

</div>



## Question 5 - Make a version of this graph for Validated Presence of WG



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#  Code in here

```
</div>

</div>



*Explanation of what you did here*



## Extra Credit Section on Error Bars... if you are interested



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#  Repeat this for the standard deviation
round2_stdev = WGPRd2.group('treatment_arm', np.std)
round2_stdev

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Get the number in each arm for adjusting the SD
round2_num= WGPRd2.group('treatment_arm')
round2_num

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# make an array of standard errors
round2_self_stdev_array= round2_stdev.column('Selfrptpct std')
print (round2_self_stdev_array)
# make an array of numbers n
round2_self_num_array = round2_num.column('count')
print (round2_self_num_array)
# make and array of the square root of n
round2_self_sqrtn_array = np.sqrt(round2_self_num_array)
print (round2_self_sqrtn_array)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Make the standard error dividing the SD by the square root of n
round2_self_se=np.divide(round2_self_stdev_array,round2_self_sqrtn_array)
print (round2_self_se)
round2_self_2se = round2_self_se*2
round2_self_2se

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Let's add in the error bars - adding in yerr= 2* SE - this would be the 95% Confidence Interval
round2_means.bar('treatment_arm','Selfrptpct mean', yerr=round2_self_2se) 

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Standard Errors for round 3
round3_stdev = WGPRd3.group('treatment_arm', np.std)
round3_num= WGPRd3.group('treatment_arm')
# make an array of standard errors
round3_self_stdev_array= round3_stdev.column('Selfrptpct std')
round3_self_num_array = round3_num.column('count')
round3_self_sqrtn_array = np.sqrt(round2_self_num_array)
#print (round2_self_sqrtn_array)
round3_self_se=np.divide(round3_self_stdev_array,round3_self_sqrtn_array)
print (round3_self_se)
round3_self_2se = round3_self_se*2
round3_self_2se

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Round 3 Graph
round3_means.bar('treatment_arm','Selfrptpct mean', yerr=round3_self_2se) 

```
</div>

</div>



## Extra Credit  -  Make another graph
Make another graph similar but different to the previous 6 ones above, that 
- uses the Validated means and Confidence Intervals 
- looks awesome ( change the colors, choose the orientation, think about what you wish it looked like)
- Add a short paragraph of explanation - what can you summarize from looking at the error bars in your graph?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#  add code here 

```
</div>

</div>



Write a short paragraph explaining and interpereting your graph



## Practice with pyplot & Matplotlib



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# This is just to check our inputs in to the more complicated graph in the following cell
#print(round2_means_array,round2_self_stderr_array )
# Shouldnt be necessary, but in case you have problems

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Now we can make a graph that compares round 2 and round 3 
# This is a more complicated graphing using Matplotlib

# following from https://matplotlib.org/gallery/api/barchart.html
# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
#plt.style.use('fivethirtyeight')
%matplotlib inline
plt.style.use('classic')

N = 7
ind = np.arange(N)  # the x locations for the groups
width = 0.5       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, round2_means_self_array, width, color='g', yerr=round2_self_2se)

rects2 = ax.bar(ind + width, round3_means_array, width, color='b', yerr=round3_self_2se)

# add some text for labels, title and axes ticks
ax.set_ylabel('Percent of HH using WG')
ax.set_title('Self reported WG use')
ax.set_xlabel('Treatment Arm')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('1', '2', '3', '4', '5', '6','7'))

ax.legend((rects1[0], rects2[0])
          ,('3 Week Visit', '3 Month Visit')
          ,bbox_to_anchor=(0.5, 1.0))

#plt.savefig("WG_Trial.png")

plt.show()


```
</div>

</div>



 

