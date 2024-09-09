# # Определение декоратора:
# def printing(function):
#     def inner(*args, **kwargs):
#         result = function(*args, **kwargs)
#         print('result =', result)
#         return result
#     return inner
#
# # Применение декоратора
# @printing
# def add_one(x):
#     return x + 1
#
# y = add_one(10)
# # >>> result = 11
# print(y)
# # >>> 11

# 11.2.4 Самостоятельная практика

# # Задача 1
# # Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой
# # функцией, являются целыми, и округляет их до целых, если это не так.
#
# def check_integers(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         # Проверка на тип с использованием type()
#         if type(result) == float:
#             return round(result)
#         elif type(result) in (list, tuple):
#             rounded = [round(x) if type(x) == float else x for x in result]
#             # Возвращаем тот же тип, что и исходный (list или tuple)
#             return type(result)(rounded)
#         else:
#             return result
#     return wrapper
#
# @check_integers
# def numbers(x):
#     return x
#
# y = numbers((1, 2, 3.3, 5, 3.14, 41))
# print(y)

# # Задача 2
# # Напишите декоратор, который повторно вызывает декорируемую функцию
# # три раза, каждый раз через три секунды, если произошла ошибка.
#
# import time
#
# def retry(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             try:
#                 return func(*args, **kwargs)
#             except:
#                 time.sleep(3)
#         raise Exception('Function call failed after multiple retries.')
#     return wrapper
#
# @retry
# def add_one(x):
#     return x + 10

# # # Задача 3
# # # Напишите декоратор, который позволяет возвращать элементы декорируемой функции
# # # по одному через yield, если эта функция возвращает список или кортеж.
#
# def yield_items(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         # Проверка на тип с использованием type()
#         if type(result) in (list, tuple):
#             for item in result:
#                 yield item
#         else:
#             yield result
#     return wrapper
#
# @yield_items
# def list_lists(x):
#     return x

# y = list_lists([1,2,3,4,5,6,7,8])
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

# for _ in range(6):
#     print(next(y))

# Задача 4
# Напишите декоратор, который берет результат декорируемой функции (текст) и
# возвращает текст, в котором каждое слово сокращено до 8 символов. Если слово
# было сокращено, в конце слова ставится точка.

# def shorten_words(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         words = result.split()
#         shortened_words = []
#         for word in words:
#             if len(word) > 8:
#                 shortened_word = word[:8] + "."
#                 shortened_words.append(shortened_word)
#             else:
#                 shortened_words.append(word)
#         return " ".join(shortened_words)
#     return wrapper


# # Вариант решения, в котором логика сокращения слова записана в одну строчку:
#
# def shorten_words(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return " ".join(f"{word[:8]}." if len(word) > 8 else word for word in result.split())
#
#     return wrapper
#
# @shorten_words
# def strings(x):
#     return x
#
# y = strings("У Лукоморья дуб зелёный. Новосибисрск прекрасный сибирский мегаполис. Сложносочинённость")
# print(y)


# # Задача 5
# # Напишите три декоратора, которые можно применять последовательно к результату декорируемой функции.
# # Первый декоратор должен заменять в тексте, который выдает функция, все восклицательные знаки ! на !!!.
# # Второй декоратор должен заменять в тексте, который выдает функция, все знаки вопроса ? на ???.
# # Третий декоратор должен заменять в тексте, который выдает функция, все точки . на ... .
#
# def exclamation_marks(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.replace("!", "!!!")
#     return wrapper
#
# def question_marks(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.replace("?", "???")
#     return wrapper
#
# def dots(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.replace(".", "...")
#     return wrapper
#
# # Вызов декораторов:
#
# @exclamation_marks
# @question_marks
# @dots
# def my_function():
#     return "This is a sentence. It has a question? Does it need more exclamation!"
#
# print(my_function())

# 11.2.8 Самостоятельная практика

# Задача 1
# Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
# являются целыми, и округляет их до целых, если это не так. Декоратор должен принимать параметр
# precision, который указывает, до скольких цифр после запятой округлять числа.

# from functools import wraps
#
# def check_floats(precision):
#     def decorator(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             result = func(*args, **kwargs)
#             # Проверка на тип с использованием type()
#             if type(result) == float:
#                 return round(result, precision)
#             elif type(result) in (list, tuple):
#                 rounded = [round(x, precision) if type(x) == float else x for x in result]
#                 return type(result)(rounded)
#             else:
#                 return result
#         return inner
#     return decorator

# @check_floats(2)
# def numbers(x):
#     return x
#
# y = numbers((1, 2, 3.3, 5, 3.14, 41))
# print(y)


# Задача 2
# Напишите декоратор, который повторно вызывает декорируемую функцию
# заданное количество раз через заданное время, если произошла ошибка.
# Параметры, передаваемые в декоратор, обязательно должны быть именованными.

# from functools import wraps
# import time
#
# def retry(*, retries=3, delay=3):
#     def wrapper(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             for i in range(retries):
#                 try:
#                     return func(*args, **kwargs)
#                 except:
#                     time.sleep(delay)
#             raise Exception('Function call failed after multiple retries.')
#         return inner
#     return wrapper


# Задача 3
# Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
# в котором каждое слово сокращено до определенной длины. Если слово было сокращено, в конце слова
# ставится переданный символ. Количество символов в слове и знак в конце сокращенного слова —
# параметры декоратора, причем символ обязательно должен передаваться как именованный аргумент.

from functools import wraps

def shorten_words(max_len, *, end_symbol='.'):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return " ".join(f"{word[:max_len]}{end_symbol}" if len(word) > max_len else word for word in result.split())
        return inner
    return wrapper

# Пример использования:
# @shorten_words(4, end_symbol='!')
# def some_func():
#     return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
#
# print(some_func())


# Задача 4
# Напишите тесты с использованием библиотеки pytest для проверки корректности работы декоратора из задачи 3.

import pytest

# Тестируемая функция
@shorten_words(4, end_symbol='!')
def get_text():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# Тесты
def test_shortening():
    assert get_text() == "Lore! ipsu! dolo! sit amet! cons! adip! elit!"

def test_no_shortening():
    @shorten_words(10, end_symbol='!')
    def get_long_text():
        return "Lorem ipsum dolor sit amet"
    assert get_long_text() == "Lorem ipsum dolor sit amet"

def test_end_symbol():
    @shorten_words(3, end_symbol='?')
    def get_questioned_text():
        return "Lorem ipsum dolor"
    assert get_questioned_text() == "Lor? ips? dol?"

def test_different_lengths():
    @shorten_words(5, end_symbol='.')
    def get_different_length_text():
        return "Hello beautiful world"
    assert get_different_length_text() == "Hello beaut. world"

