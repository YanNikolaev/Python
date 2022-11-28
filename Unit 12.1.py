# text = input("Введите текст:")
# unique = list(set(text))
# print("Количество уникальных символов: ", len(unique)

# a = input('Введите число')
# b = input('Введите второе число')
# a_set, b_set = set(a), set(b)
# ab = b_set.symmetric_difference(a_set)
# # print(ab)

# a = set(input('Введите число').split())
# b = set(input('Введите второе число').split())
# ab = a.symmetric_difference(b)
# print(sorted(ab))

# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))
# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))
# a = 5
# print(id(a))
# b = 2 + 3
# print(id(a))
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
# print(list_id_after == list_id_before)
# a = set(input('Введите число').split())
# b = set(input('Введите второе число').split())
# ab = a.symmetric_difference(b)
# ab_int = list(map(int, ab))
# print(sorted(ab_int))



# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
#
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка


a = set(input('Введите число').split())
b = set(input('Введите второе число').split())
ab = a.symmetric_difference(b)
ab_int = list(map(int, ab))
print(sorted(ab_int))