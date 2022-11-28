# def twice_func(inside_func):
#     """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
#     inside_func()
#     inside_func()
#
#
# def hello():
#     print("Hello")
#
#
# test = twice_func(hello)
#
# def make_adder(x):
#    def adder(n):
#        return x + n # захват переменной "x" из nonlocal области
#    return adder  # возвращение функции в качестве результата
# # функция, которая будет к любому числу прибавлять пятёрку
# add_5 = make_adder(5)
# print(add_5(10))  # 15
# print(add_5(100))  # 105

# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
#
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return 0
#
# print(my_function())
# # Я - оборачиваемая функция!
# # # 0
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())
# # Я буду выполнен до основного вызова!
# # Я - оборачиваемая функция!
# # Я буду выполнен после основного вызова!
# # 0

#
# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")


# def do_it_twice(func):
#    def wrapper(*args, **kwargs):
#        func(*args, **kwargs)
#        func(*args, **kwargs)
#    return wrapper
#
# @do_it_twice
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")

# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrapper

# def counter(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         func(*args, **kwargs)
#         count += 1
#         print(f"{func} была вызванна {count} раз.")
#         return count
#
#     return wrapper
# @counter
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз
#
# say_word("Oo!!!")
#


#
# def cache(func):
#     dict_cache ={}
#     def wrapper(num):
#         nonlocal dict_cache
#         if num not in dict_cache:
#             dict_cache[num] = func(num)
#             print(f"Добавление результата в кэш {dict_cache[num]}")
#         else:
#             print(f"Возвращение результата из кеша {dict_cache[num]}")
#         print(f"Кэш = {dict_cache}")
#         return dict_cache[num]
#     return wrapper
# @cache
# def f(n):
#    return n * 123456789
# f(2)
#
#















