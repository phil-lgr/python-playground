# -*- coding: utf-8 -*-

# DEFINE GLOBAL VARIABLES
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
endofgame = 0
players = ['A', 'B']
cntr = 0


# DEFINE FUNCTIONS

# Print out the board
def print_board():
    for i1, i2, i3 in board:
        print '%s|%s|%s' % (i1, i2, i3)


# Check for the end of game conditions and outputs winner
def checkendofgame():
    for i1, i2, i3 in board:
        endofgame == 1


# Main function
while endofgame == 0:

    coords = [1, 1]
    input_status = False
    while not input_status:
        print 'Hey player %s! Where do you want to place your token? (for exemple: left, center)' % (players[cntr % 2])
        posish = raw_input()

        if len(posish.split()) == 2:

            [i1, i2] = posish.split()
            # Lets assume the player entered correct stings
            input_status = True
            player = 'B'
            cntr += 1
        elif len(posish.split()) <> 2:
            print 'Hey player %s! Are you stupid or what?' % (players[cntr % 2])
            continue

        if i1 == 'left' or i2 == 'left':
            coords[0] = 0
        if i1 == 'right' or i2 == 'right':
            coords[0] = 2
        if i1 == 'up' or i2 == 'up':
            coords[1] = 0
        if i1 == 'down' or i2 == 'down':
            coords[1] = 2
        # Update and print board
        if board[coords[1]][coords[0]] == 0:
            board[coords[1]][coords[0]] = players[(cntr - 1) % 2]
            print_board()
        else:
            cntr -= 1
            print 'Hey player %s! Are you stupid or what?' % (players[cntr % 2])
            input_status = False
