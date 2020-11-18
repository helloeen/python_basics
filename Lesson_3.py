# task 1

def f(a, b):
    while not a.isdigit() and not (a[0] == '-' and a[1:].isdigit()):
        a = input('Введите первое целое число: ')
    while not b.isdigit() and not (b[0] == '-' and b[1:].isdigit()) or b == '0':
        b = input('Введите второе целое число кроме нуля: ')
    print(f"Результат деления первого числа на второе с точностью до 2 знаков после запятой: {(int(a) / int(b)):.2f}")


f("a", 'b')

# task 2


def info(name, sur, year, city, mail, phone):
    print(f"\n{name} {sur}, {year} года рождения, живёт в городе, именуемым {city},"
          f" контакты для связи — тел: {phone}, @mail: {mail}\n")


info(name='Юля', sur='Собакина', year=2000, phone='+7 (495) 123-45-67', mail='julia@mail.ru', city='Москва')

# task 3


def max_sum(a, b, c):
    d = [a, b, c]
    d.remove(min(a, b, c))
    return sum(d)


print(f"Cумма наибольших чисел из ряда: 100, -25 и 100 равна: {max_sum(100, -25, 100)}\n")

# task 4


def expo(x, y):

    while not x.isdigit() or x == '0':
        x = input('Введите первое целое положительное число: ')
    while not (y[0] == '-' and y[1:].isdigit()):
        y = input('Введите второе отрицательное целое число: ')
    print(f"\nРезультат возведения первого числа в степень равную второму с точностью до 10 знаков после запятой: "
          f"{round(int(x) ** int(y), 10)}")
    res = int(x)
    for i in range(int(y[1:])-1):
        res *= int(x)
    print(f"Результат возведения первого числа в степень равную второму с точностью до 10 знаков после запятой: "
          f"{round(1 / res, 10)}")


expo('s', 'b')

# task 5


def str_sum():
    while True:
        user_str = input('\nДля окончания игр с суммами чисел напишите «q» вначале, '
                         'либо через пробел посреди набора чисел\nВведите ряд целых чисел, разделённых пробелом: ')
        num_list = user_str.split()
        i = 0
        for n in num_list:
            if not n.isdigit() and not (n[0] == '-' and n[1:].isdigit()) and n != 'q':
                i += 1
        if i == 0:
            break
    list_sum = 0
    if 'q' in num_list:
        for i in range(num_list.index('q')):
            list_sum = list_sum + int(num_list.pop(0))
        print(f"Сумма чисел введённого ряда: {list_sum}")
        return list_sum, 'exit'
    num_list = [int(n) for n in num_list]
    list_sum = sum(num_list)

    print(f"Сумма чисел введённого ряда: {list_sum}")
    return list_sum, 'continue'


def continue_sum():
    cycle_sum = 0

    while True:
        fin = str_sum()
        if fin[1] == 'exit':
            cycle_sum = fin[0] + cycle_sum
            print(f"Просмотр вылетающих сумм окончен. Сумма чисел всех введённых рядов чисел: {cycle_sum}")
            break
        if fin[1] == 'continue':
            cycle_sum = fin[0] + cycle_sum
        print(f"Просмотр вылетающих сумм продолжается. Сумма чисел всех введённых рядов чисел: {cycle_sum}")


continue_sum()

# task 6


def int_func(a):
    while not a.isalpha() or not a.islower():
        a = input('Введите набор только буквенных символов нижнего регистра, желательно образующих слово: ')
    return a.title()


def is_latin(a):
    while True:
        user_words = a.split()
        i = 0
        for n in user_words:
            if not n.isalpha():
                i += 1
        if i == 0:
            break
        a = input('Введите набор только буквенных символов нижнего регистра, разделённых пробелами, '
                  'желательно образующих слова: ')
    checklist1 = [i for i in range(65, 91)]
    checklist2 = [i for i in range(97, 123)]
    num = set(checklist1).union(set(checklist2))
    num = list(num)
    only_latin = []
    for n in user_words:
        i = 0
        for k in n:
            letter = ord(k)
            if letter not in num:
                i += 1
        if i == 0:
            only_latin.append(n)

    for i in range(len(only_latin)):
        only_latin[i] = int_func(only_latin[i])

    a = ' '.join(only_latin)
    print(f"\nВ указанных словах только эти написаны латиницей, за это мы им изменили регистр у первых букв: {a}")


example = input('\nВведите набор только буквенных символов нижнего регистра, желательно образующих слово: ')
print(f"\nСмотрите, как указанное слово выглядит красиво с заглавной первой буквой: {int_func(example)}\n")

example = input('Введите набор только буквенных символов нижнего регистра, разделённых пробелами, '
                'желательно образующих слова: ')
is_latin(example)
