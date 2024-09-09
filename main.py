# # 11.1 №6 Самостоятельная практика
#
# # 1
# kub = (x**3 for x in range(1, 11) if x % 2 == 0)
# print(list(kub))
#
# # 2
# def sum_dooble_positive_digits(new_list):
#     return sum(x**2 for x in new_list if x > 0)
#
# # 3
# print(sum_dooble_positive_digits([-10, 2, 5, 9, 11]))
#
# vowels = (x for x in "hello" if x in ["a", "e", "i", "o", "u", "y"])
# print(list(vowels))
#
# # 4
# def avg_3_5(old_list):
#     new_list = list(filter(lambda x: x % 3 ==0 or x % 5 == 0, old_list))
#     return sum(new_list) / len(new_list)
#
# print(avg_3_5(range(1, 101)))
#
# # 5
# # from intertools import chain
# #
# # list1 = [1, 2, 3, 4]
# # list2 = [4, 5, 6, 7]
# # list3 = [6, 8, 8, 9]
# # new_list = list(set(chain(list1, list2, list3)))
# # print(new_list)
#
# # 6
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 35},
#     {"name": "David", "age": 30},
#     {"name": "Eve", "age": 25},
# ]
#
# filtred_people = filter(lambda x: x["age"] == 30, people)
# print(list(filtred_people))

# 11.1 №10 Самостоятельная практика
# 1
# kvadrat = (x * x for x in range(10))
# print(list(kvadrat))

def square_generator(nums):
    for num in nums:
        yield num ** 2

# a = square_generator([1,2,3])
# a.next()
# a.next()
# a.next()

# 2
import random

def random_number_generator(start, stop):
    while True:
        yield random.randint(start, stop)


# 3
def func(a):
    return a + 1

def sequence_generator(start, formula):
    num = start
    while True:
        yield num
        num = formula(num)

x = sequence_generator(1, func)
print(next(x))
print(next(x))
print(next(x))
print(next(x))



# # 4
# from intertools import chain
#
# def common_lists(list1, list2):
#     new_list = list(set(chain(list1, list2)))
#
# def intersection_generator(lst1, lst2):
#     for item in lst1:
#         if item in lst2:
#             yield item
#
# # 5
# import pytest
# from your_module import intersection_generator
#
# def test_intersection_generator():
#     # Создаем тестовые данные
#     list1 = [1, 2, 3, 4, 5]
#     list2 = [3, 4, 5, 6, 7]
#     expected_result = [3, 4, 5]
#
#     # Запускаем генератор
#     result = list(intersection_generator(list1, list2))
#
#     # Проверяем, что результат соответствует ожидаемому
#     assert result == expected_result
#
# def test_empty_intersection():
#     # Тест на случай, когда пересечений нет
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
#     expected_result = []
#
#     # Запускаем генератор
#     result = list(intersection_generator(list1, list2))
#
#     # Проверяем, что результат — пустой список
#     assert result == expected_result
#
# def test_no_duplicates_in_output():
#     # Тест на то, что в выводе нет дубликатов
#     list1 = [1, 1, 1, 2, 2, 3]
#     list2 = [1, 2, 2, 3, 3, 3]
#     expected_result = [1, 2, 3]
#
#     # Запускаем генератор
#     result = list(intersection_generator(list1, list2))
#
#     # Проверяем, что результат не содержит дубликатов
#     assert result == expected_result


# 6

