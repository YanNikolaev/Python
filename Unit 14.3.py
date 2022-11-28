# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step


# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)

#
# def count(start = 1, step = 1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
#
# for i in count():
#     print(i)

# def count():
#     while True:
#         yield (x for x in range([1, 2, 3]))
#         next(x)
# #
# def count( start = [1, 2, 3]):
#     while True:
#         yield (" ".join(map(str,start)))
# for i in count():
#     print(i)
#
# start = [1, 2, 3]


# print(" ".join(map(str,start)))
#
# def count( start = [1, 2, 3]):
#     f = ""
#     while True:
#         for i in start:
#             f += str(i)
#             yield f
#
# for a in count():
#     print(a)



# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)

# для примера возьмём строку
# str_ = "my tst"
# str_iter = iter(str_)
#
# print(type(str_))  # строка
# print(type(str_iter))  # итератор строки
#
# print(next(str_iter))  # m
#
# # Получим ещё несколько элементов последовательности
# print(next(str_iter))  # y
# print(next(str_iter))  #
# print(next(str_iter))  # t
# print(next(str_iter))  # s
# print(next(str_iter))
# print(next(str_iter))

