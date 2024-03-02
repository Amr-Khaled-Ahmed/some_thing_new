#  purpose : Played with the list of numbers between 1 and 9. Each player takes
#           turns picking a number from the list. Once a number has been picked, it cannot be picked
#           again. If a player has picked three numbers that add up to 15, that player wins the game.
#           However, if all the numbers are used and no player gets exactly 15, the game is a draw.
# Author: Amr Khaled Eldahshan
# ----------------------------------------------------------------------------------------------------------------------
import time

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
players = 2
players = [[] for i in range(
    players)]  # this code make a list for every player to store the selected numbers to each of them such as 2D array.
# print the game rules.
print("Hello,in this game the winner who collect any three numbers, the summation of them = 15")
print("*** Good luck ***")
print()

def winner_checker(selected_numbers):
    # This function to check who win after every choice by adding the selected numbers for the player who chose the last
    # in different types to get the goal(15), then if the goal has been achieved the function will return the numbers
    # which achieved our goal else it will return false and will not return the numbers.
    for i in range(len(selected_numbers) - 2):
        for j in range(i + 1, len(selected_numbers) - 1):
            for k in range(j + 1, len(selected_numbers)):
                if selected_numbers[i] + selected_numbers[j] + selected_numbers[k] == 15:  # Which is our goal.
                    return True, [selected_numbers[i], selected_numbers[j], selected_numbers[k]]
    return False, []

# Stating of the game ------------------------------------------------------------------------------




def Number_scrabble_game(current_player):


    while True:
        # This part will make sure that the user will not choose any string by avoiding errors and start again.
        try:

            while len(num_list) > 0:    # The Game will work until the numbers that can be selected run out.
                print(f"player {current_player + 1} you have {players[current_player]}, please select a number from the following list: {num_list} :  ")
                selected_numbers = int(input(""))
                while selected_numbers not in num_list:     # To check if the number is in the num_list.
                    selected_numbers = int(input(f"Invalid number. Please player {current_player + 1}, select a number from the following list: {num_list} : "))

                players[current_player].append(selected_numbers)    # Add the selected number to the current_player as 2D array.
                num_list.remove(selected_numbers)   # Remove the selected number from the num_list.
                win, winning_numbers = winner_checker(players[current_player])  # get the winner from winner_checker function.
                if win:
                    print(f"***** Player {current_player + 1} wins by collected {winning_numbers} *****")   # print the winner
                    print()
                    print()
                    choice = input("write \"yes\" if you Would like to play again and if you don`t press any thing: ").upper()

                    if choice == "YES":
                        num_list.clear()
                        players[1].clear()
                        players[0].clear()
                        num_list.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
                        print("Nice choice")
                        Number_scrabble_game(current_player)
                    else:
                        print("***  Thanks for playing  ***")
                        time.sleep(3.5)  # To hold the program until the message is read
                        exit()
                              # if there is winner, this part will stop the game
                current_player = (current_player + 1) % len(players)     # this part switch between player 1 and player 2
            # If all numbers in the array are selected, the word "Draw" will be printed.
            print("****** Draw ******")
            print()
            choice = input("write \"yes\" if you Would like to play again and if you don`t press any thing: ").upper()
            if choice == "YES":
                num_list.clear()
                players[1].clear()
                players[0].clear()
                num_list.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
                print("Nice choice")
                Number_scrabble_game(current_player)
            else:
                print("***  Thanks for playing  ***")
                time.sleep(3.5)  # To hold the program until the message is read
                return 0  # to stop the program

        except ValueError:

            print()
            print("Something went wrong, please choose valid value")
            Number_scrabble_game(current_player)


Number_scrabble_game(0)     # I submit the 0 to Current player

