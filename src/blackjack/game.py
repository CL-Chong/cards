import random
import time

import blackjack.algorithms as bj
from objects.card_containers import Card, Hand
from objects.poker import Poker


def game(rng: random.Random) -> int:
    # rng=random.Random(seed=114514)

    player_dict = {s: Hand(s) for s in ["dealer", "player"]}
    deck = Poker().make_deck()
    deck.shuffle(rng)

    for _, hand in player_dict.items():
        for _ in range(0, 2):
            hand.draw(deck.deal())

    player_dict["dealer"][0].hide()
    print_state(player_dict)

    while True:
        choice = input("[h]it or [s]tand? ")
        if choice == "h":
            player_dict["player"].draw(deck.deal())
            print_state(player_dict)
            if bj.hand_score(player_dict["player"]) == 0:
                print("Oops! player busted.")
                return -1
            continue
        if choice == "s":
            break

    print("player stands. dealer reveals hand.")
    player_dict["dealer"].reveal()
    print_state(player_dict)
    while (
        bj.hand_score(player_dict["dealer"]) < 17
        and bj.hand_score(player_dict["dealer"]) > 0
    ):
        print("dealer hits.")
        player_dict["dealer"].draw(deck.deal())
        print_state(player_dict)
        time.sleep(1)
    if bj.hand_score(player_dict["dealer"]) == 0:
        print("dealer busted! player wins.")
        return +1
    print("dealer stands.")
    if bj.hand_score(player_dict["dealer"]) < bj.hand_score(player_dict["player"]):
        print("player wins.")
        return +1
    elif bj.hand_score(player_dict["dealer"]) > bj.hand_score(player_dict["player"]):
        print("dealer wins.")
        return -1
    else:
        print("draw.")
        return 0


def print_state(player_dict):
    for player_name, hand in player_dict.items():
        if True in hand.hidden():
            score = "??"
        else:
            score = bj.hand_score(hand)
            if score > 21:
                score = "BLACKJACK"
        left = f"{player_name}'s hand: {hand}"
        right = f"{player_name}'s score: {score}"
        print(f"{left: <50}{right: >20}")

    return
