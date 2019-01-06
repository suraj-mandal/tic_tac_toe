# program to play the tic tac toe game in python

import sys
from colorama import Fore

player_scores = {
    'PLAYER 1': 0,
    'PLAYER 2': 0,
}

player_dict = {
    'PLAYER 1': 'X',
    'PLAYER 2': 'O'
}


def display_board(board: list) -> None:
    print("-------------")
    for i in range(1, 10, 3):
        print(Fore.BLUE+"|   |   |   |")
        print(Fore.BLUE + f"| {board[i]} | {board[i + 1]} | {board[i + 2]} |")
        print(Fore.BLUE + "|   |   |   |")
        print(Fore.BLUE + "-------------")


def player_input() -> None:
    while True:
        marker = input(Fore.CYAN+"Enter your marker (X or O) : ")
        if marker.upper() not in ['X', 'O']:
            print(Fore.RED+"Sorry! You have not chosen the correct marker! Please try again")
        else:
            break


def place_marker(board: list, marker: str, position: int) -> None:
    board[position] = marker


def win_check(board, mark):
    win_positions = [(1, 2, 3), (1, 4, 7), (4, 5, 6), (7, 8, 9), (2, 5, 8)
                     , (1, 5, 9), (3, 5, 7), (3, 6, 9)]

    for win in win_positions:
        if board[win[0]] == mark and board[win[1]] == mark and board[win[2]] == mark:
            return True

    return False


def space_check(board: list, position: int) -> bool:
    return board[position] == ' '


def full_board_check(board: list) -> bool:
    return ' ' not in board


def player_choice(board: list) -> int:
    while True:
        position = int(input(Fore.CYAN+"Enter the position to place the marker (1 - 9) : "))
        if position > 9 or position < 1:
            print(Fore.RED+"That is not the correct position -> please fill the position correctly!")
        if space_check(board, position):
            return position
        else:
            print(Fore.LIGHTMAGENTA_EX+"Sorry that position is already filled up in the board")


def game_reset() -> None:
    player_scores['PLAYER 2'] = 0
    player_scores['PLAYER 1'] = 0

    
def replay() -> bool:
    game_reset()
    choice = input(Fore.CYAN+"Do you want to play again ? (Y/N) : ")
    return choice.upper() == 'Y'


def player_game_logic(player_name: str, board: list, match: int) -> bool:

    found_win = False
    # implementing game logic for the player
    print(Fore.LIGHTYELLOW_EX+f"----- {player_name} TURN------ ")

    marker_position = player_choice(board)
    place_marker(board, player_dict[player_name], marker_position)

    print(Fore.GREEN+"----- Current state of the board -----")
    display_board(board)

    # case if the player wins
    if win_check(board, player_dict[player_name]):
        print(Fore.MAGENTA+f"{player_name} has won match {match}")
        player_scores[player_name] += 2
        found_win = True

    return found_win


def init_board() -> list:
    board = ['#']
    for i in range(9):
        board.append(' ')
    print(Fore.LIGHTGREEN_EX+"Setting up the board")
    print(Fore.LIGHTGREEN_EX+"Current status of the board ")
    display_board(board)
    return board


def game_init_display() -> None:
    # game setup
    print()
    print(Fore.LIGHTBLUE_EX+"----------------------------------")
    print(Fore.LIGHTBLUE_EX+"Welcome players abroad !!!!")

    print(Fore.LIGHTBLUE_EX+"Markers are as follows : ")
    print(Fore.LIGHTBLUE_EX+"PLAYER 1 -> X")
    print(Fore.LIGHTBLUE_EX+"PLAYER 2 -> O")

    print(Fore.LIGHTBLUE_EX+"----------------------------------")
    print()
    player_input()


# Main gameplay


if __name__ == '__main__':

    while True:

        print(Fore.LIGHTCYAN_EX+"------------ WELCOME TO TIC TAC TOE -------------")
        print()
        print(Fore.GREEN+"RULES : ")
        print(Fore.LIGHTBLUE_EX+"1. Bet is the number of games that are played")
        print(Fore.LIGHTBLUE_EX+"1. Marker once chosen at the start of the game cannot be changed -> CHOOSE CAREFULLY")
        print(Fore.LIGHTBLUE_EX+"2. The above is the only rule :)")
        print()
        print()
        bet = int(input(Fore.CYAN+"Enter your bet : "))
        current_round = 1

        game_init_display()

        while current_round <= bet:

            # the game will continue from here
            print()
            print()
            print(Fore.GREEN+f"--------------- GAME {current_round} -------------------")
            play_board = init_board()

            while True:

                if player_game_logic('PLAYER 1', play_board, current_round):
                    break

                # case when the entire board is filled up and there is no win
                if full_board_check(play_board):
                    print(Fore.MAGENTA+f"The entire board is filled up... Game {current_round} IS A DRAW")
                    player_scores['PLAYER 1'] += 1
                    player_scores['PLAYER 2'] += 1
                    break

                # implementing game logic for player 2
                if player_game_logic('PLAYER 2', play_board, current_round):
                    break

            print(Fore.CYAN+"********************************************")
            print(Fore.BLUE+f"--- GAME {current_round} SUMMARY ---")
            print(Fore.GREEN+f"PLAYER 1 SCORE: {player_scores['PLAYER 1']}")
            print(Fore.GREEN+f"PLAYER 2 SCORE: {player_scores['PLAYER 2']}")
            print(Fore.CYAN+"********************************************")

            current_round += 1

        print("---------------------------------------------")
        print()
        print()
        if player_scores['PLAYER 1'] > player_scores['PLAYER 2']:
            print(f"Congratulations -> PLAYER 1 has won the game")
        elif player_scores['PLAYER 2'] > player_scores['PLAYER 1']:
            print(f"Congratulations -> PLAYER 2 has won the game")
        else:
            print("Its a draw! WELL PLAYED FROM BOTH SIDES")

        if not replay():
            print("------THANKS FOR PLAYING THE GAME -----")
            sys.exit(0)

