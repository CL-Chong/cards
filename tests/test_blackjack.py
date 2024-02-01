import blackjack.algorithms as bj
from objects.card_containers import Card, Hand
from objects.poker import Poker


def test_blackjack_scores():
    card_list = [
        Card(("S", "3")),
        Card(("D", "4")),
        Card(("S", "A")),
        Card(("H", "4")),
        Card(("C", "J")),
        Card(("H", "K")),
        Card(("C", "10")),
        Card(("H", "A")),
    ]

    hand1 = Hand.from_list(
        "foo", [card for i, card in enumerate(card_list) if i in {0, 1, 2, 3}]
    )
    assert bj.hand_score(hand1) == 12
    hand2 = Hand.from_list(
        "foo", [card for i, card in enumerate(card_list) if i in {0, 1, 3, 4}]
    )
    assert bj.hand_score(hand2) == 21
    hand3 = Hand.from_list(
        "foo", [card for i, card in enumerate(card_list) if i in {0, 1, 4, 5}]
    )
    assert bj.hand_score(hand3) == 0
    hand4 = Hand.from_list(
        "foo", [card for i, card in enumerate(card_list) if i in {2, 4}]
    )
    assert bj.hand_score(hand4) > 21
    hand5 = Hand.from_list(
        "foo", [card for i, card in enumerate(card_list) if i in {2, 6}]
    )
    assert bj.hand_score(hand4) == bj.hand_score(hand5)
    hand6 = Hand.from_list(
        "foo", [card for i, card in enumerate(card_list) if i in {1, 2}]
    )
    assert bj.hand_score(hand6) == 15
    hand7 = Hand.from_list(
        "foo", [card for i, card in enumerate(card_list) if i in {1, 2, 7}]
    )
    assert bj.hand_score(hand7) == 16
    hand8 = Hand.from_list(
        "foo", [card for i, card in enumerate(card_list) if i in {0}]
    )
    try:
        _ = bj.hand_score(hand8)
        assert False
    except ValueError:
        assert True

    return
