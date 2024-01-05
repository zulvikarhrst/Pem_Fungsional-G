import random as rand
import logging


def player_goal(board_size):
    row = rand.randint(0, board_size - 1)
    col = rand.randint(0, board_size - 1)

    PSP = [row, col]
    GSP = PSP
    while GSP == PSP:
        GSP = [rand.randint(0, board_size - 1), rand.randint(0, board_size - 1)]

    return PSP, GSP


def initiate(function):
    def wrapper():
        board = function()
        PG = player_goal()
        board[PG[0]][PG[1]] = "A"
        board[PG[2]][PG[3]] = "0"
        return board

    return wrapper


@initiate
def b():
    n = 7
    return [["-" for i in range(n)] for i in range(n)]


def check_location(board, subject):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == subject:
                return [i, j]
    return "asikjuga!"


def brakes(function):
    def wrapper(direction, board):
        loc = check_location(board, "A")
        try:
            movement = function(direction, board)
            for i in movement:
                if i < 0:
                    raise Exception("Aduh, Mentok")
            else:
                new_board = [row.copy() for row in board]
                new_board[loc[0]][loc[1]] = "-"
                new_board[movement[0]][movement[1]] = "A"
                return new_board
        except IndexError:
            raise Exception("Aduh, Mentok")
    return wrapper

@brakes
def move(direction, board):
    x = check_location(board, "A")
    row = x[0]
    column = x[1]

    if direction == "up":
        new_location = [row - 1, column]
    elif direction == "down":
        new_location = [row + 1, column]
    elif direction == "right":
        new_location = [row, column + 1]
    elif direction == "left":
        new_location = [row, column - 1]
    else:
        new_location = [row, column]

    return new_location


def run():
    out = False

    board = b()
    goal_location = check_location(board, "0")
    while not out:
        print("* Selamat Datang di Board Game Pemrograman Fungsional *")
        print("   Anda (A) Dapat Berjalan Secara Horizontal maupun Vertikal Untuk Menuju Target (0)")
        print("   Selamat Bermain!")

        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end=" ")
            print("\n")

        print("==========================")
        print("   1. Cek Posisi")
        print("   2. Geser Kanan")
        print("   3. Geser Kiri")
        print("   4. Geser Atas")
        print("   5. Geser Bawah")
        print("   0. Keluar")
        print("==========================")
        pilihan = input('Pilihan: ')

        if pilihan.lower() == "1":
            loc = check_location(board, "A")
            print(f"({loc[0]}, {loc[1]})")
        elif pilihan.lower() == "2":
            move("right", board)
        elif pilihan.lower() == "3":
            move("left", board)
        elif pilihan.lower() == "4":
            move("up", board)
        elif pilihan.lower() == "5":
            move("down", board)
        elif pilihan.lower() == "0":
            out = True
        if check_location(board, "A") == goal_location:
            print("Menang!")
            out = True

run()