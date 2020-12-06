from abc import abstractmethod

'''# task 1


class Date:

    def __init__(self):
        self.data = self

    @staticmethod
    def check(data):
        if not isinstance(data, str):
            raise TypeError('атрибут должен быть строковым')
        if len(data) != 10 or data[2] != '.' or data[5] != '.' \
                or not (data[0:2].isdigit() and data[3:5].isdigit() and data[6:10].isdigit()):
            raise ValueError('текст должен содержать числовую информацию о дате в формате 01.01.0001')

    @classmethod
    def extract(cls, data):
        Date().check(data)

        for i in data.split("."):
            yield int(i)

    @staticmethod
    def validate(data):
        Date().check(data)

        if not 32 > int(data.split('.')[0]) > 0 or not 13 > int(data.split('.')[1]) > 0 \
                or not 2021 > int(data.split('.')[2]) > 0:
            print('Вы ввели недопустимые данные для даты')
        if (int(data.split('.')[0]) > 30 and int(data.split('.')[1]) in ([4, 6, 9, 11])) \
                or int(data.split('.')[0]) > 30 and int(data.split('.')[1]) == 2:
            print('Вы ввели недопустимые данные для даты')


print(list(Date().extract('14.10.1010')))
print(type(list(Date().extract('14.10.1010'))[1]))
Date().validate('31.02.2020')

# task 2


class MyError(Exception):
    pass


try:
    num = int(input("Введите целоое число: "))
    num2 = int(input("Введите второе целое число: "))
    if num2 == 0:
        raise MyError("Второе число не может быть нулём")
except MyError as e:
    print(e)
except ValueError:
    print("Вводить можно только целочисленные значения")
else:
    print(round(num / num2, 2))

# task 3


class ErCheck(Exception):

    def __init__(self):
        pass

    @staticmethod
    def check(num):
        a = num
        r = a.find('.')
        if a.isdigit() or (a[0] == '-' and a[1:].isdigit()) or \
           (a[0:r].isdigit() and a[r + 1:].isdigit() and a.count('.') == 1) \
           or (a[0] == '-' and a[1:r].isdigit() and a[r + 1:].isdigit() and a.count('.') == 1):
            num = a
            return num
        else:
            print('Вы ввели нечисловое значение')
            return False


nums = []

while True:
    b = input('Для выхода из цикла напишите только q, либо введите число: ')

    if b == 'q':
        break
    elif ErCheck.check(b) is not False:
        nums.append(ErCheck.check(b))

print('Вы не ввели никаких чисел') if len(nums) == 0 else print(f"\nВведённые вами числа: {', '.join(nums)}")

# task 7


class ComplexNum:

    def __init__(self, num, i):
        self.num = num
        self.i = i
        if not isinstance(self.num, int):
            raise TypeError("передаваемый атрибут должен быть целым числом")
        if not isinstance(self.i, int):
            raise TypeError("передаваемый атрибут должен быть целым числом")

    def __str__(self):

        if self.num == 0 and self.i != 0:
            return str(self.i) + "i"
        if self.i > 0:
            return str(self.num) + "+" + str(self.i) + "i"
        if self.i < 0:
            return str(self.num) + str(self.i) + "i"
        if self.i == 0:
            return str(self.num)

    def __add__(self, other):
        return ComplexNum(self.num + other.num, self.i + other.i)

    def __mul__(self, other):
        return ComplexNum(self.num * other.num - self.i * other.i, self.num * other.i + self.i * other.num)


c = ComplexNum(0, 1)
print(c + c + c)
print(c * c)
print(c * c + ComplexNum(1, 0))
print(ComplexNum(1, 1))

# task 4'''


class Warehouse:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.vacant = self.capacity
        self.obj_list = []
        self.obj = None
        self.place = None
        self.sent = []

    def clear(self):
        self.vacant = self.capacity
        self.obj_list.clear()

    def get(self, obj):
        self.obj = obj

        if self.vacant > 0:
            self.obj_list.append(self.obj.index)
            self.vacant -= 1
        elif self.vacant == 0:
            print('На складе закончились места!')

    def show_full(self):
        if self.vacant == self.capacity:
            print('\nНа складе ничего нет!')
        else:
            print(f'\nСписок предметов, хранящихся на складе «{self.name}»:')
            for j, i in enumerate(self.obj_list, 1):
                print(f'{j}. {i["type"]} — {i["name"]}')

    def send(self, index, place):
        self.place = place
        i = self.obj_list[index]
        s = {"type": i["type"], "name": i["name"], "place": self.place}
        self.sent.append(s)
        self.obj_list.pop(index)

    def show_sent(self):
        print(f'\nСписок предметов, переданных со склада «{self.name}»:')
        for j, i in enumerate(self.sent, 1):
            print(f'{j}. {i["type"]} — {i["name"]} (со склада получил {i["place"]})')

    def how_many(self):
        list_ = []
        list_2 = []
        print(f'\nКоличество предметов хранящихся на складе «{self.name}» по их принадлежности к типу техники: ')
        for i in self.obj_list:
            list_.append(i["type"])
        list_1 = set(list_)
        for i in list_1:
            list_2.append([i, list_.count(i)])
        for i in list_2:
            print(f'{i[0]} — {i[1]}')


