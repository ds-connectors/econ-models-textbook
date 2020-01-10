---
interact_link: content/finance/finance.ipynb
kernel_name: python3
has_widgets: false
title: 'Finance and Time Series Data'
prev_page:
  url: /topic-intros/finance.html
  title: 'Finance and Time Series Data'
next_page:
  url: /topic-intros/inequality.html
  title: 'Inequality and Tax Rates'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<table style="width: 100%;">
    <tr style="background-color: transparent;"><td>
        <img src="https://d8a-88.github.io/econ-fa19/assets/images/blue_text.png" width="250px" style="margin-left: 0;" />
    </td><td>
        <p style="text-align: right; font-size: 12pt;"><strong>Economic Models</strong>, Fall 2019<br>
            Dr. Eric Van Dusen</p></td></tr>
</table>



# Lab 9: Financial Economics -- Fixed-Income Securities



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sympy
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display
import numpy as np
import warnings
warnings.filterwarnings('ignore')
plt.style.use("seaborn-muted")

```
</div>

</div>



This notebook will aim to introduce Fixed Income securities to you, as an introduction to the larger field of Financial Economics. These are assets that pay a fixed amount of money at regular intervals according to a prescribed interest rate. We will focus on what interest means and how money changes value over time. From this, we will proceed into a discussion of the different examples of fixed-income securities: Annuities, Perpetuities, Forward Start Perpetuities, Zero Coupon Bonds and Bonds themselves. Along the way, we will learn about yield, price, the yield curve, and the different measures of risk that go into selecting which fixed income security to enter. 



## The Time Value of Money



An important concept that some might argue is the basis for most of finance is the *time value of money*: money now is worth more than money in the future. This makes sense; you would rather have $\$$100 now than later. But what if I owed you money and I really wanted to postpone the payment? In order to compensate you for your bias toward having money as soon as possible, I would need to pay more than I owed. Otherwise, you might not tolerate a delayed payment. This idea of an extra payment to address time concerns is called *interest*. There is also a dimension of risk, as well. If you had reason to doubt my ability to repay you in the future, you might charge me more interest to compensate for this risk.



## Interest



Interest is at the heart of fixed income securities and financial economics in general. We are familiar with the basic transaction in the context of a bank account: the principal (you, the investor) giving a certain amount of money to a financial institution, and them compensating you for allowing them to use your money to invest in other assets. The money they pay you for keeping your money is interest, and is normally quantified as a percentage of what you deposit with them - an interest rate. Thus, for each dollar deposited into the institution, the principal will receive 1(1+r) where r is the interest rate quoted by said institution. Note that r takes the form of 0.05, for instance, and not 5%.

Fixed income securities work in a similar way. However, instead of depositing money into a bank, you decide to purchase an asset that will pay you a fixed amount of money at regular intervals, before returning the initial amount at a given time. The amount of money paid out is based on interest. Thus in both ways, bank deposits and fixed income securities, your money will grow by some amount.




The next question becomes how often is interest paid out - monthly, quarterly, yearly or continuously? This is where the concept of compounding comes in. We are able to determine how much $\$$1 will generate in t years, when compounding n times per year at an interest rate of r.

$$
\text{Value} = 1 \left (1 + \dfrac{r}{n} \right)^{nt}
$$

Take a look at the table below for an example.



|-| Bank 1: 5% annually  | Bank 2: 5% semi-annually      |
| --- | --- | --- |
| January 2016         | $\$100 $                | $\$100 $                         |
| July 2016            | -                    | $\$100 \left ( 1 + \dfrac{0.05}{2} \right )$ = $\$$102.50    |
| January 2017         | $\$$100(1.05) = $\$$105    | $\$102.50 \left ( 1+\dfrac{0.05}{2} \right )$ = $\$$105.0625 |
| July 2017            | -                    | $\$ 105.0625 \left ( 1+ \dfrac{0.05}{2} \right )$ = $\$$107.69 |
| January 2018         | $\$$105(1.05) = $\$$110.25 | $\$ 107.69 \left ( 1+ \dfrac{0.05}{2} \right )$ = $\$$110.38   |
| Total Percent Change | 10.25%               | 10.38%                        |



Notice that instead of a $5\%\cdot2$ = $10\%$ increase, you end up receiving a 10.25% or 10.38% increase depending on the rate of compounding. This is because the interest you received in the first compounding period (in bank 1’s case, a year, in bank 2’s case, half a year) is added onto your initial deposit, and this new deposit is used for calculating interest in the next period. This is the value of compounding - the growth rate is applied at an exponential rate. Thus, even a small amount of $\$$1 can grow quickly under any kind of interest rate compounding.





## The Rule of 70



We can reorganize the equation above to find out how long it will take to double your initial deposit. Let $n = 1$, and $r = 0.01$.

$$
20 = 10 \left (1 + 0.01 \right )^{t} \\
2 = \left (1 + 0.01 \right )^{t} \\
\ln(2) = t \ln(1 + 0.01) \\
0.693147 = 0.00995t \\
t \approx 69.66 \approx 70
$$

A good approximation of this is the rule of 70. This states that at a 1% 
interest rate, it will take 70 compounding periods to double one’s money. So if the rate is 1% and the compounding period is one year, it will roughly take 70 years to double the initial deposit. If the rate is 2%, it will roughly take 35 years. This is only an approximation, but a useful one for quick use.



## Present Value, Future Value, and Discount Factor



An important related concept is the idea of present and future value. We have already discussed future value above. A $\$$100 deposit at bank 1 above has a future value of $\$$110.25 after 2 years. Conversely, an important question frequently asked in finance is given an amount of money in the future, what is its fair value today? In this example, what is the present value of $\$$110.25 at bank 1 2 years in the future? Well, from the table above, $\$$100! This idea of present value is essential to the pricing of assets. What is the fair price that one should pay today for an asset that has payments in the future? It is the present value of all future payments the asset gives. The formulae for future and present value should look related.

$$
\text{FV} = 1 \left (1 + \dfrac{r}{n} \right)^{nt}
$$


$$
\text{PV} = \dfrac{1}{\left (1 + \dfrac{r}{n} \right ) ^{nt}}
$$

The formula for present value is technically a *discount factor* in the format it is in currently. It discounts any future price into a fair present-day price. It must be multiplied by face value to get the present price of the bond in our example.



## Fixed Income Securities



A fixed income security works similarly to a bank deposit, but with some slight differences. First, these securities are assets, and can be traded to someone else like any other asset, in contrast to a bank account, which cannot usually be transferred to someone else. Also, these securities represent an obligation to the owners of the assets from the company or organization that issues the asset. Unlike dividends on earnings, which a company can choose to whether or not to pay and how much, an issuer of these securities is legally obligated to pay them out according to the schedule agreed upon.

Now we will go into examples of fixed-income securities. They have a few components:
- Price: The actual amount investors pay to own the asset - the present value of all future expected payments.
- Coupon: The fixed-amount payments. You may be familiar with bonds that pay some money each quarter or year. This is the coupon.
- Face Value: The dollar value of the security itself - what gets paid out at maturity. So if you own a 5-year bond of face value $\$$100, after 5 years you will receive $\$$100.
- Maturity: The length of time the security is active for. In the above example, the maturity would be 5 years.
- Coupon Rate: The percent of the security’s face value that is paid out as coupons. So if the face value is $\$$100 and the coupon rate is 5%, then the security pays coupons of $\$$5 every so often.
- Yield: The annualized rate of return of the security, considering all of the factors above. Do not confuse this with coupon rate; these are different things. Yield is a feature of the market, and is not something the investor typically has much control over. It is related to interest rates.

As we mentioned before, these are assets where the investor purchases them at a certain price, and gets regular fixed-amount payments and/or their original investment at the securities’ maturity. The key idea with fixed-income securities is how they are priced. We are able to calculate the sum total of payments the investor will receive over the time when the security is active. 




## Yield and the Zero-Coupon Bond



Let’s begin our discussion with *zero-coupon bonds*. A zero-coupon bond is a very simple bond in which you pay an amount to own the bond, and after a specified period of time, you receive an amount of money in return. Thus, when the investor purchases the bond at the current time, they will just pay the present value of the zero-coupon bond’s face value. The question now becomes: what should the yield be?

As a simplification, we will assume that the yield curve is flat. What this means is that the annualized yield for a bond or other fixed-income security is the same regardless of the timespan in which the asset pays. Thus, the rate of return at a given time t is just one universal, constant yield. If we know that we are to receive the face value at time t, then we can say the future value is the face value. As the price of a security is the present value of all future expected cash flows, and our only cash flow is the return of the face value, then the price we pay today would just be the present value of the face value, discounted at the current yield. Thus you can interpret the yield as an annualized rate of return that is a property of the market and changes over time, much like interest rates at a bank.

Let's say we have a 1-year bond of face value $\$$100, with no coupons. And let's say the yield for this type of bond in the market is currently 5%. How much should the bond cost?

$$
\text{PV} = \dfrac{1}{\left (1 + \dfrac{r}{n} \right ) ^{nt}} \\
\text{Price} = \dfrac{\$100}{\left( 1 + 0.05 \right)} \\
\text{Price} \approx \\$95.24
$$

So we would expect this bond to be trading at about $\$$95.24.

Now let's discuss other types of fixed income.



## Perpetuity



A perpetuity is a security that pays a fixed coupon for an infinite time period. As it is active for an infinite time period, the initial investment is never repaid, in contrast to a bond which repays the face value at maturity. Once again, we need to find the present value of all future expected cash flows. Let’s first focus on finding how much we will earn - in other words, we need to find the sum of an infinite series, then discount that to present values.

To keep our notation simple let's let $n = 1$, so we have annual compounting.

$$
\text{Price} = \sum^{\infty}_{i=1} \dfrac{C}{\left( 1 + Y \right)^i}
$$

where $C$ is the annual coupon that the perpetuity pays. Note that

$$
\sum^{\infty}_{i=0} x^i = \dfrac{1}{1-x}
$$

for $\lvert x \rvert < 1$, so

$$
\text{Price} = \dfrac{C}{Y}
$$

for a perpetuity. The specific algebra to get here is left as an exercise for the reader.



## Forward-Start Perpetuity



From this, we can move to a forward-start perpetuity. As the name suggests, this is just a perpetuity that starts nt periods from now. How could we price this? We have already discussed how to find the price of a perpetuity, so let us just discount that price to present values.

$$
\text{Price} = \dfrac{1}{\left( 1 + Y \right)^t} \dfrac{C}{Y}
$$

where $t$ is the number of periods (years in our case) that the perpetuity is delayed.



## Annuity



The next security we will discuss is the annuity. This is a security that pays out a fixed coupon for nt-periods but does not repay the initial investment at the end. How would we price this? We have already derived the equation for a perpetuity and a forward-start perpetuity. How could we use these securities to create an annuity? How about if we purchase a perpetuity today and sell a forward-start perpetuity nt-periods from now? From present to nt-periods, the perpetuity will be active. We thus receive its coupons for that time period. At nt-periods on, as we have sold a forward-start perpetuity, we must pay out instead of receive coupons at every period. With this in mind, if we own a perpetuity that will pay a coupon forever, and we also have sold a forward-start perpetuity that will pay the same amount as our perpetuity coupon forever, but delayed by some time, then what do we have? We have a portfolio that first pays us a coupon for some time, then once the forward-start perpetuity kicks in, our portfolio has an asset that pays us a coupon, and an asset where we have to pay a coupon. These cancel out and we have effectively constructed an annuity. Our portfolio pays coupons for some time then stops, which is exactly what an annuity does.

$$
\text{Price} = \dfrac{C}{Y} - \dfrac{1}{\left( 1 + Y \right)^t} \dfrac{C}{Y}
$$



## Bonds



This leads us to the bond. This is a security that pays regular (normally fixed-amount) coupons and returns the face value to the investor at its maturity. Using all of the securities we have introduced, how could we construct the formula for a bond’s price?

As the bond is only active for a certain time period, we can treat the cash flows from coupons as an annuity. As for the repayment of the face value at maturity, this is just a zero-coupon bond! Thus, the price of a bond is the sum of an nt-period annuity and a zero-coupon bond.

$$
\text{Price} = \dfrac{C}{Y}\left[ 1 - \dfrac{1}{\left( 1 + Y \right)^t} \right] + \dfrac{F}{\left( 1 + Y \right)^t} \\
\text{Price} = \dfrac{C}{Y} + \dfrac{F - \dfrac{C}{Y}}{\left( 1 + Y \right)^t}
$$

where $F$ is the face value of the bond, which will typically be $\$$100 in our examples and equations, but in reality can be millions of dollars.




## Price vs. Yield: The Yield Curve



One thing to note is the inverse relationship between a bond’s price and its yield. If the price of a bond decreases, its yield increases and vice versa. This is a simple property that arises from our pricing equations for bonds, and not some mystical law of nature. The best example to illustrate this uses a zero-coupon bond. Imagine a 1-year zero-coupon bond that has a face value of $\$$100, meaning it pays $\$$100 1 year from now. What is the present value of this bond, or in other words, what is its price? Well, that depends on the yield. Using annual compounding, if the yield were 10%, the price of the bond would be about $\$$90.91. With 20%, the price would be about $\$$83.33. With 30%, $\$$76.92. Notice this relationship, and how it intuitively makes sense with a zero-coupon bond. If the price of the bond today goes down, then the yield necessarily must increase, as you are essentially making a higher return on your purchase, since you are getting paid $\$$100 after one year no matter what. Similarly, if the yield goes down, the price of the bond must increase, as a decreased yield indicates less return will be made from the bond, which can only happen if the price of the bond increases.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def bond_price(yield_rate):
    return 100 / (1 + yield_rate)
  
yields = [i / 100 for i in range(0, 100)]
prices = [bond_price(yield_rate) for yield_rate in yields]

plt.figure(figsize = [9,6])
plt.plot(yields, prices)
plt.xlabel("Yield")
plt.ylabel("Price")
plt.title("Price vs. Yield for a Simple 1-Year Zero-Coupon Bond w/ $100 Face Value");

```
</div>

