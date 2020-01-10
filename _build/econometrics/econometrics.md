---
interact_link: content/econometrics/econometrics.ipynb
kernel_name: python3
has_widgets: false
title: 'Econometrics and Data Science'
prev_page:
  url: /topic-intros/Econometrics.html
  title: 'Econometrics and Data Science'
next_page:
  url: /econometrics/dummy-variables.html
  title: 'Dummy Variables'
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
from datascience import *

```
</div>

</div>



# Lab 12: Regression



## An Introduction to Regression and Econometrics



A core practice within economics is econometrics, or the use of statistics concepts and economic interpretation to understand the underlying relationship between two or more variables - how one variable affects the other. The tool by which economists and statisticians do this is regression. We predict some variable Y, noted as the outcome or independent variable, using another variable X, known as the regressor or explanatory variable.

As we have learned from Data 8, regression is simply the method of fitting a line to a bunch of data points. Thorugh this, we select the slope and intercept that minimize the sum of squared errors. The line that is generated from this method is called the line of best fit.

When given that line, the coefficients on the variables then become important explanatory tools for understanding the effects of one variable upon another. This notebook will give an introduction into single and multi-variable regression, and their interpretations in economic contexts.



## Terminology



#### Left-Hand Side

$y$ - Outcome variable, dependent variable 



#### Right-Hand Side

$x$ - Regressor, independent variable, explanatory variable.  In machine learning, this is called a feature.

$\alpha$ or $\beta$ - Coefficient on the variable or, if it is not associated to any variable, an intercept term.

$\varepsilon$ - Error term, containing any unexplained variation that the model does not capture.

Categorical Variable - When the Right Hand Side variable is a 0-1 variable, in econometrics we call this a dummy variable, whereas in machine learning we call this a one-hot encoding.  When the left-hand side variable is a 0-1 variable we call this a classification problem in ML, and we would usually call the specification a logistic regression.  



## Introducing our dataset: NLSY79



Throughout the notebook, we will be using the NLSY79 dataset. This is a survey of young men and women who were 14-22 years old and was first collected in 1979. It contains information such as years of schooling, intelligence measured through a test called AFQT, and annual earnings.

For this lab, we will aim to predict individuals' annual earnings from different information provided by the dataset. Thus, using the terminology above:

$y$ - Annual earnings

$x$ - Years of schooling, AFQT



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nlsy_79 = Table().read_table("nlsy79.csv")
nlsy_79 = nlsy_79.drop(0)
nlsy_79.show(5)

```
</div>

</div>



## Single Variable Regression



The underlying formula that guides linear regression is the following. It is also called the regression line.

The general notation is:

$$
y = \alpha + \beta \cdot x + \varepsilon
$$

- $y$ represents the outcome or the thing we want to predict. It is also know as the dependent variable.

- $\alpha$ is the intercept term.

- $\beta$ is the slope of the regression line, or the coefficient on the $x$ variable.

- $\varepsilon$ is the error term. This is what attempts to model the variance in the data, and is also called noise.

The idea behind this formula is that if my $x$ value increases by 1, I expect my $y$ value to change by $\beta$. That is rise over run. That's why we also call $\beta$ the slope of the regression line. We assume that in the world, the "true model" follows this equation. There is a "true" $\alpha$ and $\beta$ value and some random noise. The $y$ that we observe is a linear combination of these. 

Since the error is random, with our linear model, we aim to predict our best estimate of $\alpha$ and $\beta$. We will call them $\hat{\alpha}$ and $\hat{\beta}$. These are read as "alpha hat" and "beta hat". The 'hats' represent estimates of the true values.

First, let our model prediction be called $\hat{y}$, which is given by:

$$\hat{y} = \hat{\alpha} + \hat{\beta} \cdot x$$

While we can arbitrarily pick $\hat{\alpha}$ and $\hat{\beta}$ values, we do want to pick the values that help predict $\hat{y}$ that are closest to actual $y$ values. To achieve this, we want to minimize a loss function called the "Root Mean Squared Error" which is defined as

$$
\text{RMSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^n \left ( y_i - \hat{y}_i \right ) ^2 }
$$

$n$ is the number of observations. The effect of this is to take the mean of the distance of each value of $\hat{y}$ from its corresponding value in $y$; squaring these values keeps them positive, and then we take the square root to correct the units of the error.

