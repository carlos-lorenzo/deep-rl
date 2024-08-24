from .hand import Hand
from .deck import Deck

class BasePlayer:
    def __init__(self) -> None:
        self.hand = Hand()
        self.playing: bool = True
    
    
    def __hash__(self) -> int:
        return id(self)
    
    def hit(self, deck: Deck) -> None:
        self.hand.add_card(deck.draw())
        
        self.playing = self.hand.total < 21
            
        
    def stand(self) -> None:
        self.playing = False
        
    def clear_hand(self) -> None:
        self.hand = Hand()
    
    def display_hand(self) -> None:
        print(f"{self.hand} - Total: {self.hand.total}")
        
        
class Dealer(BasePlayer):
    def __init__(self) -> None:
        super().__init__()
    
    @property
    def partial_total(self) -> int:
        """
        Returns the value of the first card in the player's hand.

        :return: An integer representing the value of the first card in the player's hand.
        :rtype: int
        """
        return self.hand.cards[0].value.value[0]
    
        
    def play(self, deck: Deck) -> None:
        """
        Plays the game by hitting cards until the total value of the hand is 17 or higher.
        
        Args:
            deck (Deck): The deck of cards from which to draw the cards.
        
        Returns:
            None: This function does not return anything.
        """
        while self.hand.total < 17:
            self.hit(deck)
        self.stand()
    
    def display_hand_partial(self) -> None:
        """
        Display the first card in the player's hand along with its partial total.

        This function prints the first card in the player's hand along with its partial total.
        The partial total is calculated by accessing the value of the first card in the hand.

        Parameters:
            self (Player): The player object.

        Returns:
            None: This function does not return anything.
        """
        print(f"{self.hand.cards[0]} - Total: +{self.partial_total}")
        

class Player(BasePlayer):
    def __init__(self) -> None:
        super().__init__()
        self.actions_taken = []
    
    def hit(self, deck: Deck, save_action: bool = True) -> None:
        """
        Adds a card from the given deck to the player's hand and updates the playing status.

        Args:
            deck (Deck): The deck from which to draw the card.
            save_action (bool, optional): Whether to save the action taken. Defaults to True.

        Returns:
            None: This function does not return anything.

        This function adds a card from the given deck to the player's hand and updates the playing status.
        It first stores the initial total and usable ace of the player's hand. Then, it draws a card from the deck
        and adds it to the player's hand. After that, it checks if the total of the player's hand is less than 21,
        and updates the playing status accordingly. If save_action is True, it appends a dictionary containing the
        action, initial total, usable ace, new total, and reward to the actions_taken list.

        Note: The actions_taken list is expected to be a list of dictionaries, where each dictionary represents an
        action taken by the player. The dictionary should have the following keys: "action", "total", "usable_ace",
        "new_total", and "reward". The "action" key should have the value 1 to indicate that a card was hit. The
        "total" key should have the value of the initial total of the player's hand. The "usable_ace" key should have
        the value of the usable ace status of the player's hand. The "new_total" key should have the value of the
        total of the player's hand after the card was hit. The "reward" key should have the value of 0, as it is not
        known at this point.
        """
        
        initial_total = self.hand.total
        usable_ace = self.hand.usable_ace
        self.hand.add_card(deck.draw())
        
        self.playing = self.hand.total < 21
        
        if save_action:
            self.actions_taken.append({
                "action": 1,
                "total": initial_total,
                "usable_ace": usable_ace,
                "new_total": self.hand.total,
                "reward": 0
            })
        
    def stand(self) -> None:
        """
        Sets the playing status of the player to False, indicating that they are no longer playing.
        Appends a dictionary to the actions_taken list, representing the action of standing. The dictionary has the following keys:
        - "action": an integer value of 0 to indicate that the player is standing.
        - "total": the total value of the player's hand before standing.
        - "usable_ace": a boolean value indicating whether the player's hand has a usable ace.
        - "new_total": the same value as "total", as the player's hand does not change after standing.
        - "reward": an integer value of 0, as the reward is not known at this point.
        
        This function does not return anything.
        """
        self.playing = False
        
        self.actions_taken.append({
            "action": 0,
            "total": self.hand.total,
            "usable_ace": self.hand.usable_ace,
            "new_total": self.hand.total,
            "reward": 0
        })
        
    def play(self, deck: Deck, action: int) -> None:
        """
        Play a card from the deck based on the given action.

        Parameters:
            deck (Deck): The deck from which to draw the card.
            action (int): The action to perform. Must be either 1 to hit or 0 to stand.

        Raises:
            ValueError: If the action is not 1 or 0.

        This function plays a card from the given deck based on the given action. If the action is 1, it calls the `hit`
        method to add a card to the player's hand. If the action is 0, it calls the `stand` method to set the playing
        status of the player to False. If the action is neither 1 nor 0, it raises a `ValueError`.

        Note:
            The `hit` method adds a card from the deck to the player's hand and updates the playing status. The `stand`
            method sets the playing status of the player to False.
        """
        if action == 1:
            self.hit(deck)
        elif action == 0:
            self.stand()
        else:
            raise ValueError("Invalid action")
        
    