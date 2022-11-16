# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

all_nums = list(map(int, input().split()))
res_nums = list(filter(lambda x: len(x) == 2, all_nums))
print(res_nums)



# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

list1 = input().split()

list2 = list(filter(lambda x: x.isdigit(), list1))
list3 = list(filter(lambda x: x.isdigit()== False, list1))
print(list2, list3)



# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
num = input('Введите вещественное число: ')
result = sum(map(int, num.replace(',', '').replace('.', '').replace('-', '')))
print(result)



# # 2) Игра в конфеты игрок против умного бота
from random import randint

def game():
    candies = 22
    max_take = 3
    count = 0
    bot = 'Bot'
    player = input('players name ')


    a = randint(1,2)
    if a==1:
        start = bot
        finish = player
        print('Bot start ')
    else:
        start = player
        finish = bot
        print('Player start ')


    while candies > 0:

        if count == 0:

            if start == bot:

                neeed_to_take = candies%(max_take+1)
                if neeed_to_take == 0:
                    candies = candies-1
                    print('Boot is taking 1 candies')
                    count = 1
                
                candies = candies-neeed_to_take
                print(f'Bot is takingg {neeed_to_take} candies')
                if candies == 0:
                    print(f'Bot won')
                else:
                    print(f'Bot finish his turn and overrall candies{candies}')
                    count = 1

                


            if start == player:
                turn = int(input(f'{start} how much candies u want to take? '))
                if turn > max_take or turn > candies:
                    print(f'Take {max_take} or less candies plz ')
                else:
                    candies -= turn
                if candies == 0:
                    print(f'{start} u won!') 
                else:
                    print(f'{finish} ur turn and overall candies {candies} ')
                    count = 1

        if count == 1:

            if finish == bot:

                neeed_to_take = candies%(max_take+1)
                if neeed_to_take == 0:
                    candies = candies-1
                    print('Bot is taking 1 candies')
                    count = 0
                else:
                    candies = candies-neeed_to_take
                    print(f'Bot is taking {neeed_to_take} candies')
                    if candies == 0:
                        print(f'Bot won')
                    else:
                        print(f'Bot finish his turn and overall candies{candies}')
                        count = 0


            else:
            
                turn = int(input(f'{finish} how much candies u want to take? '))
                if turn > max_take or turn > candies:
                    print(f'Take {max_take} or less candies plz ')

                candies -= turn
                if candies == 0:
                    print(f'{finish} u won!') 
                else:
                    print(f'{start} ur turn and overall candies {candies} ')
                    count = 0

game()