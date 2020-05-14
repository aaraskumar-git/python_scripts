class Car:
    def __init__(self, color):
        print('we are in init')
        self.color = color

    @staticmethod
    def mycolor(color):
        return color

    def display(self):
        return self.color

colorcode = Car('red')

Car.mycolor('green')
print(colorcode.display())

