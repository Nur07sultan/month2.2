# homework_4.py

from datetime import datetime as dt
from time import sleep


def checktime(func):
    def wrapper(*args, **kwargs):
        time_now = dt.now()
        print(f"Функция была вызвана в {time_now.hour:02d}:{time_now.minute:02d}:{time_now.second:02d} "
              f"{time_now.day:02d}/{time_now.month:02d}/{time_now.year}")
        return func(*args, **kwargs)
    return wrapper


def checktime_before_after(func):
    def wrapper(*args, **kwargs):
        start_time = dt.now()
        print(f"Функция была вызвана в {start_time.hour:02d}:{start_time.minute:02d}:{start_time.second:02d} "
              f"{start_time.day:02d}/{start_time.month:02d}/{start_time.year}")

        result = func(*args, **kwargs)

        end_time = dt.now()
        print(f"Функция была закончена в {end_time.hour:02d}:{end_time.minute:02d}:{end_time.second:02d} "
              f"{end_time.day:02d}/{end_time.month:02d}/{end_time.year}")
        return result
    return wrapper


@checktime
def hello_world():
    print("hello world")


@checktime_before_after
def hello_world_long():
    print("hello world")
    sleep(1)  # имитация долгой работы


# Проверка работы
hello_world()
print()
hello_world_long()