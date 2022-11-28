# def linear_solve(a, b):
#     return b/a
# print(linear_solve(0,1))

# def linear_solve(a, b):
#     if a:
#         return b/a
#     elif not a and not b: # снова используем числа в логических выражениях
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"
#

#
# def D(a,b,c):
#     return b**2 - 4*a*c
#
# def quadratic_solve(a,b,c):
#     if D(a,b,c) < 0:
#         return "Нет вещественных корней"
#     elif D(a,b,c) == 0:
#         return -b/(2*a)
#     else:
#         return (-b-D(a,b,c)**0.5)/(2*a), (-b+D(a,b,c)**0.5)/(2*a)
# L = list(map(float, input().split()))
# print(quadratic_solve(L[0], L[1], L[2]))


# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
#
#
# print(min_list([1,-5, 73, 14, 0]))

# def mirror(a, res=0):
#     if a == 0:
#         return res
#     else:
#         return mirror(a // 10, res * 10 + a % 10)
#
# print(mirror(15))
#
# b = 1%10
# print(b)
#
# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)
#
# print(equal(15,6))

# def e():
#     n = 1
#
#     while True:
#         yield (1 + 1 / n) ** n
#         n += 1
# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
#
yesno = input("""Введите Y, если хотите авторизоваться или N,
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper

@is_auth
def from_db():
    print("some data from database")

from_db()

@is_auth
def change_profile():
    print("Profile has been changed")


USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")
def has_access(func):
    def wrapper():
        if username in USERS:
            print("Авторизован как", username)
            func()
        else:
            print("Доступ пользователю", username, "запрещен")
    return wrapper
@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()

