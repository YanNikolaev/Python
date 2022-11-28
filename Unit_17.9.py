# L = input("Введите последовательность чисел через пробел: ")
# L_mod = [int(a) for a in L.split()]
#
# if (' ' not in (L)):
#     raise ValueError("Введены некорректные данные! Введите последовательность чисел через пробел!")
#
# num = int(input("Введите любое число: "))
# if num % 1 != 0:
#     raise ValueError("Введены некорректные данные! Введите число!")
#
# for i in range(1, len(L_mod)):
#     x = L_mod[i]
#     idx = i
#     while idx > 0 and L_mod[idx-1] > x:
#         L_mod[idx] = L_mod[idx-1]
#         idx -= 1
#     L_mod[idx] = x
# print("Сортированный список:", L_mod)
#
# def binary_search(L_mod, num, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#     middle = (right + left) // 2  # находим середину
#     if L_mod[middle] == num:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif num < L_mod[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(L_mod, num, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(L_mod, num, middle + 1, right)
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(L_mod, num, 0, len(L_mod)-1))

L = input("Введите последовательность чисел через пробел: ")
L_mod = [int(a) for a in L.split()]

if (' ' not in (L)):
    raise ValueError("Введены некорректные данные! Введите последовательность чисел через пробел!")

num = int(input("Введите любое число: "))
if num % 1 != 0:
    raise ValueError("Введены некорректные данные! Введите число!")

for i in range(1, len(L_mod)):
    x = L_mod[i]
    idx = i
    while idx > 0 and L_mod[idx-1] > x:
        L_mod[idx] = L_mod[idx-1]
        idx -= 1
    L_mod[idx] = x
print("Сортированный список:", L_mod)

def binary_search(L_mod, num, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if L_mod[middle] == num:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif num < L_mod[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(L_mod, num, left, middle - 1)
    else:  # иначе в правой
        return binary_search(L_mod, num, middle + 1, right)

# запускаем алгоритм на левой и правой границе
print(binary_search(L_mod, num, 0, len(L_mod)-1))


