from dataclasses import dataclass
from typing import List
from enum import Enum
from collections import OrderedDict

class Suit(Enum):
    SPADES = 1
    DIAMONDS = 2
    CLUBS = 3
    HEARTS = 4

@dataclass
class Value:
    name: str
    value: List[int]

@dataclass
class Card:
    suit: Suit
    value: Value
    
    def __str__(self) -> None:
        return f"{self.value.name} of {self.suit.name}"
    
    

values = OrderedDict()
values["ACE"] = Value("ACE", [1, 11])
values["TWO"] = Value("TWO", [2])
values["THREE"] = Value("THREE", [3])
values["FOUR"] = Value("FOUR", [4])
values["FIVE"] = Value("FIVE", [5])
values["SIX"] = Value("SIX", [6])
values["SEVEN"] = Value("SEVEN", [7])
values["EIGHT"] = Value("EIGHT", [8])
values["NINE"] = Value("NINE", [9])
values["TEN"] = Value("TEN", [10])
values["JACK"] = Value("JACK", [10])
values["QUEEN"] = Value("QUEEN", [10])
values["KING"] = Value("KING", [10])

