cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = ''


def draw_grid():
    print('-' * 9
          + '\n| ' + cells[0][2] + ' ' + cells[1][2] + ' ' + cells[2][2] + ' |'
          + '\n| ' + cells[0][1] + ' ' + cells[1][1] + ' ' + cells[2][1] + ' |'
          + '\n| ' + cells[0][0] + ' ' + cells[1][0] + ' ' + cells[2][0] + ' |\n'
          + '-' * 9)
    check_winner()
    place_turn()


# convert grid matrix
def rearrange_grid():
    global cells
    temp_list = cells
    cells = ''
    count = -3
    for _ in range(len(temp_list)):
        cells += temp_list[count]
        count -= 3
        if count == -12:
            count = -2
        elif count == -11:
            count = -1
        elif count == -10:
            break
    cells = [(cells[i:i + 3]) for i in range(0, len(cells), 3)]
    draw_grid()


# place X or O
def place_turn():
    global cells, turn
    ascii_check = False
    turn = whos_turn(turn)
    coordinate = ''
    while not ascii_check:
        coordinate = input('Enter the coordinates: ').replace(' ', '')
        if coordinate.isnumeric():
            if check_number(coordinate):
                if cells[int(coordinate[0]) - 1][int(coordinate[1]) - 1] != ' ':
                    print('This cell is occupied! Choose another one!')
                else:
                    ascii_check = True
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
    coordinate = [int(x) - 1 for x in coordinate]
    cells[coordinate[0]] = list(cells[coordinate[0]])
    cells[coordinate[0]][coordinate[1]] = turn
    cells[coordinate[0]] = ''.join(cells[coordinate[0]])
    draw_grid()


# check if the input is between 1 and 3
def check_number(coordinate):
    for number in coordinate:
        if int(number) > 3 or int(number) < 0:
            return False
        return True


# checking the winner
def check_winner():
    winning = [[cells[0][2], cells[1][2], cells[2][2]], [cells[0][1], cells[1][1], cells[2][1]], [cells[0][0], cells[1][1], cells[2][0]],
               [cells[0][2], cells[0][1], cells[0][0]], [cells[1][2], cells[1][1], cells[1][0]], [cells[2][2], cells[2][1], cells[2][0]],
               [cells[0][2], cells[1][1], cells[2][0]], [cells[2][2], cells[1][1], cells[0][0]]]
    result = []
    for row in winning:
        if len(set(row)) == 1:
            if row[0] == 'O':
                result.append('O')
            elif row[0] == 'X':
                result.append('X')
    if result:
        print(result[0] + ' wins')
        exit()
    elif not result and ' ' not in [y for x in cells for y in x]:
        print(cells)
        print('Draw')
        exit()


def whos_turn(x_or_o):
    if x_or_o == 'X':
        return 'O'
    elif x_or_o == 'O':
        return 'X'
    else:
        return 'X'


rearrange_grid()
