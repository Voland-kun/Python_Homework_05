#Создайте программу для игры с конфетами человек против человека.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Игрок с игроком

from random import randint

def coinflip():
    count = randint(0, 1)
    print('Бросок монеты:')
    if count == 1:
        print(f'Выпала решка, первым ходит {players[(count+1)%2]}')
    else:
        print(f'Выпал орёл, первым ходит {players[(count+1)%2]}')
    return count

def input_candy(description, candy=28):
    while True:
        try:
            user_number = input(description)
            user_number = int(user_number)
            if 0 < user_number <= candy:
                return user_number
            else:
                print('Неверное количество конфет.')
        except ValueError:
            pass

#player1_pocket = 0
#player2_pocket = 0
table = 2021
player1 = 'Игрок'
player2 = 'Скайнет'
players = [player1, player2]

def candy_game(table, count, players):
    while table != 0:
        count += 1
        if table < 28:
            if count%2 == 0:
                pickup = input_candy(f'Ходит {players[count%2]}. Сколько конфет взять? ', table)
            else:
                pickup = table
                print(f'{players[count%2]} взял {pickup} конфет')
            table -= pickup
        else:
            if count%2 == 0:
                pickup = input_candy(f'Ходит {players[count%2]}. Сколько конфет взять? ',)
            else:
                if table % 29 != 0:
                    pickup = table %29
                else:
                    pickup = randint(1, 28)
                print(f'{players[count%2]} взял {pickup} конфет')
            table -= pickup
        print(f'Осталось {table} конфет')
    print(f'Победил {players[count%2]}')

print('\033[32m{}'.format('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.'))
print('За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.) ')
print('\033[0m')
count = coinflip()
candy_game(table, count, players)