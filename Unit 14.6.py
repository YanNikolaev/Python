# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))

# # Из заданного списка вывести только положительные элементы
# def positive(x):
#     return x > 0  # функция возвращает только True или False
#
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
#
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))   # [1, 2]
#
# def positive(x):
#     return x % 2 == 0
# result = filter(positive, [2, 5, 8, 15, 18,21])
#
# print(list(result))

# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"} - Сортировать словарь по ключам
#
# # Чтобы отсортировать его по ключам, нужно сделать так:
# print(dict(sorted(d.items())))
# # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}

# sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря
#
# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
#
# print(sorted(data, key = lambda x: x[0] / x[1] ** 2))
# print(min(data, key = lambda x: x[0]/ x[1] ** 2))
#
