#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#50 -> 1, 2, 4, 8, 16, 32

n = int(input('Введите число N: '))
num = 1
while num < n:
    if(num < n):
        if (num * 2 > n):
            break
        else:
            num = num * 2
            print(num)