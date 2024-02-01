from objects.card_containers import Card, Hand
from objects.poker import Poker


def card_score(card: Card) -> int:
    _, num = card.name
    if num == "A":
        return 1
    elif num.isnumeric():
        return int(num)
    else:
        return 10


def hand_score(hand: Hand) -> float | int:
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
