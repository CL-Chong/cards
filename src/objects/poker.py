from objects.card_containers import Card, Hand


class Poker:
    def __init__(self):
        self.suits = ["C", "D", "H", "S"]
        self.numbers = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
            "A",
        ]
        self.special = [("r", "j"), ("b", "j")]
        self.cardlist = [(suit, num) for suit in self.suits for num in self.numbers]

    def make_deck(self, deck_name="deck", jokers=False):
        deck = Hand(deck_name)
        for name in self.cardlist:
            deck.draw(Card(name))
        if jokers:
            for name in self.special:
                deck.draw(Card(name))
        return deck

    def rank_by_suit(self, card: Card):
        if card.name in self.special:
            return len(self.cardlist) + self.special.index(card.name)
        suit, num = card.name
        return self.numbers.index(num) + len(self.numbers) * self.suits.index(suit)

    def rank_by_number(self, card: Card):
        if card.name in self.special:
            return len(self.cardlist) + self.special.index(card.name)
        suit, num = card.name
        return self.suits.index(suit) + len(self.suits) * self.numbers.index(num)
