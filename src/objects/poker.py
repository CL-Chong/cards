from objects.card_containers import Card, Hand


class Poker:
    """Poker contains information on playing cards.
    Constructor:
        constructs the 52 playing cards + 2 jokers

    Attributes:
    suits: list[str]
        single capital letter for the 4 suits
    numbers: list[str]
        2-10, J, Q, K ,A
    special: list[tuple[str]]
        represent red and black jokers as [("r", "jk"), ("b", "jk")]
    cardlist: list[tuple[str]]
        52 playing cards, each represented as (<suit>, <number>)

    Methods:
    make_deck(deck_name, jokers): str, bool -> Hand
        deck_name: str, default="deck"
            describes name of the deck
        jokers: bool, default=False
            includes jokers if True, exclude if False
        returns a Hand containing a deck of playing cards
    rank_by_suit(card): Card -> int
        returns an integer rank of a playing card, suit-first (e.g D3 < S2)
        suits ranked in Engish convention C < D < H < S
    rank_by_number(card): Card -> Card
        returns an integer rank of a playing card, number-first (e.g. S2 < D3)
        suits ranked in Engish convention C < D < H < S
    """

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
        self.special = [("r", "jk"), ("b", "jk")]
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
