# Добавил еще остаток от деления
class Customfloat:

    @staticmethod  # НОД
    def get_nod(a, b):
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        while b != 0:
            a, b = b, a % b
        if a == 0:
            return 1
        return a

    def __init__(self, num: int, denum: int):
        nod = self.get_nod(num, denum)
        self.num = num // nod
        self.denum = denum // nod

    def __str__(self):
        nod = self.get_nod(self.num, self.denum)
        return f'{self.num // nod}\\{self.denum // nod}'

    def __add__(self, other):  # +
        if isinstance(other, Customfloat):
            return Customfloat(self.num * other.denum + other.num * self.denum, self.denum * other.denum)
        else:
            return Customfloat(self.num + other * self.denum, self.denum)

    def __sub__(self, other):  # -
        pass
        if isinstance(other, Customfloat):
            return Customfloat(self.num * other.denum - other.num * self.denum, self.denum * other.denum)
        else:
            return Customfloat(self.num - other * self.denum, self.denum)

    def __mul__(self, other):  # *
        if isinstance(other, Customfloat):
            return Customfloat(self.num * other.num, self.denum * other.denum)
        else:
            return Customfloat(self.num * other, self.denum)

    def __truediv__(self, other):  # /
        if isinstance(other, Customfloat):
            if other.num == 0:
                raise ZeroDivisionError("division by zero")  # Взял из int
            else:
                return Customfloat(self.num * other.denum, self.denum * other.num)
        else:
            if other == 0:
                raise ZeroDivisionError("division by zero")
            elif other < 0:
                return Customfloat(self.num * -1, self.denum * other * -1)
            else:
                return Customfloat(self.num, self.denum * other)

    def __mod__(self, other):  # %
        if isinstance(other, Customfloat):
            if other.num == 0:
                raise ZeroDivisionError("division by zero")  # Взял из int
            else:
                return Customfloat((self.num * other.denum) % (other.num * self.denum), self.denum * other.denum)
        else:
            if other == 0:
                raise ZeroDivisionError("division by zero")
            else:
                return Customfloat(self.num % (other * self.denum), self.denum)

    def __eq__(self, other):  # ==
        if isinstance(other, Customfloat):
            return self.num * other.denum == self.denum * other.num
        else:
            return False

    def __lt__(self, other):  # <
        if isinstance(other, Customfloat):
            return self.num * other.denum < self.denum * other.num
        else:
            return False

    def __gt__(self, other):  # >
        if isinstance(other, Customfloat):
            return self.num * other.denum > self.denum * other.num
        else:
            return False

    def __le__(self, other):  # <=
        return self < other or self == other

    def __ge__(self, other):  # >=
        return self > other or self == other

