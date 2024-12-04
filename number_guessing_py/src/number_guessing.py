#!/usr/bin/env python
import random
import shutil
import os
from time import sleep
from player import Player


if __name__ == "__main__":

    # Get terminal size
    window_center = shutil.get_terminal_size().columns

    def generate_random_number():

        random_numbers = []
        for i in range(0, 4):
            rNumber = random.randint(0, 9)
            random_numbers.append(rNumber)
        return random_numbers

    def create_players():

        p1_name = input("Player 1, Please write your name: ").capitalize()
        player1 = Player(p1_name, 0)

        p2_name = input("Player 2, Please write your name: ").capitalize()
        player2 = Player(p2_name, 0)
        return [player1, player2]

    def print_name_and_score(player1: Player, player2: Player):
        print(
            f"⫘⫘⫘ < {player1.player_name} ─── ⋆⋅☆⋅⋆ ───  {player2.player_name} > ⫘⫘⫘".center(
                window_center
            )
        )
        print(
            f"——— « {player1.player_score} »» —— ⍟ —— «« {player2.player_score} » ———".center(
                window_center
            )
        )
        print("  ꧁꧂  ꧁꧂  ꧁꧂  ꧁꧂  ꧁꧂  \n\n\n".center(window_center))

    def guess_and_get_hints(user_guesses, secret_numbers):
        # TODO: fix duplicated numbers (e.g 4454) hints????  

        hints = []
        for i in range(0, 4):
            if secret_numbers[i] == user_guesses[i]:
                hints.append("*")
                continue
            elif secret_numbers.__contains__(user_guesses[i]):
                hints.append("+")
                continue
            else:
                hints.append("-")
                continue
        # Wrong check it should check only "* * * *" "- - - -"
        are_equal = all(hint == "*" for hint in hints)

        return hints, are_equal

    def get_user_input():

        # TODO:
        while True:
            try:
                user_guesses = [
                    int(guess_list)
                    for guess_list in input(
                        "\nEnter a number of 4-digits between 0-9 (e.g: X X X X): "
                    ).split()
                ]
            except ValueError:
                print("\n")

            # Check if the input contains exactly 4 numbers
            if len(user_guesses) == 4 and all(0 <= num <= 9 for num in user_guesses):
                break
            else:
                print("Invalid input! Please enter exactly 4 numbers between 0-9.")
        return user_guesses

    def display():
        print(
            "                          Welcome to Gues Number Game.                  \n"
        )
        print(
            "Game info:\n The players have just 5 guesses to discover a secret number (0-9) of 4-digits."
            "Players type their guess into the screen and are told whether the secret"
            "number is 'more than' or 'less than' the number they guessed. "
            "If you get '*' sign it is correct nummber in correct digit place."
            "If you get '+' it's means correct number but wrong place"
            "If you get '-' it it's incorrect number and incorrect place. Good luck!🍀"
        )
        players = create_players()
        print("Getting ready...")
        secret_numbers = generate_random_number()
        sleep(3)
        os.system("cls")
        print_name_and_score(players[0], players[1])
        # Game started

        # print(f"Random num: {secret_numbers}")
        isPlayerActive = True
        user_guesses = get_user_input()
        while isPlayerActive:
            if not user_guesses:
                user_guesses = get_user_input()
                continue
            else:
                hints, are_equal = guess_and_get_hints(user_guesses, secret_numbers)
                user_guesses = ""
                if are_equal:
                    print(
                        f"Congratulations🎉🎊🍾 Winnn, the secret numbers are: {secret_numbers}".center(
                            window_center
                        )
                    )
                    isPlayerActive = False
                else:
                    print("\t\t\t\t\t\t      ", end="")
                    for j in range(0, 4):
                        print(f" {hints[j]}", end="")


display()
