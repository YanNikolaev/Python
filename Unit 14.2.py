# x = 3
# def function():
#     print(x)
#     return x
#
# print(function())


x = 3


# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
#
#
# func()
# print(x)

# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
#
# hello_world_func = get_my_func()  # получить функцию в качестве результата
#
# print(type(hello_world_func))  # <class 'function'>
# hello_world_func()
#
# def get_mul_func(m):
#     nonlocal_m = m
#
#     def local_mul(n):
#         return n * nonlocal_m
#
#     return local_mul
#
#
# two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
# two_mul(5)  # 5 * 2
# print(two_mul)

# def adder(*nums):
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#
#     return sum_
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(1, 2, 3))  # 6

# def adder(*args):
#     sum = 1
#     for i in args:
#         sum *= i
#     return sum
#
# print(adder(2, 7))

# def mul(*nums):
#     p = 1
#     for n in nums:
#         p *= n
#
#     return p
# print(mul(2, 7))


# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#       return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# rec_fibb(10)

# def rec_sum(n): - С помощью рекурсивной функции найдите сумму чисел от 1 до n.
#     if n == 1:
#         return 1
#     return n + rec_sum(n-1)
# print(rec_sum(2))

# def reverse_str(string):   С помощью рекурсивной функции разверните строку.
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# reverse_str('test')  # tset

# def sum_digit(n): Дано натуральное число N. Вычислите сумму его цифр.
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# sum_digit(123)  # 6
