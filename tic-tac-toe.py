import os
from random import randint

start = 0
player = 'Player'
board_type = 1
board = [['', '', ''], ['', '', ''], ['', '', '']]
win_board = [['', '', ''], ['', '', ''], ['', '', '']]
X = 'X'
O = 'O'
size = 3  # Size of board

def countWins(p1, p2):
    count = 0  # Keeps count of wins possible

    for i in range(size):
        for j in range(size):
            if board[i][j] != p1 and board[i][j] != p2:
                copy = board[i][j]  # A dummy variable to restore 'board[i][j]'
                board[i][j] = p1

                if win(p1) == 1:
                    count += 1

                board[i][j] = copy

    return count


def get_insane_AI_move(ai, pl, x=0, name=''):
    for i in range(size):
        for j in range(size):
            if board[i][j] != ai and board[i][j] != pl:
                copy = board[i][j]
                board[i][j] = ai

                if win(ai) == 1 or tie() == 1:
                    if x:
                        print(name + ' placed in cell ', i * size + j + 1)
                    return

                board[i][j] = copy

    for i in range(size):
        for j in range(size):
            if board[i][j] != ai and board[i][j] != pl:
                copy = board[i][j]
                board[i][j] = pl

                if win(pl) == 1 or tie() == 1:
                    board[i][j] = ai
                    if x:
                        print(name + ' placed in cell ', i * size + j + 1)
                    return
                board[i][j] = copy

    wins2 = []
    l = 0

    for i in range(size):
        for j in range(size):
            if board[i][j] != ai and board[i][j] != pl:
                copy = board[i][j]
                board[i][j] = ai

                if countWins(ai, pl) > 1:
                    l += 1
                    r = [i, j]
                    wins2.append(r)

                board[i][j] = copy

    if l:
        m = wins2[randint(0, 1000) % l]
        board[m[0]][m[1]] = ai
        if x:
            print(name + ' placed in cell ', m[0] * size + m[1] + 1)
        return

    l = 0

    pos_centers = [[i, j] for i in range(size) for j in range(size)
                   if (i in [0, size - 1]) == (j in [0, size - 1]) == False]

    centers = []

    for i in range(len(pos_centers)):
        x = pos_centers[i][0]
        y = pos_centers[i][1]

        if board[x][y] != ai and board[x][y] != pl:
            centers.append(pos_centers[i])
            l += 1

    if l:
        r = centers[randint(1, 1000) % l]
        board[r[0]][r[1]] = ai

        if x:
            print(name + ' placed in cell ', r[0] * size + r[1] + 1)

        return

    l1 = 0
    l2 = 0

    pos_edges = [[0, 0], [0, size - 1], [size - 1, 0], [size - 1, size - 1]]
    edges = []

    for i in range(len(pos_edges)):
        x = pos_edges[i][0]
        y = pos_edges[i][1]

        if board[x][y] != ai and board[x][y] != pl:
            edges.append(pos_edges[i])
            l1 += 1

    if l1:
        r = edges[randint(1, 1000) % l1]
        board[r[0]][r[1]] = ai

        if x:
            print(name + ' placed in cell ', r[0] * size + r[1] + 1)

        return

    pos_middles = [[i, j] for i in range(size) for j in range(size)
                   if (i in [0, size - 1]) != (j in [0, size - 1])]

    middles = []

    for i in range(len(pos_middles)):
        x = pos_middles[i][0]
        y = pos_middles[i][1]

        if board[x][y] != ai and board[x][y] != pl:
            middles.append(pos_middles[i])
            l2 += 1

    r = middles[randint(1, 1000) % l2]
    board[r[0]][r[1]] = ai

    if x:
        print(name + ' placed in cell ', r[0] * size + r[1] + 1)

    return


def get_hard_AI_move(ai, pl, x=0, name=''):
    for i in range(size):
        for j in range(size):
            if board[i][j] != ai and board[i][j] != pl:
                copy = board[i][j]
                board[i][j] = ai

                if win(ai) == 1 or tie() == 1:
                    if x:
                        print(name + ' placed in cell ', i * size + j + 1)
                    return

                board[i][j] = copy

    for i in range(size):
        for j in range(size):
            if board[i][j] != ai and board[i][j] != pl:
                copy = board[i][j]
                board[i][j] = pl

                if win(pl) == 1 or tie() == 1:
                    board[i][j] = ai

                    if x:
                        print(name + ' placed in cell ', i * size + j + 1)

                    return

                board[i][j] = copy

    l = 0

    possible = [[i, j] for i in range(size) for j in range(size)]

    available = []

    for i in range(len(possible)):
        x = possible[i][0]
        y = possible[i][1]

        if board[x][y] != ai and board[x][y] != pl:
            available.append(possible[i])
            l += 1

    r = available[randint(1, 1000) % l]

    board[r[0]][r[1]] = ai

    if x:
        print(name + ' placed in cell ', r[0] * size + r[1] + 1)

    return


