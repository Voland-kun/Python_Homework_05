# Создайте программу для игры в ""Крестики-нолики"".

from random import randint

def coinflip():
    player_count = randint(0, 1)
    print('Бросок монеты:')
    if player_count == 1:
        print(f'Выпала решка, первым ходит {players[(player_count)%2]}')
    else:
        print(f'Выпал орёл, первым ходит {players[(player_count)%2]}')
    return player_count

player1 = 'Игрок1'
player2 = 'Игрок2'
players = [player1, player2]
field_visual = [['___|','___|','___'],['___|','___|','___'],['   |','   |','   ']]
field = [['','',''],['','',''],['','','']]
player_count = coinflip()
char = ['X', 'O']

def vis(field_visual):
    for i in range(len(field_visual)):
        print()
        for j in range(len(field_visual[i])):
            print(field_visual[i][j], end='')

def win_condition(char, players, player_count):
    if field[0][0]==field[0][1]==field[0][2]\
        or field[1][0]==field[1][1]==field[1][2]\
        or field[2][0]==field[2][1]==field[2][2]\
        or field[0][0]==field[1][0]==field[2][0]\
        or field[0][1]==field[1][1]==field[2][1]\
        or field[0][2]==field[1][2]==field[2][2]\
        or field[0][0]==field[1][1]==field[2][2]\
        or field[0][2]==field[1][1]==field[2][0]:
        print()
        print(f'Победил {players[player_count%2]}.')
        win_flag = True
        return win_flag
    else:
        win_flag = False
        return win_flag

def player_input(players, player_count):
    print()
    a, b = map(int, input(f'Ходит {players[player_count%2]}. Выберите поле: ').split(","))
    return a, b

def tictactoe(field, field_visual, player_count, players, char):
    count = 0
    while True:
        a, b = player_input(players, player_count)
        if field[a][b] != '':
            print('Выберите другое поле')
            break
        else:
            field[a][b] = char[count%2]
            field_visual[a][b] = field_visual[a][b][:1] + field[a][b] + field_visual[a][b][2:]
            vis(field_visual)
            if count >= 4:
                win_flag = win_condition(char, players, player_count)
                if win_flag == True:
                    break
            count += 1
            player_count += 1

print('Игра крестики-нолики, выбор клетки определяется вводом координат через запятую в формате "x,y"')
print('где x - номер строки, а y номер столбца, значения от 0 до 2') #проверку ввода координат не сделал
vis(field_visual)
tictactoe(field, field_visual, player_count, players, char)