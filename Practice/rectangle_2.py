from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle (2, 15)

print("Площадь 1 прямоугольника:", rect_1.get_area())
print("Площадь 2 прямоугольника", rect_2.get_area())


square_1 = Square(5)
square_2 = Square(10)

print("Площадь квадрата:", square_1.get_area_square(), square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance(figure, Square):
        print("Square", figure.get_area_square())
    else:
        print("Rectangle", figure.get_area())

circle_1 = Circle(2)
circle_2 = Circle(10)

print(circle_1.get_area_circle(), circle_2.get_area_circle())