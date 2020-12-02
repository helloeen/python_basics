from abc import abstractmethod

# task 1

x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

z = [[0.2]]
zz = [[15.1]]


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

        if not isinstance(self.matrix, list):
            raise TypeError("передаваемый атрибут должен быть списком списков")

        for el in self.matrix:

            if not isinstance(el, list):
                raise TypeError("передаваемый атрибут должен быть списком списков")

    def __str__(self):

        return '\n'.join(' '.join(str(column) for column in row) for row in self.matrix)

    def __add__(self, other):

        result = [[(self.matrix[i][j] + other.matrix[i][j]) for j in range(len(self.matrix[0]))] for i in
                  range(len(self.matrix))]

        return Matrix([r for r in result])


print(f'{Matrix(x)}\n')
print(f"{Matrix(y)}\n")
print(f"{Matrix(x) + Matrix(y) + Matrix(x)}\n")
print(Matrix(z) + Matrix(zz) + Matrix(z))


# task 2

class Clothes:

    def __init__(self, name, size=0, height=0):
        self.name = name
        self.size = size
        self.height = height
        self.s = 0

    def __str__(self):
        if self.s > 0:
            return f"\n{self.name} имеет площадь {self.s}"
        if self.s == 0:
            return f"\n{self.name}"
        if self.s < 0:
            return f"\n{self.name} не существует в привычной нам реальности"

    def __add__(self, other):
        return self.s + other.s if self.s + other.s > 0 else 0  # f'Нереальная площадь стала нулём'

    # хотелось поинтереснее реализовать как-нибудь через класс, но времени катастрофически не хватает, поэтому tuple ):

    @property
    @abstractmethod
    def square(self):
        self.s = round((self.size / 6.5 + 0.5), 2) + round((self.height * 2 + 0.3), 2)
        return self.s

    @square.setter
    def square(self, s):
        if s < 1 or s > 100:
            self.s = 0
            print('Что это вообще за площадь для одежды такая?')
        else:
            self.s = s


class Coat(Clothes):

    def __init__(self, size, name='Coat', height=0):
        super().__init__(name, size, height)

    @property
    def square(self):
        self.s = round((self.size / 6.5 + 0.5), 2)
        return self.s

    @square.setter
    def square(self, s):
        if s < 1 or s > 100:
            self.s = 0
            print('Что это вообще за площадь для одежды такая?')
        else:
            self.s = s


class Suit(Clothes):

    def __init__(self, height, name='Suit', size=0):
        super().__init__(name, size, height)

    @property
    def square(self):
        self.s = round((self.height * 2 + 0.3), 2)
        return self.s

    @square.setter
    def square(self, s):
        if s < 1 or s > 100:
            self.s = 0
            print('Что это вообще за площадь для одежды такая?')
        else:
            self.s = s


a = Clothes('Clothes', 10, 10)
b = Coat(100)
c = Suit(-100)
print(a.size, a.height, a.square)
print(b.name, b.square, b.size, c.name, c.square, c.height)
print(a, b, c)
print(c + b)
b.square = 101
print(b.s)
print(a + c)


# task 3

class Cell:

    def __init__(self, num):
        self.num = num
        self.line = None
        if not isinstance(self.num, int) or not self.num > 0:
            raise TypeError("передаваемый атрибут должен быть целым числом больше нуля")
        self.show = "*" * self.num
        self.nominal = self.show

    def __str__(self):
        return self.show

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        return Cell(self.num - other.num) if self.num > other.num else "Вычитать можно только из большей клетки меньшую!"

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num) if self.num // other.num != 0 else "Делить можно только большую клетку на меньшую!"

    def make_order(self, line):
        self.line = line
        unsorted = self.show
        unsorted = unsorted.replace("*" * self.line, "+" * self.line + "\n")
        if unsorted[-1] == '\n':
            unsorted = unsorted[:-1]
        unsorted = unsorted.replace("*", "+")
        self.show = unsorted.replace("+", "*")
        return self.show

    def set_nominal(self):
        self.show = self.nominal


a = Cell(10)
print(a.show)
a.make_order(5)
print(a)
a.set_nominal()
print(a)
b = Cell(7)
print(a + b)
print(Cell(100)-Cell(25)-Cell(70))
print(a - Cell(11))
print((a * b).make_order(25))
print(a / b)
print(Cell(20) / Cell(25))

