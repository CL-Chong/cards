from objects.card_containers import Card, Hand
from objects.poker import Poker


def card_score(card: Card) -> int:
    """comptues the blackjack score of a card from Poker().cardlist.
    returns 1 for aces.
    """
    _, num = card.name
    if num == "A":
        return 1
    elif num.isnumeric():
        return int(num)
    else:
        return 10


def hand_score(hand: Hand) -> float | int:
    """computes the blackjack score of a blackjack hand.
    returns 0 for busted hand, and 21.1 for blackjacks.
    raises ValueError if the hand size is less than 2."""
    if hand.size() < 2:
        raise ValueError(f"Invaid hand size for {hand.player}'s hand.")
    point_hand = [card_score(card) for card in hand]
    ace_count = point_hand.count(1)
    base_point = sum(point_hand)
    if ace_count > 0 and base_point < 12:
        base_point += 10
    if base_point == 21 and hand.size() == 2:
        base_point += 0.1
    if base_point >= 22:
        return 0
    return base_point
