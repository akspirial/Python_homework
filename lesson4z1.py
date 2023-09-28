import random

def unical_numbers():
    ''''Эта функция находит уникалные числа которые встречаются в обоих наборах '''
    try:
        n = int(input('Введите кол-во элементов в первом списке  '))
        m = int(input('Введите кол-во элементов во втором списке   '))
        lst1 = [random.randint(1,100) for _ in range(n)] 
        lst2 = [random.randint(1,100) for _ in range(m)]
        result = set(lst1) & set(lst2)
        if len(result) == 0:
            return f"Уникальные числа которые встречаются в обоих наборах не найдены ({set(lst1)} и {set(lst2)}) - не пересекаются"
        return f'{set(lst1) & set(lst2)} - Это уникальные числа которые встречаются в обоих наборах '
    except TypeError:
        return 'Неверный ввод данных'
    except ValueError:
        return 'Нверный ввод данных'
    except KeyboardInterrupt:
        return 'Вы ввели не все данные'

print(unical_numbers())