Plugging in the formula $\hat{y}$ in RMSE formula, we get, 
$$
\text{RMSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^n \left ( y_i - (\hat{\alpha} + \hat{\beta}x_i) \right ) ^2 }
$$

By doing a bit of math (which we will not go over in this class), we get the following formulas for $\hat{\alpha}$ and $\hat{\beta}$

$$\Large
\hat{\beta} = r\frac {SD_y} {SD_x}
$$

$$\Large
\hat{\alpha} = \bar{y} - \hat{\beta}\bar{x}
$$

- $r$ is the correlation between x and y
- ${SD_y}$ is the standard deviation of y
- ${SD_x}$ is the standard deviation of x
- $\bar{y}$ is the average of all our $y$ values 
- $\bar{x}$ is the average of all our $x$ values

where

$$
r = \frac{1}{n}\sum^n_{i=1}\text{SU}_{xi}\text{SU}_{yi}
$$



## Single Variable Regression and the NLSY79 dataset



We will now apply this to the NLSY79 dataset. Let us attempt to predict future annual earnings using number of years of schooling. Our regression equation will become:
$$
y = \alpha + \beta \cdot x + \varepsilon
$$

Where: 
- $y$ = annual earnings for the year 2000, for the given individual
- $x$ = number of years of schooling accomplised by the individual when they were 28
- $\varepsilon$ = error term



To be clear, the regression equation for the first person will be as follows:

$$
98315.97 = \alpha_1 + \beta_1 \cdot 16 + \varepsilon
$$

As we are attempting to estimate the $\hat \alpha$ and $\hat \beta$ that best fit everyone in the above dataset, $y$ and $x$ will be an array of values. Note that there is an implicit array of 1s right after $\alpha$. We will now define two arrays: one for our outcome variable and the other for the dependent variables: the array of 1s and the number of years of schooling.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nlsy_79.show(5)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
outcomes = nlsy_79.column("earnings_in_2000")
independent_variable = nlsy_79.column("HGC_Age28")

SD_y = outcomes.std()
SD_x = independent_variable.std()
mean_y = outcomes.mean()
mean_x = independent_variable.mean()
outcomes_s = (outcomes - mean_y) / SD_y
independent_variable_s = (independent_variable - mean_x) / SD_x
r = (1 / len(outcomes)) * sum(outcomes_s * independent_variable_s)

beta = r * SD_y / SD_x
alpha = mean_y - beta * mean_x
print("alpha:", alpha, "beta:", beta)

```
</div>

</div>



A $\beta$ of $6949$ implies that we expect an increase of \\$6949 in earnings for each additional year of schooling a person has. We now have everything we need to plot our regression line.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

predictions = np.array([alpha + beta * x for x in independent_variable])
plt.figure(figsize=(9,6))
plt.scatter(independent_variable, outcomes)
plt.plot(independent_variable, predictions)
plt.xlabel("Years of Schooling")
plt.ylabel("Income")
plt.title("Income vs. Years of Schooling");

```
</div>

</div>



Note that $\alpha$ in our calculations is negative. The literal interpretation of this is that a person with no years of schooling earns a negative income, which doesn't make sense. This is a consequence of the ranges of our data. Notice that the minimum value for years of schooling is virtually 8, as almost no one has fewer than 8 years of schooling. Therefore, we will never expect someone to have 0 years of schooling, and the negative intercept is not of much concern. If we do expect people to have 0 years of schooling, then our model is not good and we need to refine it. Negative intercepts (and therefore negative predictions) appearing in contexts where they don't make sense is common in cases like this where the range of x values starts somewhere well above 0. Thus one needs to be careful when interpreting results of regression; intuitive understanding of the underlying economic concepts is important.



Also note the fact that we need an intercept term ($\alpha$), even if its value is negative. If we were to exclude the intercept term, the regression line would have to go through the point $(0, 0)$, which would restrict ourselves when we construct the line, and therefore generate a line that will necessarily have error greater than or equal to the minimum possible error, which means it is not a best-fit line.



## Multivariable Regression



So far we have been operating under a large limitation: we are only using one feature, years of schooling, as our explanatory variable! Intuitively, using more than one feature will allow us to provide more explanatory power to the predicted value. Suppose we want to predict future earnings - it would make sense that both years of schooling and some measure of intelligence could both possibly contribute to one's earnings. A multi-variable model is useful here.

Visually, the multiple regression model is very similar to a single-variable regression model. The only difference is the additional number of explanatory variables. The following is an example of a multiple variable regression model using two features:

