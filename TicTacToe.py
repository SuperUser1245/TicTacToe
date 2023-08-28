count = 0
field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
for i in field:
    print(i)
print('Write your answers as "row" "column"')


def turn():
    if count % 2 == 0:
        nought()
    elif count % 2 == 1:
        cross()


def cross():
    global winningcombs, count
    p1 = list(map(int, input('\nThe "Crosses" player, make your move: ').split()))
    if field[p1[0] - 1][p1[1] - 1] == '-':
        field[p1[0] - 1][p1[1] - 1] = 'X'
    else:
        print('\nMake another move')
        cross()

    count = count + 1
    for i in field:
        print(i)
    winningcombs = [[field[0][0], field[0][1], field[0][2]],
                    [field[1][0], field[1][1], field[1][2]],
                    [field[2][0], field[2][1], field[2][2]],
                    [field[0][0], field[1][0], field[2][0]],
                    [field[0][1], field[1][1], field[2][1]],
                    [field[0][2], field[1][2], field[2][2]],
                    [field[0][0], field[1][1], field[2][2]],
                    [field[0][2], field[1][1], field[2][0]]]
    check_the_victory()


def nought():
    global winningcombs, count
    p2 = list(map(int, input('\nThe "Noughts" player, make your move: ').split()))
    if field[p2[0] - 1][p2[1] - 1] == '-':
        field[p2[0] - 1][p2[1] - 1] = 'O'
    else:
        print('Make another move')
        nought()
    count = count + 1
    for i in field:
        print(i)
    winningcombs = [[field[0][0], field[0][1], field[0][2]],
                    [field[1][0], field[1][1], field[1][2]],
                    [field[2][0], field[2][1], field[2][2]],
                    [field[0][0], field[1][0], field[2][0]],
                    [field[0][1], field[1][1], field[2][1]],
                    [field[0][2], field[1][2], field[2][2]],
                    [field[0][0], field[1][1], field[2][2]],
                    [field[0][2], field[1][1], field[2][0]]]
    check_the_victory()


def check_the_victory():
    for i in winningcombs:
        if i == ['X', 'X', 'X'] or i == ['O', 'O', 'O']:
            if i == ['X', 'X', 'X']:
                print('\n The "Cross" Player Won. Congratulations')
                break
            elif i == ['O', 'O', 'O']:
                print('\n The "Nought" Player Won. Congratulations')
                break
        elif count == 8:
            print('Tie')
            break

    else:
        turn()


turn()