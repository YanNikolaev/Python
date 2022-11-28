# month = int(input())
#
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")


# У вас есть заготовка функции — def get_wind_class(speed):
# Вам нужно вместо "???" написать цикл, который возвращает из функции класс ветра в зависимости от его характера:
# от 1 до 4 м/с - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# # от 19 м/c - "hurricane [4]"
# # В последней строке мы просим программу напечатать результат (в зависимости от цифры в скобках) —
# def get_wind_class(speed):  # Объявление функции
# ???
# print(get_wind_class(3))  # Печатаем результат выполнения

# a = []
# for i in range(1, 15):
#     a.append(i)
# print(a)

# speed = []
# for i in range(1,20):
#     speed.append(i)
# speed = int(input('ndfjr'))
# def get_wind_class(speed):
#     if speed >= 1 and speed <= 4:
#         return "weak"
#     elif speed >= 5 and speed <= 10:
#         return "moderate"
#     elif speed >= 11 and speed <=18:
#         return 'strong'
#     elif speed > 19:
#         return 'hurricane'
# print(get_wind_class(3))
# def get_wind_class(speed): #объявление функции
#     if 1 <= speed <= 4: #только аргумент
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return"strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class(20)) #мы просим программу напечатать то, что в скобках
# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False

# a = 40
# b = 41
# result = a if a > b else b
# print(result)

# a = int(input('Введите первое число\n'))
# b = int(input('Введтите второе число\n'))
# c = int(input('Введите третье число\n'))
# if (a < 45) and (b >= 45) and (c >= 45):
#     print("Истина А")
# elif (b < 45) and (a >= 45) and (c >= 45):
#     print("Истина В")
# elif (c < 45) and (a >= 45) and (b >= 45):
#     print("Истина С")
# else:
#     print("Более 2 чисел меньше 45 или не одно из них")


# A = int(input('Введите первое число\n'))
# B = int(input('Введите второе число\n'))
# C = int(input('Введите третье число\n'))
#
# if ((A < 45) and (B >= 45) and (C >=45)) or \
#     ((A >= 45) and (B < 45) and (C >=45)) or \
#     ((A >= 45) and (B >= 45) and (C < 45)):
#     print('Есть число меньше 45 и только одно')
# else:
#     print('Числа меньше 45 нет или их несколько')

# a = int(input("Введите число\n"))
# if a == (-10 <= a <= -1) or (2 <= a <= 15):
#     print("a - принадлежит диапозону")
# else:
#     print("a - Не принадлежит диапозону")


# A = int(input('Введите число\n'))
#
# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print("Число не принадлежит интервалу")
# else:
    # print("Число принадлежит интервалу")



# n = 105
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))

# list_ = [-5, 2, 4, 8, 12, 1, -7, 5] - обычный список

# print(len(list_) == len(set(list_))) - длинна списка == длинна списка переведенное в множество(множества уникальны, там нет дубликатов)


# num = 123454321
# print(str(num) == str(num)[::-1])