def get_easy_AI_move(ai, pl, x=0, name=''):
    l = 0

    possible = [[i, j] for i in range(size) for j in range(size)]

    available = []

    for i in range(len(possible)):
        x = possible[i][0]
        y = possible[i][1]

        if board[x][y] != ai and board[x][y] != pl:
            available.append(possible[i])
            l += 1

    r = available[randint(1, 1000) % l]
    board[r[0]][r[1]] = ai

    if x:
        print(name + ' placed in cell ', r[0] * size + r[1] + 1)
    return


def get_user_move(p1, p2):
    g = int(input('Enter your move: ')) - 1

    x = g // size
    y = g % size

    if x >= size or y >= size or board[x][y] == p1 or board[x][y] == p2:
        print('Move not valid, try again')
        get_user_move(p1, p2)
        return

    print(player + ' placed in cell ', g + 1)

    board[x][y] = p1
    print()


def get_win(p):
    for i in range(size):
        if all(board[i][j] == p for j in range(size)):
            for j in range(size):
                win_board[i][j] = p
            return

        if all(board[j][i] == p for j in range(size)):
            for j in range(size):
                win_board[j][i] = p
            return

    if all(board[i][i] == p for i in range(size)):
        for i in range(size):
            win_board[i][i] = p
        return

    if all(board[i][-(i + 1)] == p for i in range(size)):
        for i in range(size):
            win_board[i][-(i + 1)] = p
        return


def printBoard():
    for i in range(size - 1):
        print('      ' + '|       ' * (size - 1))
        print(end='  ')

        for j in range(size - 1):
            print(board[i][j], end='   |   ')

        print(board[i][-1])
        print('      ' + '|       ' * (size - 1))
        print('------' + '--------' * (size - 1))
        '      |       '

    print('      ' + '|       ' * (size - 1))
    print(end='  ')

    for j in range(size - 1):
        print(board[-1][j], end='   |   ')

    print(board[-1][-1])
    print('      ' + '|       ' * (size - 1))

    print()


def printWin(p):
    get_win(p)
    for i in range(size - 1):
        for j in range(size - 1):
            print(win_board[i][j], end=' | ')
        print(win_board[i][-1])
        print('---' * size + '-' * (size - 2))

    for j in range(size - 1):
        print(win_board[-1][j], end=' | ')

    print(win_board[-1][-1])
    print()


def changeSize():
    global size
    size = int(input('Enter board size: '))
    initialize()


def main_menu():
    global start
    print()

    if start == 0:
        intro()
        start = 1
        main_menu()
        return

    print('\nQ to quit\n')
    print('1. Change size')
    print('2. Play')
    option = input('\nPlease choose option: ')

    if option == '1': changeSize()

    if option == '2':
        initialize()
        play('X', 'O')

    if option == 'q' or option == 'Q':
        print('Thanks for playing!\n')
        return

    print()
    main_menu()

def intro():
    initialize()

    print('Hello ' + player + '! Prepare to lose with AI :)')

    print('Three levels of difficulty possible\n')
    print('1 - easy')
    print('2 - hard')
    print('3 - insane')


def play(p1, p2):
    print()
    initialize()

    computer = 'AI'

    print('1 - easy')
    print('2 - hard')
    print('3 - insane')

    print()

    level = int(input('Please choose difficulty (1-3): '))

    print()

    c = randint(0, 1)

    pl = p1
    ai = p2

    if c == 0:
        ai = p1
        pl = p2

        print('\n' + computer + ' goes first!\n\n')

    else:
        print('\n' + player + ' goes first!\n\n')
        printBoard()

    d = 0

    while True:
        t = d % 2

        if t == c:
            if level == 1: get_easy_AI_move(ai, pl, 1, computer)
            if level == 2: get_hard_AI_move(ai, pl, 1, computer)
            if level == 3: get_insane_AI_move(ai, pl, 1, computer)

            printBoard()

            if win(ai):
                print(computer + ' wins!\n')
                print('Winning setup of AI:\n\n')
                printWin(ai)
                break

        else:
            get_user_move(pl, ai)

            printBoard()

            if win(pl):
                print(player + ' wins!')
                print('Winning setup of Player:\n\n')
                printWin(pl)
                break

        if tie():
            print('Tie!')
            break

        d += 1

    play_again(p1, p2)


def initialize():
    global board, win_board

    board = [[' ' for _ in range(size)] for __ in range(size)]
    win_board = [[' ' for _ in range(size)] for __ in range(size)]


def play_again(p1, p2):
    option = input('Want to play again? ( y / n ): ').lower()

    if option == 'y':
        play(p1, p2)
    elif option == 'n':
        return
    else:
        print('\nOption invalid, please enter valid one.')
        play_again(p1, p2)


def win(p):
    if any(all(board[i][j] == p for j in range(size)) for i in range(size)):
        return True
    if any(all(board[j][i] == p for j in range(size)) for i in range(size)):
        return True
    if all(board[i][i] == p for i in range(size)):
        return True
    if all(board[i][-(i + 1)] == p for i in range(size)):
        return True

    return False


def tie():
    return all(all(j in [X, O] for j in i) for i in board)

main_menu()