class Tech:

    def __init__(self, name, is_need_net=True):
        self.name = name
        self.is_need_net = is_need_net
        self.index = {"type": "Tech", "name": self.name}
        Tech.validate(self)

    @abstractmethod
    def validate(self):
        if not isinstance(self.name, str):
            self.name = input('Введите название техники: ')


class Phone(Tech):

    def __init__(self, name, colour, is_need_net=True):
        super().__init__(name, is_need_net)
        self.colour = colour
        self.index = {"type": "Phone", "name": self.name}
        Phone.validate(self)

    def validate(self):
        if not isinstance(self.name, str):
            self.name = input('Введите модель телефона: ')


class Printer(Tech):
    def __init__(self, name, paper, color_num, is_need_net=True):
        super().__init__(name, is_need_net)
        self.paper = paper
        self.color_num = color_num
        self.index = {"type": "Printer", "name": self.name}
        Printer.validate(self)

    def validate(self):
        if not isinstance(self.name, str):
            self.name = input('Введите модель принтера: ')
        while self.paper not in ['A4', 'A5', 'A3']:
            self.paper = input('Введите наибольший формат бумаги, с которым работает принтер: ').lower()
        while self.color_num not in [1, 4]:
            self.color_num = input('Введите количество цветов, с которым работает принтер: ')
            if self.color_num.isdigit():
                self.color_num = int(self.color_num)


class Scan (Tech):
    def __init__(self, name, paper, dpi, is_need_net=False):
        super().__init__(name, is_need_net)
        self.paper = paper
        self.dpi = dpi
        self.index = {"type": "Scan", "name": self.name}
        Scan.validate(self)

    def validate(self):
        if not isinstance(self.name, str):
            self.name = input('Введите модель сканера: ')
        while self.paper not in ['A4', 'A5', 'A3']:
            self.paper = input('Введите наибольший формат бумаги, с которым работает сканер: ').lower()
        while self.dpi not in range(200, 700, 100):
            self.dpi = input('Введите максимальную глубину изображения, с которым работает сканер: ')
            if self.dpi.isdigit():
                self.dpi = int(self.dpi)


class MFP(Tech):
    def __init__(self, name, paper, color_num, dpi, is_on_wheels=False, is_need_net=True):
        super().__init__(name, is_need_net)
        self.paper = paper
        self.color_num = color_num
        self.dpi = dpi
        self.is_on_wheels = is_on_wheels
        self.index = {"type": "MFP", "name": self.name}
        MFP.validate(self)

    def validate(self):
        if not isinstance(self.name, str):
            self.name = input('Введите модель сканера: ')
        while self.paper not in ['A4', 'A5', 'A3']:
            self.paper = input('Введите наибольший формат бумаги, с которым работает сканер: ').lower()
        while self.color_num not in [1, 4]:
            self.color_num = input('Введите количество цветов, с которым работает принтер: ')
            if self.color_num.isdigit():
                self.color_num = int(self.color_num)
        while self.dpi not in range(200, 700, 100):
            self.dpi = input('Введите максимальную глубину изображения, с которым работает сканер: ')
            if self.dpi.isdigit():
                self.dpi = int(self.dpi)


w = Warehouse('Склад 1', 10)
w.show_full()
a1 = Tech('Лестница')
a2 = Tech('Диван')
w.get(a1)
w.get(a2)
w.show_full()
w.send(0, 'Строительный отдел')
w.show_sent()
a3 = Printer('LaserJet 5050', 'A3', 2)
a4 = Scan('FujiScan 3840', 'A4', 0)
a5 = MFP('Xerox V7500', 'A4', color_num=4, dpi=600)
a6 = Phone('Cisco 3050', 'Black')
a0 = [a3, a4, a5, a6, a3, a4, a5, Phone('Siemens A150', 'Silver'), a3, a5]
for y in a0:
    w.get(y)
w.show_full()
w.how_many()
for y in range(0, 4, 2):
    for yy in ['Отдел маркетинга', 'Отдел продаж', 'Строительный отдел']:
        w.send(y, yy)
w.show_sent()
w.show_full()
