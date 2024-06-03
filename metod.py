# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# # my_list.extend(a) # TypeError: 'int' object is not iterable
# print(my_list)  # [None]
# my_list.extend(b)
# print(my_list)  # [None, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
# my_list.extend(c)
# print(my_list)  # [None, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!', 1, 3, 5, 7]
# my_list.extend(my_list)
# print(my_list)  # [None, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!', 1, 3, 5, 7, None, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!', 1, 3, 5, 7]


# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.append(a)
# print(my_list)  # [None, 42]
# my_list.append(b)
# print(my_list)  # [None, 42, 'Hello world!']
# my_list.append(c)
# print(my_list)  # [None, 42, 'Hello world!', [1, 3, 5, 7]]
# # my_list.append(my_list)
# # print(my_list)  # [None, 42, 'Hello world!', [1, 3, 5, 7], [...]] !!!рекурсия, никогда так не делать!!!


# my_list = [2, 4, 6, 8, 10, 12]
# spam = my_list.pop()
# print(spam, my_list)  # 12 [2, 4, 6, 8, 10]
# eggs = my_list.pop(1)  # !где 1 это индекс!
# test = []
# for _ in range(5):
#     test.append(my_list.pop())  # [12, 10, 8, 6, 4]

# test = my_list[-1::-3]  # [12, 6]
#
# print(test)


"""
        Сортировка и разворачивание
        sorted()
        reverse()
        sort()
"""

# my_list = [4, 8, 2, 9, 1, 7, 2]
# sort_list = sorted(my_list)
# print(my_list, sort_list, sep='\n')
# rev_list = sorted(my_list, reverse=True)
# print(my_list, rev_list, sep='\n')


# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)


# my_list = [4, 8, 2, 9, 1, 7, 2]
# res = reversed(my_list)
# print(type(res), res)
# rev_list = list(reversed(my_list))  # Важно! Подобный приём затратен по времени и по памяти.
# print(rev_list)

# for item in reversed(my_list):
#     print(item, end=' ')


"""
Создание копий
"""


# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n')

"""
Мы скопировали в переменную new_list указатель на список my_list. Далее мы
изменили элемент в исходном списке. Новый список также оказался изменённым.
Как вы помните list — изменяемый тип данных и подобное поведение нормально.
Что делать, если нужно менять оригинал, но не затрагивать копию. Верно. Метод
copy.
"""

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list.copy()
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n')
# # Теперь изменяется лишь один список.


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = matrix.copy()
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')
"""
Метод copy создал поверхностную копию, копию верхнего уровня. Изменения же
вложенных объектов отразится и на оригинале. В таком случае для создания
полной копии любой глубины вложенности используют функцию deepcopy из
модуля copy.
"""


import copy


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = copy.deepcopy(matrix)
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')
"""
Функция рекурсивно обходит все вложенные объекты создавая их копии.
Изменения одной коллекции теперь не затрагивают её копию.
"""

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(len(my_list))
# print(len(matrix))
# print(len(matrix[1]))
