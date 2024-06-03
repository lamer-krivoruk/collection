"""
Способы создания кортежа
Создать кортеж можно четырьмя способами.
"""


a = ()
b1 = 1,
b2 = (1,)
c1 = 1, 2, 3,
c2 = (1, 2, 3)
d = tuple(range(3))
print(a, b1, b2, c1, c2, d, sep='\n')
"""
1. Пара круглых скобок создаёт пустой кортеж
2. Один элемент с замыкающей запятой в скобках или без них создаёт кортеж с
элементом
3. Несколько элементов разделенных запятыми с замыкающей запятой или в
круглых скобках
4. Функция tuple(), которой передаётся любой итерируемый объект
!!!!!!!🔥 Важно! Обратите внимание, что на самом деле кортеж образует запятая,
    а не круглые скобки. Круглые скобки необязательны, за исключением случая
    пустого кортежа или когда они необходимы, чтобы избежать синтаксической
    неоднозначности. Например, f(a, b, c) — это вызов функции с тремя
    аргументами. f((a, b, c)) — вызов функции с кортежем в качестве
    единственного аргумента.!!!!!!!!!!!!!!!!!!!!!!!
"""

my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
print(my_tuple[2:6:2])
print(my_tuple[-3])
print(my_tuple.count(2))
print(f'{my_tuple = }')
print(my_tuple.index(2, 2))
print(type('text',))
