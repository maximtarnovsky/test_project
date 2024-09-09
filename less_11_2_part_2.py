# ПОДГОТОВКА К ПРАКТИКЕ С НАСТАВНИКОМ
# ЗАДАЧА 3
# Создайте декоратор
# @logging
# , который будет логировать вызовы функции и ее результат. Лог должен выводиться на экран.
# Пример вывода:
#
# @logging
# def multiply(x, y):
#     return x * y
# multiply(2, 3)
# >>> Function multiply called with args: (2, 3) and kwargs: {}. Result: 6
#
# def logging(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, *kwargs)
#         print(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}. Result: {result}")
#         return result
#     return wrapper
#
#
# @logging
# def multiply_three(x, y, z):
#     return x * y * z
#
#
# multiply_three(2, 3, 8)
# Function multiplay called with args: (2, 3) and kwargs: {}. Result: 6

# ЗАДАЧА 4
# Создайте декоратор
# @memoize, который кеширует результаты функции для определенных аргументов. Если функция вызывается
# с теми же аргументами, что и в предыдущий раз, она должна возвращать результат из кеша, а не вычислять
# его заново. Также создайте два дополнительных декоратора:
# @slowit(n) — декоратор с параметрами, которые замедляют работу функции на n секунд. Без параметров декоратор
# замедляет функцию на 1 секунду. В декораторе используется функция time.sleep(n).
# @timeit — декоратор, который выводит время работы функции.
# Пример работы кода:
# # Без кеширования время работы функции при каждом вызове не менее 2 секунд.
# @timeit
# @slowit(2)
# def product(n):
#     return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None
#
# product(10)
# product(10)
#
# # С кешированием время работы функции при первом вызове не менее 2 секунд, при втором вызове почти мгновенно.
# @timeit
# @memoize
# @slowit(2)
# def product(n):
#     return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None
#
# product(10)
# product(10)

from intertools import reduce


