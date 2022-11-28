# a = []
# for i in range(1, 15):
#     a.append(i)
# print(a)

# squares = [i**2 for i in range(1,11)] вадраты первых десяти натуральных чисел


# squares = [i**2 for i in range(1,11) if i % 2 == 1] квадраты только от нечетных чисел

# list_tuples = [(i, i**2) for i in range(1,11)]
# print(list_tuples)nип элемента, который будет включаться в список может быть любым, список из кортежей:


# M = [[i+j for j in range(5)] for i in range(5)] - используя вложенные генераторы списков можно создать матрицу
# на каждой итерации цикла с индексом i создавали вложенный список с индексами j,
# что в итоге позволило создать матрицу (таблицу чисел)

# T = [[i*j for j in range(1,11)] for i in range(1,11)] - таблица умножения чисел от 1 до 10
# print(T)

# L = [input() for i in range(5)]  На каждой итерации цикла консоль будет запрашивать данные
# для ввода и сохранять их в качестве элемента списка

# L = [int(input()) for i in range(5)]


# L = [int(input()) % 2 == 0 for i in range(5)] True, если элемент четный, и False, если элемент нечетный

# L = [i for i in range(10)]
# # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1
# for a in zip(L,M):
#     print(a)
# for a, b in zip(L, M):
# L = [i for i in range(10)]
#
# M = [i for i in range(10, 0, -1)]
# for a, b in zip(L,M):
#     print(a*b)
#
# N = [a*b for a,b in zip(L,M)]
