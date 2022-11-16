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
