#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#50 -> 1, 2, 4, 8, 16, 32

#def step2():
 #   try:
  #      n = int(input('Введите число N: '))
#
 #       num1 = []
  #      num1 = [2**i for i in range(1,n) if 2**i < n]
   #     if len(num1) !=0:
    #        return f'{num1}'
     #   elif len(num1) ==0:
      #      return f'нужные числа отсутствуют'
    #except ValueError:
     #   return 'Вы ввели не число'
    #except KeyboardInterrupt:
     #   return "Ведены не все данные"
#print(step2())



n = int(input('Введите число N: '))
num = 0.5
while num < n:
    if(num < n):
        if (num * 2 > n):
            break
        else:
            num = num * 2
            print(num)

