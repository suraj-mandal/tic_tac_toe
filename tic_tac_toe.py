# program to play the tic tac toe game in python

import sys

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
        print("|   |   |   |")
        print(f"| {board[i]} | {board[i + 1]} | {board[i + 2]} |")
        print("|   |   |   |")
        print("-------------")


def player_input() -> None:
    while True:
        marker = input("Enter your marker (X or O) : ")
        if marker.upper() not in ['X', 'O']:
            print("Sorry! You have not chosen the correct marker! Please try again")
        else:
            break


def place_marker(board, marker, position):
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
        position = int(input("Enter the position to place the marker (1 - 9) : "))
        if position > 9 or position < 1:
            print("That is not the correct position -> please fill the position correctly!")
        if space_check(board, position):
            return position
        else:
            print("Sorry that position is already filled up in the board")


def game_reset() -> None:
    player_scores['PLAYER 2'] = 0
    player_scores['PLAYER 1'] = 0

    
def replay() -> bool:
    game_reset()
    choice = input("Do you want to play again ? (Y/N) : ")
    return choice.upper() == 'Y'


def player_game_logic(player_name: str, board: list, match: int) -> bool:

    found_win = False
    # implementing game logic for the player
    print(f"----- {player_name} TURN------ ")

    marker_position = player_choice(board)
    place_marker(board, player_dict[player_name], marker_position)

    print("----- Current state of the board -----")
    display_board(board)

    # case if the player wins
    if win_check(board, player_dict[player_name]):
        print(f"{player_name} has won match {match}")
        player_scores[player_name] += 2
        found_win = True

    return found_win


def init_board() -> list:
    board = ['#']
    for i in range(9):
        board.append(' ')
    print("Setting up the board")
    print("Current status of the board ")
    display_board(board)
    return board


def game_init_display() -> None:
    # game setup
    print()
    print("----------------------------------")
    print("Welcome players abroad !!!!")

    print("Markers are as follows : ")
    print("PLAYER 1 -> X")
    print("PLAYER 2 -> O")

    print("----------------------------------")
    print()
    player_input()


# Main gameplay


if __name__ == '__main__':

    while True:

        print("------------ WELCOME TO TIC TAC TOE -------------")
        print()
        print("RULES : ")
        print("1. Bet is the number of games that are played")
        print("1. Marker once chosen at the start of the game cannot be changed -> CHOOSE CAREFULLY")
        print("2. The above is the only rule :)")
        print()
        print()
        bet = int(input("Enter your bet : "))
        current_round = 1

        game_init_display()

        while current_round <= bet:

            # the game will continue from here
            print()
            print()
            print(f"--------------- GAME {current_round} -------------------")
            play_board = init_board()

            while True:

                if player_game_logic('PLAYER 1', play_board, current_round):
                    break

                # case when the entire board is filled up and there is no win
                if full_board_check(play_board):
                    print(f"The entire board is filled up... Game {current_round} IS A DRAW")
                    player_scores['PLAYER 1'] += 1
                    player_scores['PLAYER 2'] += 1
                    break

                # implementing game logic for player 2
                if player_game_logic('PLAYER 2', play_board, current_round):
                    break

            print("********************************************")
            print(f"--- GAME {current_round} SUMMARY ---")
            print(f"PLAYER 1 SCORE: {player_scores['PLAYER 1']}")
            print(f"PLAYER 2 SCORE: {player_scores['PLAYER 2']}")
            print("********************************************")

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

