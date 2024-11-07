"""class Percon:
    def __init__(self, name, last_name, age, gender):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def info(self):
        print(f'i am {self.name} my name {self.last_name} {self.age} {self.gender}')

a = Percon('Камила','Таалайбек кызы', 18, 'ж')
a.info()
"""
#2
"""class Laptop:
    def __init__(self, model, processor, ram, gpu):
        self.model = model
        self.processor = processor
        self.ram = ram
        self.gpu = gpu

    def info(self):
        print(f'мадел:{self.model} :{self.processor} ГБ: {self.ram} видое:{self.gpu}')

a = Laptop('Acer', 'Intel Core i5', '8 гб', 'видое карта')
a.info()

b = Laptop('MacBook', 'Intel Core i7', '16 ГБ', 'AMD Radeon Pro 5500M')
b.info()
"""
#3
"""class Car:
    def __init__(self, name, model, steering, balloon, Germany):
        self.name = name
        self.model = model
        self.steering = steering
        self.balloon = balloon
        self.Germany = Germany

    def info(self):
        print(f'name:{self.name} model:{self.model} steering:{self.steering} balloon:{self.balloon} Germany:{self.Germany}')

a = Car('BMW', 'Gran Turismo серии 3 и 6:', 'Queda el volante', '4', 'Germany на машин')
a.info()
"""

"""======================================================Тапшырма===================================="""

#1

"""class Country:
    def __init__(self, name, religion, capital, president, famous_for, population, land_area, development):
        self.name = name
        self.religion = religion
        self.capital = capital
        self.president = president
        self.famous_for = famous_for
        self.population = population
        self.land_area = land_area
        self.development = development

    def st(self):
        print(f"{self.name}: {self.population} жителей")

russ = Country( "Россия", "православие", "Москва", "Владимир Путин", "балалайка, матрешки", 144000000,17100000, "развитая экономика" )
russ.st()
china = Country("Китай", "конфуцианство, буддизм, даосизм", "Пекин", "Си Цзиньпин", "Великая Китайская стена", 1400000000, 9600000, "великая цивилизация")
china.st()
india = Country("Индия", "индуизм, буддизм, ислам", "Нью-Дели", "Рам Натх Ковинд", "Тадж-Махал", 1390000000, 3280000, "разнообразная культура")
india.st()
a = max(russ.population, china.population, india.population)
print(a)
"""
"""
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Ошибка: деление на ноль"

    def perform_operation(self, operation, x, y):
        return operation(self, x, y)

calculator = Calculator()

operations = {
    '+': Calculator.add,
    '-': Calculator.subtract,
    '*': Calculator.multiply,
    '/': Calculator.divide
}

print("Доступные операции:")
print("+ - Сложение")
print("- - Вычитание")
print("* - Умножение")
print("/ - Деление")

choice = input("Введите операцию (+/-/*/ /): ")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

operation = operations.get(choice, Calculator.subtract) 
result = calculator.perform_operation(operation, num1, num2)

print("Результат:", result)
"""

"""class School:
    def init(self, mathematics=None, russian=None, physics=None, kyrgyztill=None):
        self.mathematics = mathematics
        self.russian = russian
        self.physics = physics
        self.kyrgyztill = kyrgyztill
        self.schedule_days = {}

    def add_day(self, day, time_math, time_russian, time_physics, time_kyrgyztill):
        self.schedule_days[day] = {
            "mathematics": self.mathematics(time_math),
            "russian": self.russian(time_russian),
            "physics": self.physics(time_physics),
            "kyrgyztill": self.kyrgyztill(time_kyrgyztill)
        }

    def display_schedule(self):
        print("Расписание занятий:")
        for day, subjects in self.schedule_days.items():
            print(day)
            print(subjects["mathematics"])
            print(subjects["russian"])
            print(subjects["physics"])
            print(subjects["kyrgyztill"])
            print("")

# Создаем экземпляр класса School с предопределенными предметами
a = School("matem")

# Добавляем расписание для разных дней
a.add_day("Понедельник", "10:00-11:30", "11:45-13:15", "14:00-15:30", "15:45-17:15")
a.add_day("Вторник", "09:00-10:30", "10:45-12:15", "13:00-14:30", "14:45-16:15")

# Выводим расписание занятий
a.display_schedule()"""

class School:
    def __init__(self, mathematics, russian, physics, kyrgyztill):
        self.mathem = mathematics
        self.russ = russian
        self.phys = physics
        self.kyrgyz = kyrgyztill
    def st(self):
        print(f"{self.mathem}: {self.russ} {self.phys} {self.kyrgyz}")

mat = School( "математика", "3 раза в неделю", "времия", "10:00 до 11:30")
mat.st()
rus = School("русский", "3 раза в неделю", "времия", "11:45 до 13:15")
rus.st()
phys = School("Физика", "1 раза в неделю", "времия", "14:00 до 15:30")
phys.st()
kyr = School("кыргызкий", "2 раза в неделю", "времия", "15:45 до 17:15")
a = mat.mathem, rus.russ, kyr.kyrgyz
print(a)

