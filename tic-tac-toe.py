# helper functions
def prompt(axis):
    x = input('Enter {axis} position (1-3): '.format(axis=axis))
    return x


def create_board():
    return [[' ' for x in xrange(0, 3)] for r in xrange(0, 3)]


def print_line(board_line):
    return ' {a} | {b} | {c} '.format(a=board_line[0], b=board_line[1], c=board_line[2])


def print_board(board):
    def get_board_line(board_line):
        return ' {a} | {b} | {c} '.format(a=board_line[0], b=board_line[1], c=board_line[2])

    print ''
    print get_board_line(board[0])
    print '--- --- ---'
    print get_board_line(board[1])
    print '--- --- ---'
    print get_board_line(board[2])
    print ''


def place(symbol, x, y, b):
    if b[x - 1][y - 1] == ' ':
        b[x - 1][y - 1] = symbol
    else:
        raise Exception()


count_symbol = lambda symbol, lst: lst.count(symbol) == 3


def check_full_line(b):
    for row in b:
        if count_symbol('x', row) or count_symbol('o', row):
            return True


def check_victory(b):
    if check_full_line(b):
        return True

    board_c = create_board()

    for i in xrange(0,2):
        for j in xrange(0,2):
            board_c[i][j] = b[j][i]

    if check_full_line(board_c):
        return True

    diag_1 = [b[0][0], b[1][1], b[2][2]]
    diag_2 = [b[2][0], b[1][1], b[0][2]]

    if count_symbol('x', diag_1) or count_symbol('o', diag_1):
        return True

    if count_symbol('x', diag_2) or count_symbol('o', diag_2):
        return True


# game
player_turn = 1
turn = 1
board = create_board()
print_board(board)
print 'Game starts!'

while True:
    if player_turn == 1:
        print 'Player one turn, enter position: \n'
        pos_x = prompt('x')
        pos_y = prompt('y')

        try:
            place('x', pos_x, pos_y, board)
            player_turn = 2
        except:
            print "Can't place 'x' to position {x}, {y}".format(x=pos_x, y=pos_y)
    else:
        print 'Player two turn, enter position: \n'
        pos_x = prompt('x')
        pos_y = prompt('y')
        try:
            place('o', pos_x, pos_y, board)
            player_turn = 1
        except:
            print "Can't place 'o' to position {x}, {y}".format(x=pos_x, y=pos_y)

    print print_board(board)

    if check_victory(board):
        if player_turn == 2:
            print 'Player one wins'
            break
        else:
            print 'Player two wins'
            break

    if turn == 9:
        print "Tie!"
        break
