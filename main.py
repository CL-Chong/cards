import random

import blackjack.game as bjg


def main():
    current_score = 1000
    rng = random.Random()
    bjg.welcome()
    print(f"current score: {current_score}")
    while True:
        bet_raw = input("Place your bet: ")
        if not bet_raw.isnumeric():
            print("Please place a positive integer as a bet.")
            continue
        bet = int(bet_raw)
        if bet <= 0:
            print("Please place a positive integer as a bet.")
            continue
        if bet > current_score:
            print(f"Bet cannot exceed current score {current_score}.")
            continue
        current_score += bjg.game(rng) * bet
        if current_score <= 0:
            print(f"current score: {current_score}. You lose!")
            break
        choice = input(f"current score: {current_score}. continue? [y]/n ")
        if choice.lower() == "n":
            break
    print(f"final score: {current_score}")
    return


if __name__ == "__main__":
    main()
