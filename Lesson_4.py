from sys import argv
from functools import reduce
from itertools import count, cycle

# task 1

try:
    path, rate, hours, premium = argv

    def salary(rate1, hours1, premium1):
        while not premium1.isdigit() and not (premium1[0] == '-' and premium1[1:].isdigit()):
            premium1 = input('Введите размер целочисленной премии в рублях (может быть отрицательной, как штраф): ')
        while not rate1.isdigit() or rate1 == '0':
            rate1 = input('Введите целочисленное значние часовой ставки в рублях: ')
        while not hours1.isdigit() or hours1 == '0':
            hours1 = input('Введите целочисленное количество отработанных часов: ')
        result = (int(rate1) * int(hours1)) + int(premium1)
        return result

except ValueError:
    print('Значения программе передаются через терминал.')

else:
    print(f"Зарплата сотрудника при указаных данных: {salary(rate, hours, premium)} руб.")

# task 2

non_sorted = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"\nИзначальный список: {non_sorted}")
sorted_list = [non_sorted[i] for i in range(1, len(non_sorted)) if non_sorted[i] > non_sorted[i - 1]]
print(f"Список из чисел изначального списка, что больше предыдущего: {sorted_list}\n")

# task 3

list2021 = [str(i) for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(f"В диапозоне чисел от 20 до 240: {', '.join(list2021)} — кратны 20 или 21.")

# task 4

non_sorted = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"\nИзначальный список: {non_sorted}")
sorted_list = [i for i in non_sorted if non_sorted.count(i) == 1]
print(f"Список из чисел изначального списка, что представлены единожды: {sorted_list}\n")

# task 5


def multy(a1, a2):
    return a1 * a2


even = [i for i in range(100, 1001, 2)]
res = reduce(multy, even)
print(f"Результат перемножения всех чётных чисел от 100 до 1000 равен: {str(res)[0:1]}.{str(round(int(str(res)[1:4])))}"
      f"+e{len(str(res))-1}\n")

# task 6

num = []

for i in count(3, 3):
    if i < 100:
        num.append(str(i))
    else:
        break

print(', '.join(num))

j = 0

num.clear()

for i in cycle('REPEAT'):
    if j < 11:
        num.append(i)
        j += 1
    else:
        break
print(f"{', '.join(num)}\n")

'''# task 6.5

num = []

for i in count(3, 3):
    if i < 100:
        num.append(str(i))
    else:
        break

print(', '.join(num))

j = 0
num1 = []

for i in cycle(num):
    if j < 11:
        num1.append(i)
        j += 1
    else:
        break

print(f"{', '.join(num1)}\n")

j = 0

itera = cycle(num)
num1.clear()

while j < 11:
    num1.append(next(itera))
    j += 1

print(num1)

j = 0
itera = count(3, 3)
num1.clear()

while j < 11:
    num1.append(next(itera))
    j += 1

print(num1)'''


# task 7


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def gen(n):
    while not n.isdigit() or n == '0':
        n = input("Введите неотрицательное целое число: ")
    n = int(n)

    for el in range(1, n + 1):
        yield [str(el)+'!=', fact(el)]


a = gen('s')
a = list(a)
print(f"\nСписок факториалов для диапазона чисел от 1 до указанного:")
for i in a:
    print(f"{i[0]}{i[1]}")
