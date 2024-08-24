from dataclasses import dataclass, field
from typing import List

from .card import Card, Suit, Value


@dataclass
class Hand:
    cards: List[Card] = field(default_factory=list)
    n_aces: int = field(init=False, default=0)

    def __str__(self) -> str:
        return ", ".join([str(card) for card in self.cards])
    
    @property
    def usable_ace(self) -> bool:
        """
        Returns a boolean indicating whether the hand has a usable ace.

        A usable ace is an Ace card that can be counted as either 1 or 11 to improve the total value of the hand.
        This property checks if the number of Ace cards in the hand is greater than 0 and if the total value of the hand without considering the Ace cards is less than or equal to 10.

        Returns:
            bool: True if the hand has a usable ace, False otherwise.
        """
        return self.n_aces > 0 and self.total_without_ace <= 10
    
    @property
    def total_without_ace(self) -> int:
        """
        Returns the total value of the hand without considering the value of any Ace cards.
        
        :return: An integer representing the total value of the hand without considering the value of any Ace cards.
        :rtype: int
        """
        return sum([card.value.value[0] for card in self.cards if card.value.name != "ACE"])
    
    @property
    def total(self) -> int:
        """
        Calculates the total value of the hand, taking into account the usable ace.

        Returns:
            int: The total value of the hand.
        """
        ace_sum = (self.n_aces - 1) * 1
        ace_sum += 11 if self.usable_ace else 1
        return self.total_without_ace + ace_sum
    
    def add_card(self, card: Card):
        """
        Adds a card to the hand and updates the number of Aces if necessary.

        Parameters:
            card (Card): The card to be added to the hand.

        Returns:
            Card: The added card.
        """
        self.cards.append(card)
        
        if card.value.name == "ACE":
            self.n_aces += 1
        
        return card