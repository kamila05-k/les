# Наследование
#
# class Person: # Super Class
#     def __init__(self, first_name, last_name):
#         self.fist_name = first_name
#         self.last_name = last_name
#
#     def get_info(self):
#         return f"{self.fist_name} - {self.last_name}"


# class User(Person): # Sub Class
#     pass
#
# user = User("Saltanat", "Salatanova")
# print(user.fist_name)
# print(user.last_name)
# print(user.get_info())

# person = Person("Saltanat", "Salatanova")
#
# class Other:
#     def func(self):
#         info = person.get_info()
#         return info
#
#
# oth = Other()
# print(oth.func())


# superclass first_name, last_name, subclass age, gender
# My first_name: Saltanat, last_name: Salatanova. I am 17 years old. I am female
"""

class Info:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def user(self, age, gender):
        return (f"My {self.first_name}, {self.last_name}, I am {age}, I am {gender}")
class Inf(Info):
    pass

inf = Inf("Kamila", "Таалайбек кызы")
print(inf.user(18, "female"))
"""

"""class Sfr:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Desk(Sfr):
    def sq(self):
        return self.a + self.b

class Sfdes(Desk):
    def sq(self):
        return self.a + self.b

t2 = Sfdes(10, 2)
print(t2.sq())
"""

#2 мисал
"""class Desk(Sfr):
    def sq(self):
        return self.a + self.b

class Sfdes(Desk):
    def sq(self, monitor=0.0):
        return self.a + self.b - monitor

t2 = Sfdes(55, 9)
print(t2.sq())
"""

"""class Car:
    def __init__(self, marka, speed):
        self.marka = marka
        self.speed = speed

    def sh(self):
        print(self.marka)
        print(self.speed)
class Airplane(Car):
    def airplen(self):
        print("взлетает на небе")

class Boat(Airplane):
    def boat(self):
        print("плавает в воде")

boat1 = Boat(marka="BMV", speed=200)
boat1.boat()
boat1.airplen()
boat1.sh()
"""
#2 мисал
"""class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"The {self.brand} car is driving."

class Airplane(Car):
    def fly(self):
        return "The airplane is flying."

class Boat(Airplane):
    def sail(self):
        return "The boat is sailing."

car = Car("Toyota")
airplane = Airplane("Boeing")
boat = Boat("Yacht")

print(car.drive())
print(airplane.fly())
print(boat.sail())
"""


