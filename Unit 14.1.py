# def print_2_add_2():
#     a = 2 + 2
#     print(a)
# def print_2_add_2():
#    result = 2 + 2
#    print(result)
# print_2_add_2()

# def hello_world():
#     print("Hello World!")
# hello_world()
#
# def pow_func(base, n=2):
#    print(base ** n)
#
# pow_func(3)  # 9
# pow_func(5, 3)  # 125

# def pow_func(n, a):
#     n % a == 0
#     print(int(n/a))
# pow_func(50, 5)

# def pow_func(a,n):
#     if a % n == 0:
#         print(f"{n} - является делителем числа {a}")
#     else:
#         print(f"{n}-не является делителем числа {a}")
# pow_func(50, 5)
#
# def reverse_stair(n):
#    for i in range(n, 0, -1):
#        print("*" * i)
#
# reverse_stair(10)

# def pow_func(base, n=2):
#    print(base ** n)
# print(pow_func(3))

# def pow_func(base, n=2):
#     inside_result = base ** n
#     return inside_result
#
# print(pow_func(3))
# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# print(get_multipliers(5))


# def char_frequency(text):
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")

# str_ = input(str("Enter"))
# def check_palindrome(str_):
#     str_ = str_.lower()
#     str_ = str_.replace(" ", "")
#     if str_ == str_[::-1]:
#         return True
#     else:
#         return False
# print(check_palindrome(str_))





