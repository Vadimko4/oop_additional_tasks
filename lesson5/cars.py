import timeit

"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходи получение, присваивание и удаление значения.
"""


class Car:

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def get_set_del(self):
        self.name += " - new"
        del self.year
        self.year = 0


class CarSlots(Car):
    __slots__ = ('name', 'model', 'year')

    # def __init__(self, name, model, year):
    #     self.name = name
    #     self.model = model
    #     self.year = year
    #
    # def get_set_del(self):
    #     self.name += " - new"
    #     del self.year
    #     self.year = 0


car = Car('Toyota', 'Corolla', 2022)
car_slots = Car('Toyota', 'Crown', 1990)

car.get_set_del()
car_slots.get_set_del()

print(car.year)
print(car_slots.year)

t1 = timeit.timeit('car.get_set_del()', globals=globals(), number=1000)
t2 = timeit.timeit('car_slots.get_set_del', globals=globals(), number=1000)
print((t1-t2)/t1*100)
