
tickets = int(input("Введите количество билетов:\n"))
person = tickets
cash = 0
tickets = int(person)
while person != 0:
    age = int(input(f"Введите возраст №{person} покупателя:\t"))
    if age < 18:
        print(f"Для покупателя под №{person}, билет бесплатный")
    elif age >= 18 and age < 25:
        cash += 990
        print(f"Для покупателя под №{person}, стоимость бидета: 990 рублей")
    elif age >= 25:
        cash += 1390
        print(f"Для покупателя под №{person}, стоимость бидета: 1390 рублей")
    person -= 1

if tickets >= 3:
    print(f"Общая стоимость со скидкой: {int(cash-(cash/100*10))} рублей")
else:
    print(f"Общая стоимость билетов:{int(cash)} рублей")




