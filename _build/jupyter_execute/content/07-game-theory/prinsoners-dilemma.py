# The Iterated Prisoner's Dilemma

from datascience import *
import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
plt.style.use("seaborn-muted")
%matplotlib inline
import functools
import warnings
warnings.simplefilter("ignore")
from ipywidgets import interact, FloatSlider

from players import *

We will study the **iterated prisoner's dilemma**, a game paradigm in which the prisoner's dilemma is played over multiple rounds and in tournaments to determine the best strategy for playing the game. This paradigm was introduced by [Robert Axelrod](https://en.wikipedia.org/wiki/Robert_Axelrod) to use the prisoner's dilemma as a lens through which to study the Cold War during the Cuban Missile Crisis. Axelrod created a tournament out of an iterated prisoner's dilemma and invited theoreticians to write programs that could strategically play the game, and then pitted them one against another in a round-robin-style tournament.

## Strategies

To begin, we'll consider the two most basic strategies for playing this game: the **defector** and the **cooperator**. A defector always defects and a cooperator always cooperates. Because of this, we would expect that the defector would win every round in a match between these two players, because they will always accrue 0 years where the cooperator always accrues 5.

Other strategies for playing this game are summarized in the table below. (Note that we use the shorthand "D" for defect and "C" for cooperate.)

| Name | Description |
|-----|-----|
| `Alternator` | Alternates between C and D |
| `Backstabber` | Forgives first 3 opponent D's then D forever after fourth |
| `Bully` | Starts by defecting and then does the opposite of opponent's previous move |
| `Desperate` | Only cooperates after mutual defection |
| `FoolMeOnce` | Forgives one D then retaliates forever on a second D |
| `Forgiver` | Starts by cooperating however will defect if at any point the opponent has defected more than 10 percent of the time |
| `ForgivingTitForTat` | Starts by cooperating and defects if opponent has defected more than 10% of the time **and** their last move was defection |
| `Grudger` | Starts with C and then D forever on opponent's first D |
| `OnceBitten` | C once on opponent D, but if opponent D's twice in a row defaults to D for 10 turns |
| `TitForTat` | Repeats opponent's previous move |

To see the class definitions for these players, see [this section](player-definitions.ipynb).

## Matches

Our analysis of the prisoner's dilemma hinges on analyzing strategies over multiple rounds. For this reason, we need a way to pit players against each other and find out who has the fewest years accrued. The function `run_match` will run a match of two players with a specified number of turns. If `winner` is `True`, it returns the winner of the match; if `winner` is `False`, it returns a list for each player containing the sequence of years accrued.

run_match(Defector(), Cooperator())

run_match(Defector(), Cooperator(), winner=False)

Let's consider another strategy: randomness. The random player will randomly defect or cooperate. Note that the `Random` constructor takes an optional argument indicating the probability of **defecting** on any given turn which defaults to 0.5. For example, `Random(.25)` defects 25% of the time and `Random(1)` always defects (it's a defector).

np.random.seed(42)

Random().play(None), Random().play(None)

Let's test a few payoffs with our new `Random` player.

np.random.seed(100)

payoff(Defector(), Random()), payoff(Defector(), Random(.75))

## Tournaments

Now that we can pit two players against each other, how do we compare multiple players? We can create a round-robin tournament that runs matches between each pair of players. If the tournament has $n$ players, this will take $\frac{n(n-1)}{2}$ matches:

> Player $i$ must go against $n-i$ players at iteration $i$ (as it will have already played the $i-1$ previous players in previous iterations), so the number of matches is 
$$\begin{aligned}
\sum_{i=1}^{n} (n-i) &= n^2 - \sum_{i=1}^{n} i \\
&= n^2 - \frac{n(n+1)}{2} \\
&= n \left ( \frac{2n}{2} - \frac{n+1}{2} \right ) \\
&= \frac{n(n-1)}{2}
\end{aligned}$$

To run through the tournament, we'll need to iterate through each player and pit them against every other player in a match. To ensure that we don't duplicate matches, we'll loop from 0 to the number of players in the outer loop and loop from the next player to the last player in the inner loop. The function `most_common` returns the value in an array of values that has the largest number of occurrences; it is here used to determine which player won the most times.

players = make_array(Defector(), Cooperator())
winners = make_array()
for i in range(len(players)):
    for j in range(i+1, len(players)):
        winner = run_match(players.item(i), players.item(j))
        winners = np.append(winners, winner)
        
biggest_winner = most_common(winners)
biggest_winner

 