l_l1 = ['', '', '']
l_l2 = ['', '', '']
l_l3 = ['', '', '']

mat_jeux = [l_l1, l_l2, l_l3]


def reset():
    for ligne in range(3):
        for colonne in range(3):
            mat_jeux[ligne][colonne] = ' '


def aff():
    for ligne in mat_jeux:
        print ligne


def player_input():
    print 'input ligne: '
    ligne = input()
    print 'input colonne '
    colonne = input()

    while ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2:
        print 'met ta piece sur le jeux!'
        print 'input ligne: '
        ligne = input()
        print 'input colonne '
        colonne = input()

    return [ligne, colonne]


def player_victory():
    victoire = False

    for line in mat_jeux:
        if line[0] == line[1] == line[2] != ' ':
            victoire = True

    for col in range(3):
        test = ['']
        for case in mat_jeux:
            test.append(case[col])
        print test
        if test[1] == test[2] == test[3] != ' ':
            victoire = True

    if mat_jeux[0][0] == mat_jeux[1][1] == mat_jeux[2][2] != ' ':
        victoire = True
    if mat_jeux[0][2] == mat_jeux[1][1] == mat_jeux[2][0] != ' ':
        victoire = True

    return victoire



reset()
print (mat_jeux)
aff()

# a=raw_input()
# print a*2

quit_flag = False
while quit_flag != True:

    print 'Le jeux commence :'
    reset()

    endgame = False
    p_turn = 0
    turn_count = 0

    while endgame == False:
        aff()

        curr = player_input()
        while mat_jeux[curr[0]][curr[1]] != ' ':
            print 'Il y a deja une piece! ca commence a 0-0 en haut a gauche'
            curr = player_input()

        if p_turn == 0:
            mat_jeux[curr[0]][curr[1]] = 'X'
            p_turn += 1
        else:
            mat_jeux[curr[0]][curr[1]] = 'O'
            p_turn -= 1

        if player_victory():
            endgame = True
            victory = True

        if turn_count > 8:
            endgame = True

        turn_count += 1

    else:
        if victory:
            aff()
            if p_turn == 1:
                print 'Player 1 Wins'
            else:
                print 'Player 2 Wins'
        else:
            print 'NUL!!!'

        print 'partie terminee'
        print 'continuer? (y/n)'
        test = raw_input()
        test = test.lower()
        if test == 'n':
            quit_flag = True