$$
y = \alpha + \beta_{1} \cdot x_{1} + \beta_{2} \cdot x_{2} + \varepsilon
$$

$\beta_{1}$ is the slope coefficient on $x_{1}$, and $\beta_{2}$ is the slope coefficient on $x_{2}$. You can interpret each coefficient as the expected marginal change in $y$ resulting from a 1 unit change in the corresponding regressor, holding all else constant.

How is this different from doing two single-variable regressions? Let's go through a hypothetical example. Suppose we regress earnings on years of schooling, and generate a coefficient of $5000$, meaning for each additional year of schooling, we expect annual earnings to increase by \\$5000. Then, suppose we regress earnings on some measure of intelligence, like AFQT, and we generate a coefficient of $400$, meaning that for each additional point on the AFQT scale we expect a rise in earnings of \\$400 annually. Does this mean that if we do a multi-variate regression, with years of schooling as $x_1$ and intelligence as $x_2$, we will get a $\beta_1$ of $5000$ and a $\beta_2$ of $400$? Not necessarily.

To find out why, think about the relation between years of schooling and education. If I tell you that someone has 20 years of schooling, you can probably make some reasonable conclusions about their intelligence, and vice versa, if I tell you that someone is particularly intelligent, you can probably assume they likely have more years of schooling. Knowing this, return to the regression of earnings on years of schooling. The coefficient of $5000$ means that for a 1 year increase in schooling, we expect a \\$5000 increase in annual earnings. However, we have also just observed that a 1 year increase in schooling tends to be associated with a small increase in intelligence as well. Therefore, when we say "for a 1 year increase in schooling..." implicit in this is also an increase in intelligence, and the coefficient of $5000$ reflects the effect of schooling on earnings *as well as* the effects of intelligence that accompany a rise in schooling.

When we do multi-variable regression, the coefficients that the program outputs reflect the expected effect of a change in one variable *keeping all other variables constant*. So were we to do multi-variable regression of earnings on years of schooling and intelligence, we would likely not get coefficients of $5000$ and $400$, respectively. Rather, the coefficients would likely be less than $5000$ and $400$, as these two coefficients include multiple effects, as we saw earlier. If we want to observe just the effect of years of schooling on earnings, without the associated change in intelligence, we can expect an effect of less than \\$5000.



## Omitted Variable Bias



Notice that in the above section we encountered a situation in which one feature affected another. In other words (at the risk of adding some confusion to terminology) two independent variables were not independent of eachother. We conclused above that the coefficient generated by a regression of earnings on years of schooling was a somewhat misleading figure, as it does not measure *just* the expected change in earnings for a change in schooling, but also the associated change in intelligence one would expect from people with increased schooling. This concept of a regression coefficient including the effects of multiple variables, when we do not explicitly measure and regress on these variables, is called *omitted variable bias*.

When we did a multiple-variable regression including both years of schooling and AFQT as independent variables, we generated two coefficients that measured the exepcted change in earnings for a change in either of the variables, *accounding for the other*. In other words we found the expected effect of one variable while keeping the other constant. We have accounted for omitted variable bias by generating coefficients for schooling and AFQT that do not include the hidden effects of eachother. Because of this, we hypothesized that the new coefficient for schooling should be less than than the coefficient in the single-variable case.

Does this mean that we have created the prefect model? Of course not. There are many other factors that can affect one's future earnings, and it seems reasonable to assume that some of these factors can also interact with years of schooling and AFQT. Although we have addressed the issue of omitted variable bias between schooling and AFQT score, we have not exhaustively accounted for all OVB, and indeed, it is somewhat of a challenge (if not impossible) to control for all possible OVB. The job of the econometrician is somewhat of a qualitative one as well as quantitative, in that it requires a certain amount of convincing and persuasion that one's model is good enough and does not contain significant OVB. Doing this successfully requires solid economic intuition.



## The `statsmodels` Package for Regression



Statsmodels is a popular Python package used to create and analyze various statistical models. To create a linear regression model in statsmodels, we use the following code in general:

```X = data.select(features)```


```Y = data.select(target) # Separate features (independent variables) and target (outcome variable)```

```model = sm.OLS(Y, X) # Initialize the OLS regression model```


```result = model.fit() # Fit the regression model and save it to a variable```


`print(result.summary()) # Print a summary of results`

