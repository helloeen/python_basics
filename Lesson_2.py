# task 1

list1 = [1, 1.5, complex(15, -7), [0, 55], (2, 74), {23, 8}, 'py', None, {11: 'word'}, 4 < 6]
print(list1)
what_type = []

for i in range(len(list1)):
    a = str(type(list1[i]))[8:-2]
    what_type.append(a)

print(what_type)

# task 2

user_list = input('\nВведите элементы списка, разделяя запятой: ').split(',')
print(user_list)

for i in range(1, len(user_list), 2):
    user_list[i], user_list[i - 1] = user_list[i - 1], user_list[i]

print(f"{user_list}\n")

# task 3

m = 0
num = [str(a) for a in range(1, 13)]
m_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
m_dict = {'1': 'зима', '2': 'зима', '3': 'весна', '4': 'весна', '5': 'весна', '6': 'лето',
          '7': 'лето', '8': 'лето', '9': 'осень', '10': 'осень', '11': 'осень', '12': 'зима'}

while m not in num:
    m = input('Введите порядковый номер месяца, чтобы узнать к какому времени года он относится: ')

print(f"{m}-й месяц относится ко времени года {m_list[int(m) - 1]} — решение выполнено при помощи списка")
print(f"{m}-й месяц относится ко времени года {m_dict[m]} — решение выполнено при помощи словаря\n")

# task 4

user_list = input('Введите элементы списка, разделяя пробелом: ').split(' ')

for i, ii in enumerate(user_list, 1):
    print(i, ii[:10])

# task 5

rating = [100, 50, 25, 10, 5]
print(f"\nИзначальный рейтинг: {rating}")
m = '0'

while m == '0' or m.isdigit() is False:
    m = input('Введите любое натуральное число: ')

m = int(m)

for i in range(len(rating)):
    if m > rating[i]:
        rating.insert(i, m)
        break
    elif m == rating[i] or (i == len(rating) - 1 and m < rating[len(rating)-1]):
        rating.insert(i + 1, m)
        break

print(f"{rating}\n")

# task 6

m = 0

while m not in ['2', '3']:
    m = input('Введите колчество товаров на вашем складе «для проверки огрничимся двумя или тремя»: ')

m = int(m)
goods_list = []

for i in range(m):
    goods_tuple = []
    goods_tuple.append(i + 1)

    name = input('\nВведите название товара: ').lower()
    cost = '0'
    while cost.isdigit() is False or cost == '0':
        cost = input('Введите целочисленную стоимость товара в рублях большую нуля: ')
    cost = int(cost)
    measure = input('Введите единицы учёта товара: ').lower()
    q = 'q'
    while q.isdigit() is False:
        q = input('Введите не отрицательное целочисленное количество товара в указанных единицах учёта: ')
    q = int(q)
    goods_dict = {'название': name, 'цена': cost, 'количество': q, 'ед. учёта': measure}


    goods_tuple.append(goods_dict)
    goods_tuple = tuple(goods_tuple)
    goods_list.append(goods_tuple)

print('\nструктура данных «Товары» представлена ниже:')
print(goods_list)

names = []
costs = []
qs = []
measures = []

for i in range(m):
    dict_val = goods_list[i][1]
    names.append(dict_val['название'])
    costs.append(dict_val['цена'])
    qs.append(dict_val['количество'])
    measures.append(dict_val['ед. учёта'])

anal_dict = {'название': list(set(names)), 'цена': list(set(costs)),
             'количество': list(set(qs)), 'ед. учёта': list(set(measures))}
print('\nсловарь с проанализированными данными представлен ниже:')
print(anal_dict)
