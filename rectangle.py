class Rectangle:
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def getWidth(self):
        return self.width

    def getHight(self):
        return self.hight

    def getArea(self):
        return self.width * self.hight
