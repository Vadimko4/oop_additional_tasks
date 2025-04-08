import datetime

"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""


class Car:

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        if year <= datetime.datetime.now().year:
            self.year = year
        else:
            raise ValueError('Год выпуска не может быть больше текущего')


# код для проверки
car = Car('Toyota', 'Corolla', 2022)

car1 = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
