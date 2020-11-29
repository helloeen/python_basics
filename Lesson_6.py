from time import sleep
from itertools import cycle

# task 1 доделать здесь нужно переключение режимов


class TrafficLight:
    __colour = cycle([['red', 7], ['yellow', 2], ['green', 5], ['yellow', 2]])

    def running(self):
        k = next(self.__colour)
        print(k[0])
        sleep(k[1])


a = TrafficLight()
for i in range(5):
    a.running()


# task 2


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return self._length * self._width * 25 * 5 / 1000


a = Road(20, 5000)
print(f"Масса асфальта необходимого для покрытия всего дорожного полотна равна {a.mass()} т")


# task 3


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        if not isinstance(self._income, dict):
            raise TypeError("передаваемый атрибут должен быть словарём")
        if list(self._income.keys()) != ['wage', 'bonus']:
            raise KeyError("Словарю переданы неверные значения ключей: должны быть 'wage', 'bonus'")
        for el in self._income.values():
            if not isinstance(el, int):
                raise TypeError("Значения ключей словаря должны быть целочисленными числами")


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Зоя', 'Фрэйхт', 'Секретарь', {'wage': 10000, 'bonus': 5000})
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
b = Worker('Артём', 'Тулов', 'Механик', {'wage': 38520, 'bonus': 1000})
print(b.name)
print(b.surname)
print(b._income)


# task 4

class Car:

    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police
        if not isinstance(self.is_police, bool):
            raise TypeError("передаваемый атрибут должен логическим типом данных")
        self.direction = None
        self.base_speed = speed

    def go(self):
        print(f'{self.name} поехал(а)')
        self.speed = self.base_speed

    def stop(self):
        print(f'{self.name} выжал(а) тормоза полностью')
        self.speed = 0

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернул(а) {self.direction}')

    def show_speed(self):
        print(f"{self.name} имеет скорость равную {self.speed} км/ч")


class TownCar(Car):

    def __init__(self, speed=65, colour='Белый', name='Тихоход', is_police=False):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):

        if self.speed > 60:
            print(f"{self.name} имеет скорость равную {self.speed} км/ч и превышающую допустимую")
        else:
            print(f"{self.name} имеет скорость равную {self.speed} км/ч")


class SportCar(Car):

    def __init__(self, speed=120, colour='Красный', name='Ferrari', is_police=False):
        super().__init__(speed, colour, name, is_police)


class WorkCar(Car):

    def __init__(self, speed=50, colour='Коричневый', name='Камаз', is_police=False):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):

        if self.speed > 40:
            print(f"{self.name} имеет скорость равную {self.speed} км/ч и превышающую допустимую")
        else:
            print(f"{self.name} имеет скорость равную {self.speed} км/ч")


class PoliceCar(Car):

    def __init__(self, speed=100, colour='Чёрный', name='Corvette', is_police=True):
        super().__init__(speed, colour, name, is_police)


a = Car(80, 'Красный', 'Бибизика')
a.stop()
a.show_speed()
a.go()
a.show_speed()
a.turn('влево')
print(a.direction)
print(a.is_police)
b = TownCar()
print(b.speed)
b.show_speed()
b.stop()
b.show_speed()
c = SportCar()
c.show_speed()
print(c.name)
d = WorkCar()
d.show_speed()
d.speed = 35
d.show_speed()
e = PoliceCar()
print(e.is_police)
print(e.colour)
e.turn('Назад')

# task 5


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки при помощи {self.title}')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки при помощи ручки {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки при помощи карандаша {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки при помощи маркера {self.title}')


Stationery('мелка').draw()
Pen('Erich Krause').draw()
Pencil('Koh-I-Noor Hardtmuth').draw()
Handle('Brauberg Pro').draw()
