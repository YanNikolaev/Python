class Rectangle:
    def __init__(self, x, y, width, hight):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight

    def __str__(self):
        return f"Rectangle:{self.x}, {self.y}, {self.width}, {self.hight}"

    def get_area_rectangle(self):
        return f"Area Rectangle {self.width * self.hight}"

rect_1 = Rectangle(5, 10, 50, 100)

print(rect_1, rect_1.get_area_rectangle())


class Client:
    def __init__(self, name, lastname, city, balance):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.balance = balance


    def __str__(self):
        return f"{self.name}.{self.lastname}.{self.city}.{self.balance}"

    def get_inf(self):
        return f"{self.name}.{self.lastname}.{self.city}"

person_1 = Client("Иван","Петров", "Москва", "50 руб")
person_2 = Client("Дмитрий", "Степанов", "Саратов", "17 руб")
person_3 = Client("Алексей", "Медведев", "Коломна", "20 000 руб")
person_4 = Client("Владимир","Иванов","Нижний Новгород","532 руб")

clients = [person_1, person_2, person_3, person_4]

for client in clients:
   print(client.get_inf())