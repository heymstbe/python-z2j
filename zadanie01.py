def display_board(board):
    # Rysuję tablicę wraz z polami skreślonymi przez użytkownika i komputer
    print(" " * 25)
    print(" " + 3 * " " + str(board[0][0]) + 3 * " " + "|" + 3 * " " + str(board[0][1]) + 3 * " " + "|" + 3 * " " + str(
        board[0][2]) + 3 * " " + " ")
    print("-" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "-")
    print(" " + 3 * " " + str(board[1][0]) + 3 * " " + "|" + 3 * " " + str(board[1][1]) + 3 * " " + "|" + 3 * " " + str(
        board[1][2]) + 3 * " " + " ")
    print("-" + 7 * "-" + "+" + 7 * "-" + "+" + 7 * "-" + "-")
    print(" " + 3 * " " + str(board[2][0]) + 3 * " " + "|" + 3 * " " + str(board[2][1]) + 3 * " " + "|" + 3 * " " + str(
        board[2][2]) + 3 * " " + " ")
    print(" " * 25)
    print()


def enter_move(board):
    # Wprowadzam ruch uźytkownika
    entered = True
    while entered:
        try:
            move = int(input("Wskaż pole: "))
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = "O"
                        print("Ty:")
                        display_board(board)
                        entered = False
        except ValueError:
            print("Ups! To pole jest zajęte.")


def make_list_of_free_fields(board):
    # Sprawdzam czy możliwy jest kolejny ruch
    empty_tuple = ()
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                empty_tuple += ((i, j),)
    return empty_tuple


def victory_for(board, sign):
    # Sprawdzam czy ktoś wygrał
    win = None
    for i in range(3):
        win = True
        for j in range(3):
            if board[i][j] != sign:
                win = False
                break
        if win:
            return win

    for i in range(3):
        win = True
        for j in range(3):
            if board[j][i] != sign:
                win = False
                break
        if win:
            return win

    win = True
    for i in range(3):
        if board[i][i] != sign:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(3):
        if board[i][3 - 1 - i] != sign:
            win = False
            break
    if win:
        return win
    return False


def draw_move(board):
    # Tworzę ruch komputera
    from random import randrange
    marked = True
    while marked:
        if not victory_for(board, "O") and len(make_list_of_free_fields(board)) < 2:
            for i in range(3):
                for j in range(3):
                    if board[i][j] != "X" and board[i][j] != "O":
                        board[i][j] = "X"
            display_board(board)
            marked = False
            break
        if not victory_for(board, "O"):
            if len(make_list_of_free_fields(board)) > 1:
                move = randrange(8) + 1
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == move:
                            board[i][j] = "X"
                            print("Komputer:")
                            display_board(board)
                            marked = False
        else:
            print("Komputer:")
            display_board(board)
            marked = False


board = [[False for i in range(3)] for j in range(3)]
number = 1
for i in range(3):
    for j in range(3):
        board[i][j] = number
        number += 1
board[1][1] = "X"  # Każdą grę zaczyna komputer od skreślenia środkowego pola (5)
display_board(board)
while True:  # Graj dopóki będzie to możliwe
    enter_move(board)
    draw_move(board)
    if victory_for(board, "O"):
        print("Brawo! Wygrałeś!")
        break
    if victory_for(board, "X"):
        print("Niestety, komputer wygrał!")
        break
    if len(make_list_of_free_fields(board)) < 2:
        print("No i mamy remis.")
        break
