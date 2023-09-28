import random

def bluberry():
    '''Эта функция собирает ягоды с этого куста и с двух соседних с ним за 1 заход'''
    try:
        m = int(input('Введите количество кустов   '))
        bushes = [random.randint(1,100) for _ in range(m)]
        n = len(bushes)
        max_harvest = 0

        for i in range(n):
            harvest = bushes[i] + bushes[(i+1) % n] + bushes[(i+2) % n]
            max_harvest = max(max_harvest, harvest)
        return f'Максимальное количество ягод собранное за один заход модуля  {max_harvest}'
    except TypeError:
        return 'Неверный ввод данных'
    except ValueError:
        return 'Нверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы ввели не все данные'
print(bluberry())