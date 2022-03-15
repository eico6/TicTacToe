from classes import Board
import os
import random
import time

# Declearing 'BAORD' as a global variable to improve readability
BOARD = Board()

def game_loop(is_player_turn: bool) -> int:
    BOARD.draw_board()
    winner = check_winner()

    # Initiate a turn, or end the game if a win condition is met
    if winner == 'NONE':
        player_turn() if is_player_turn else computer_turn()
    else:
        end_game(winner)
        return 0

    # Pass the turn over to the opponent and start a new game loop
    is_player_turn = False if (is_player_turn == True) else True
    game_loop(is_player_turn)

def check_winner() -> str:
    # Check for horizontal win conditions
    for i in range(0, 7, 3):
        potential_winner = BOARD.slots[i]
        for j in range(i, i + 3):
            if not BOARD.slots[j] == potential_winner:
                break
        else:
            return 'PLAYER' if (potential_winner == 'X') else 'COMPUTER'

    # Check for vertical win conditions
    for i in range(0, 3):
        potential_winner = BOARD.slots[i]
        for j in range(i, i + 7, 3):
            if not BOARD.slots[j] == potential_winner:
                break
        else:
            return 'PLAYER' if (potential_winner == 'X') else 'COMPUTER'

    # Check for win condition along ascending diagonal
    potential_winner = BOARD.slots[2]
    for i in range(2, 7, 2):
        if BOARD.slots[i] != potential_winner:
            break
    else:
        return 'PLAYER' if (potential_winner == 'X') else 'COMPUTER'


    # Check for win condition along descending diagonal
    potential_winner = BOARD.slots[0]
    for i in range(0, 9, 4):
        if not BOARD.slots[i] == potential_winner:
            break
    else:
        return 'PLAYER' if (potential_winner == 'X') else 'COMPUTER'

    # Check if there has been a tie
    for i in range(1, 10):
        if not BOARD.is_slot_occupied(i):
            break
    else:
        return 'TIE'

    # Function has reached its end, implying no win condition has been satisfied
    return 'NONE'

def player_turn() -> None:
    # Filter out invalid moves
    player_input = 0
    while (player_input not in range(1, 10)) or BOARD.is_slot_occupied(player_input):
        player_input = input(" Make your move (1 - 9): ")

        # Check if input is an integer
        try:
            int(player_input)
        except ValueError:
            continue
        player_input = int(player_input)

    # Insert move to the board
    BOARD.insert_to_board(player_input, 'X')

def computer_turn() -> None:
    print(" Computer's turn ...")

    # Synthetic 'do-while' loop to calculate a valid move
    while True:
        calculated_move = random.randint(1 , 9)
        if not BOARD.is_slot_occupied(calculated_move):
            break

    # Proceed with insertion and pause game to add immersion
    BOARD.insert_to_board(calculated_move, 'O')
    time.sleep(1.5)

def end_game(winner: str) -> None:
    BOARD.draw_board()

    # A dictionary is used to store conclusion texts
    conclusions = {
        'PLAYER': " Congratulations! Player wins!",
        'COMPUTER': " Too bad! Computer wins.",
        'TIE': " It's a tie! No one wins."
    }
    print(conclusions[winner] + '\n')
    os.system("pause")
