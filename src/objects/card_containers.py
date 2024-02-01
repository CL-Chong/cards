import random


class Card:
    """
    Constructor: Card(name): tuple[str] -> Card

    Attributes:
    name: tuple
        a tuple of strings identifying the card
    _hidden: bool, default False
        if True, hides card and prints |X| when __repr__ is called

    Methods:
    hidden: -> bool
        returns self._hidden
    hide: -> self
        sets _hidden to False in-place and return self
    reveal: -> self
        sets _hidden to True in-place and return self

    """

    def __init__(self, name: tuple):
        self.name = name
        self._hidden = False

    def __repr__(self) -> str:
        if self._hidden:
            return "|X|"
        rep = "|"
        for s in self.name:
            rep += s
        rep += "|"
        return rep

    def __eq__(self, other):
        return self.name == other.name

    def hidden(self):
        return self._hidden

    def hide(self):
        self._hidden = True
        return self

    def reveal(self):
        self._hidden = False
        return self


class Hand:
    """container class for Card. Supports iteration and indexing.
    Constructor: Hand(player): str -> Hand
        constructs an empty hand with the player's name
    Alternative constructor: Hand.from_list(player, card_list): str, list[Card] -> Hand
        constructs a hand with the player's name and card_list as hand

    Attributes:
    hand: list[Card]
        a list containing the cards
    player: str
        string containing name of the hand

    Methods:
    size: -> int
        returns the size of the hand
    shuffle(rng): random.Random ->
        shuffles the hand in-place using rng
    sort(key): function(Card -> int) ->
        sort the hand using the key provided
    draw(card): Card ->
        appends the card to the right of the hand
    deal: -> Card
        removes and returns the rightmost card of the hand
    play(card): Card -> Card
        removes and returns the input card from the hand
        raises ValueError if the card is not in the hand
    hidden: -> list[bool]
        returns list containing card.hidden() for card in hand
    hide: -> Hand
        applies card.hide() for card in hand and return self
    reveal: -> Hand
        applies card.reveal() for card in hand and return self

    """

    def __init__(self, player: str):
        self.hand = []
        self.player = player

    def __repr__(self) -> str:
        return self.hand.__repr__()

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        if self._idx == len(self.hand):
            raise StopIteration
        card_idx = self.hand[self._idx]
        self._idx += 1
        return card_idx

    def __getitem__(self, idx):
        if isinstance(idx, int):
            return self.hand[idx]
        else:
            return Hand.from_list(self.player, self.hand[idx])

    @classmethod
    def from_list(cls, player: str, card_list: list):
        new_hand = Hand(player)
        new_hand.hand = card_list
        return new_hand

    def size(self):
        return len(self.hand)

    def shuffle(self, rng: random.Random):
        rng.shuffle(self.hand)
        return

    def sort(self, key):
        self.hand.sort(key=key)
        return

    def draw(self, card: Card):
        self.hand.append(card)
        return

    def deal(self):
        if len(self.hand) == 0:
            raise ValueError(f"No cards in {self.player}'s Hand")
        card_out = self.hand.pop()
        return card_out

    def play(self, card: Card):
        try:
            self.hand.remove(card)
            return card
        except ValueError:
            print(f"No {card} in {self.player}'s Hand")

    def hidden(self) -> list:
        return [card.hidden() for card in self.hand]

    def hide(self):
        for card in self.hand:
            card.hide()
        return self

    def reveal(self):
        for card in self.hand:
            card.reveal()
        return self
