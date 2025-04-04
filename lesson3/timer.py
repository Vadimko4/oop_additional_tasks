import time

"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""


class Timer:

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        # print(f"Время выполнения: {self.end - self.start} секунд")
        self.elapsed_time = self.end - self.start
        return self


with Timer() as timer:
    # блок кода
    for i in range(10 ** 8):
        flag = True
    # код для проверки 
print("Execution time:", timer.elapsed_time)
