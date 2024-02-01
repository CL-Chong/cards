from objects.card_containers import Card, Hand
from objects.poker import Poker


def test_poker_rank():
    carddata = Poker()
    three_of_spades = Card(("S", "3"))
    four_of_diamonds = Card(("D", "4"))
    red_joker = Card(("r", "j"))
    four_of_hearts = Card(("H", "4"))
    jack_of_clubs = Card(("C", "J"))
    queen_of_spades = Card(("S", "Q"))
    king_of_hearts = Card(("H", "K"))

    assert carddata.rank_by_number(three_of_spades) < carddata.rank_by_number(
        four_of_diamonds
    )
    assert carddata.rank_by_suit(three_of_spades) > carddata.rank_by_suit(
        four_of_diamonds
    )
    deck = carddata.make_deck()
    for card in deck:
        assert carddata.rank_by_number(card) < carddata.rank_by_number(red_joker)
        assert carddata.rank_by_suit(card) < carddata.rank_by_suit(red_joker)
    assert carddata.rank_by_number(four_of_hearts) < carddata.rank_by_number(
        jack_of_clubs
    )
    assert carddata.rank_by_number(queen_of_spades) < carddata.rank_by_number(
        king_of_hearts
    )
    assert carddata.rank_by_suit(jack_of_clubs) < carddata.rank_by_suit(
        four_of_diamonds
    )
    assert carddata.rank_by_suit(four_of_hearts) > carddata.rank_by_suit(
        four_of_diamonds
    )
    assert carddata.rank_by_number(four_of_hearts) > carddata.rank_by_number(
        four_of_diamonds
    )
    return


def test_poker_sort():
    carddata = Poker()
    card_list = [
        Card(("S", "3")),
        Card(("D", "4")),
        Card(("r", "j")),
        Card(("H", "4")),
        Card(("C", "J")),
        Card(("H", "K")),
    ]

    bar = Hand.from_list("foo", card_list)
    bar.sort(key=carddata.rank_by_number)
    assert bar.hand == [
        Card(("S", "3")),
        Card(("D", "4")),
        Card(("H", "4")),
        Card(("C", "J")),
        Card(("H", "K")),
        Card(("r", "j")),
    ]
    bar.sort(key=carddata.rank_by_suit)
    assert bar.hand == [
        Card(("C", "J")),
        Card(("D", "4")),
        Card(("H", "4")),
        Card(("H", "K")),
        Card(("S", "3")),
        Card(("r", "j")),
    ]

    return
