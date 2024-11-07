class AddOperation:
    def init(self, a, b):
        self.a = a
        self.b = b

class Addoperation1(AddOperation):
    def add(self, other):
        self.other = other
        return (self.a + self.b + self.other)

class Calculator(Addoperation1):
    pass
cal = Calculator(34, 54)
print(cal.add(2))

