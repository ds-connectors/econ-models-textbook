# Iterated Prisoner's Dilemma Players

This section provides the class definitions for the strategies used for the iterated prisoner's dilemma.

import functools
import numpy as np
from datascience import *
most_common = lambda a: a[np.argmax([np.count_nonzero(np.equal(i, a)) for i in a])]

We create these classes using the `create_player_class` function which creates the class and returns it for us using a provided player name and play method (a method which takes players and returns `True` if the player defects and `False` if they cooperate. The classes include:

* an `__init__` method for creating instances and instance variables
* a `play` method that takes an opponent and returns the player's decision at a single turn
* a `reset_history` method that clears the player's history for use between matches
* an `update_history` method that adds the player's last move to their history
* a `__repr__` method that returns the player's name
* a `__hash__` method that returns an integer [hash](https://en.wikipedia.org/wiki/Hash_function) of the player
* an `__eq__` method that defines the comparison of a player using `==`
* an `__lt__` method that defines the comparison of a player using `<`

A couple of notes on the class:

* The instance variable `last_move` is used to store the player's last move so that it can later be appended to the history using `update_history`. This helps define strategies that rely on using the histories for calculations, so we don't need to take into account whether the player is player 1 or player 2.
* The [decorator](https://wiki.python.org/moin/PythonDecorators) `functools.total_ordering` defines all comparison dunders not defined (`__neq__`, `__gt__`, `__gtq__`, and `__lte__`) in the class for us using the two provided (`__eq__` and `__lt__`).
* We define `__hash__` so that the players are **hashable**, allowing them to be used in dictionaries.

def create_player_class(player_name, play_method):
    @functools.total_ordering
    class Player:
        def __init__(self, p=0.5):
            self.history = make_array(True)[:0]
            assert len(self.history) == 0
            self.prob = p
            self.name = player_name
            self.last_move = None
        
        def play(self, opponent):
            """Returns True if player defects, False otherwise"""
            defect = play_method(self, opponent)
            self.last_move = defect
            return defect
        
        def reset_history(self):
            self.history = make_array()
        
        def update_history(self):
            assert self.last_move is not None
            self.history = np.append(self.history, self.last_move)
            self.last_move = None
        
        def __repr__(self):
            if player_name == "Random":
                return player_name + "({})".format(self.prob)
            return player_name
        
        def __hash__(self):
            return hash(self.name)
        
        def __eq__(self, other):
            return self.name == other.name
        
        def __lt__(self, other):
            return self.name < other.name
    
    return Player

## Defector

def defector_play(self, opponent):
    return True

Defector = create_player_class("Defector", defector_play)

## Cooperator

def cooperator_play(self, opponent):
    return False

Cooperator = create_player_class("Cooperator", cooperator_play)

## Random

def random_play(self, opponent):
    return np.random.random() < self.prob

Random = create_player_class("Random", random_play)

## Alternator

def alternator_play(self, opponent):
    if len(self.history) > 0:
        return not self.history.item(-1)
    else:
        return False

Alternator = create_player_class("Alternator", alternator_play)

## Backstabber

def backstabber_play(self, opponent):
    return np.sum(opponent.history) > 3

Backstabber = create_player_class("Backstabber", backstabber_play)

## Bully

def bully_play(self, opponent):
    if len(self.history) == 0:
        return True
    return not opponent.history.item(-1)

Bully = create_player_class("Bully", bully_play)

## Desperate

def desperate_play(self, opponent):
    return np.sum(np.logical_and(self.history, opponent.history)) < 1

Desperate = create_player_class("Desperate", desperate_play)

## Fool-Me-Once

def fool_me_once_play(self, opponent):
    return np.sum(opponent.history) > 1

FoolMeOnce = create_player_class("FoolMeOnce", fool_me_once_play)

## Forgiver

def forgiver_play(self, opponent):
    if len(self.history) == 0:
        return False
    return np.sum(opponent.history) / len(opponent.history) > 0.1

Forgiver = create_player_class("Forgiver", forgiver_play)

## Once-Bitten

def once_bitten_play(self, opponent):
    if not hasattr(self, "defects_left"):
        self.defects_left = 0
    if self.defects_left > 0:
        self.defects_left -= 1
        return True
    if len(opponent.history) >= 2:
        if opponent.history[-1] and opponent.history[-2]:
            self.defects_left = 9
            return True
    return False

OnceBitten = create_player_class("OnceBitten", once_bitten_play)

## Grudger

def grudger_play(self, opponent):
    return np.sum(opponent.history) > 0

Grudger = create_player_class("Grudger", grudger_play)

 