</div>



Yield is a bit more nuanced than what we have been discussing so far. We have made the assumption that yield is the same for all bond lengths, meaning that a 1-year bond has the same annual yield as a 20-year bond. In reality this is rarely true. Usually for longer term bonds the yield is higher, again from the time value of money we discussed earlier. Something called the *yield curve* depicts how yield changes with the timeframe of bonds. When our assumption of one prevailing yield holds in real life, the yield curve is said to be flat. We will not worry a great deal about the specific shape of the curve in the lesson or homework, but it is important to know the assumptions we make.

Before we continue, let's gain some more intuition on the meaning of yield. Let's say we have a simple zero-coupon bond with some price $P$ having yield $Y$. How would the price of the bond change if the bond also paid coupons, keeping yield constant? If we draw a conceptual parallel between bond yields and bank interest rates, the bond has to pay a certain yield after one year, in one way or another. In the zero-coupon context, this yield manifests as a difference between the price you paid and the face value received. When the bond pays a coupon, some of this yield manifests as coupon payments. Therefore, in order for the bond to pay the same yield, the bond that pays coupons will have a higher price than the zero-coupon bond, as there is less of a need for that difference in price to account for the yield.



## Dollar Duration and Convexity



Looking at the graph above that ties together price and yield, we can find two important metrics of bonds. The first is called *dollar duration*, which is a measure of how much the price of the bond changes with a change in yield. As yield is not something the bondholder usually controls and is a factor of the financial environment, the way a bond’s price behaves is important to investors, as a bond whose dollar duration is large, meaning its price changes dramatically for a change in yield, may be undesirable to an investor averse to risk. Dollar duration is simply just the negative derivative of the curve at a given point. We make the derivative negative so that the final result is a positive number, as lines tangent to the curve all have negative slope. One step further, *convexity* is a measure of how much the dollar duration changes with a change in yield, and is of course the second derivative of the curve at a given point.

Computationally, it is possible to find the duration by applying a very small change in yield in both the positive and negative direction, finding what the price of the bond would be for these small changes, taking that difference, and dividing by twice the small change in yield. This method of approximating the duration generates the *effective duration*.

$$
- \dfrac{P(Y+dY) - P(Y-dY)}{2dY}
$$



## Conclusion



Today we discussed the time value of money, the concept of interest that arises from this, and the fixed-income assets that utilize the phenomenon of interest. We also discussed the properties of these assets, and how to price them.



 

