"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        min_denominator = min(self.denominator, other.denominator)
        if min_denominator == self.denominator:
            less = 'self'
        else:
            less = 'other'
        for i in range(min_denominator, 0, -1):
            if self.denominator % i == 0 and other.denominator % i == 0:
                common_mult = i
                break
        self_mult = self.denominator // common_mult
        other_mult = other.denominator // common_mult
        lowest_common_denominator = common_mult * self_mult * other_mult
        result_numerator = self.numerator * other_mult + other.numerator * self_mult
        return Fraction(result_numerator, lowest_common_denominator)


# код для проверки 
fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
