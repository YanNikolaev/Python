import math
# print('Введите радиус круга')
# r = int(input("r= \t"))
# print("P=%d; S=%.2f"% (2*math.pi*r, math.pi*r**2))

# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a < c or a < b and a > c:
#     print(a)
# elif b > a and b < c or b<a or b>c:
#     print(b)
# else:
#     print(c)
#
# a = input()
# print(a[::-1])

# n = 1
# for i in range(1,6):
#     n = n * i
#     print(n)

n = int(input())
fac = 1
while n > 1:
    fac *= n
    n -= 1
print(fac)



