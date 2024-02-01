import random


class Card:
    def __init__(self, name: tuple):
        self.name = name

    def __repr__(self) -> str:
        rep = "|"
        for s in self.name:
            rep += s
        rep += "|"
        return rep

    def __eq__(self, other):
        return self.name == other.name


class Hand:
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

    @classmethod
    def from_list(self, player: str, card_list: list):
        new_hand = Hand(player)
        new_hand.hand = card_list
        return new_hand

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
            raise IndexError(f"No cards in {self.player}'s Hand")
        cardOut = self.hand.pop()
        return cardOut

    def play(self, card: Card):
        try:
            self.hand.remove(card)
            return card
        except ValueError:
            print(f"No {card} in {self.player}'s Hand")
