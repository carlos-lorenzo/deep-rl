from dataclasses import dataclass, field
from typing import List

from .card import Card, Suit, Value, values

@dataclass
class Deck:
    n_full_decks: int = field(default=6)
    cards: List[Card] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        for suit in Suit:
            for value in values.values():
                
                self.cards.append(Card(suit, value))
        self.shuffle()
        
    def __len__(self) -> int:
        return len(self.cards)
    
    def reset(self):
        """
        Resets the deck by clearing the list of cards and reinitializing the deck.

        This method clears the `cards` list by setting it to an empty list. It then calls the `__post_init__` method to reinitialize the deck by populating the `cards` list with new cards.

        Parameters:
            None

        Returns:
            None
        """
        self.cards = []
        self.__post_init__()
    
    def shuffle(self):
        """
        Shuffles the deck of cards.

        This method uses the `random.shuffle` function from the `random` module to shuffle the `cards` list in place.

        Parameters:
            None

        Returns:
            None
        """
        import random
        random.shuffle(self.cards)
    
    def draw(self) -> Card:
        """
        Draws and returns a card from the deck.

        Returns:
            Card: The card that was drawn from the deck.
        """
        return self.cards.pop()