*You must manually add a constant column of all 1's to your independent features. Statsmodels will not do this for you and if you fail to do this you will perform a regression without an intercept alpha term.*



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import numpy as np
import statsmodels.api as sm

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
independent_variable = sm.add_constant(independent_variable)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
model = sm.OLS(outcomes, independent_variable)
result = model.fit()
result.summary()

```
</div>

</div>



Notice that the package gives the same values for $\alpha$ and $\beta$ that we calculated earlier. Now let's examine what happens when we regress on years of schooling and AFQT.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
independent_variables = nlsy_79.select(["HGC_Age28", "AFQT"])
independent_variables = sm.add_constant(independent_variables.values)

model2 = sm.OLS(outcomes, independent_variables)
result2 = model2.fit()
result2.summary()

```
</div>

</div>



Just as we theorized, the coefficient for years of schooling has decreased when we controlled for AFQT. Now we can see that a unit rise in years of schooling is associated with an increase of \\$3695 in annual income, *holding AFQT constant*. It seems that increased schooling doesn't have nearly as large of an effect as we calculated previously.



### Interpreting Single-Variable Regression Results



The `summary()` method outputs a detailed description of various relevant results from our regression, including number of observations, the fitted $\beta$ coefficients, and the value of $\alpha$. The tabular results are formatted similarly to regression summaries in other popular languages in econometrics such as STATA.

For the purposes of this lab, we will focus on the `coef` column. Here are the interpretations of each value:

- `const`: $\alpha$, the OLS intercept term
- `x1`: The OLS value of $\beta_1$
- `x2`: The OLS value of $\beta_2$



## Categorical and Dummy Variables



Perhaps one useful indicator to predict earnings is an individual's gender. Historically, men have earned more than women, so incorporating gender into our regression may be helpful as an explanatory variable in predicting earnings.

But how would we encode this into our model? After all, being male or female is not a number, unlike years of schooling.

So far, we assume that the inputs to our regression model were continuous values (aka numbers). However, not all data is continuous and thus cannot be directly inputted into a regression model. Categorical variables are a common case of this phenomenon. 

Categorical variables are not necessarily binary, like gender. Another example of a categorical variable is a person's race - we could have any arbitrary amount of race categories or subgroups depending on our dataset.

To translate any categorical variable to continuous inputs to our regression model, we convert them into dummy variables - binary, numeric variables that represent subgroups in categorical variables. Thus, each subgroup is designated as either 0 or 1, indicating whether the subgroup can be attributed to a particular observation or not.

Hence, to do dummy encoding for gender, we would create a variable for each category, or each gender in our case. When the unit is male, the variable for male would be 1 and the variable for female would be 0. Our regression would follow the form:
$$y = \alpha + \beta_1x_{\text{education}} + \beta_2x_{\text{male}} + \beta_3x_{\text{female}}$$

Notably, $\beta_2-\beta_3$ would be the difference in log earnings that is associated with being male rather than female.



## OPTIONAL READING: Reading Economics Papers



In upper division economics courses, you'll often read economics papers that utilize ordinary least squares to conduct regression. Now that we have familiarized ourselves with multi-variate regression, let's familiarize ourselves with reading the results of economics papers!

Let's consider an existing empirical study conducted by David Card, a professor at UC Berkeley, that regresses income on education:

![](https://i.imgur.com/FPLII4s.png)

Every column here is from a different regression: the first column predicts the log hourly earnings from years of education, the fifth column predicts the log annual earnings from years of education, and so on. For now, let's focus on the first column, which states the linear regression as follows: 
$$
\ln{(\text{hourly earnings})_i} = \alpha + \beta \cdot (\text{years of schooling})_i + \varepsilon_i
$$
From the table, the education coefficient is 0.100, with a (0.001) underneath it. This means that our $\beta$ value is equal to 0.100. What does the (0.001) mean? It is the standard error: which is essentially a measure of our uncertainty. From Data 8, the standard error is most similar to the standard deviation of sample means, which is a measure of the spread in the population mean. Similarly, the the standard error here is a measure of the spread in the population coefficient. We can use the standard error to construct a confidence interval of the actual coefficient: a 95% confidence interval is between 2 standard errors above and below the reported value.

The effects of schooling on income is captured by the education coefficient term: 0.100. This means that an increase in 1 unit (year) of education is correlated with a log hourly earnings by 0.1. This approximately corresponds to a 10% increase in wages per year of schooling.



 

