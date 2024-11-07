"""person = {'name': 'Samat', 'age': 23, 'etty': 'Bishkek', 'position': 'programmer'}
for key, value in person.items():
     if value == 'Bishkek' and key == 'city':
         print('3')
     else:
         print(key, value)"""

"""names = {'name': 'Kamila', 'age': 18, 'Anna' 'age': 13, 'Annara' 'age': 19}
for key, value in names.items():
    if value == 18:
        print(key, value)"""





#person = {'name': 'Ramazan', 'age': 23, 'city': 'Bishkek'}
"""s = person.setdefault('name')
print(s)
"""

"""d = {'position': 'programmer'}
person['programmer'] = 24
print(d)

for k, v in person.items():
    print(k, v)
"""

# original = {1:'one', 2:'two'}
# new = original.copy()
# print('Orignal: ', original)
# print('New: ', new)


# person = {'name': 'Samat', 'age': 23, 'city': 'Bishkek', 'position': 'programmer'}
# d = person.pop('city')
# print(d)
# print(person)


# d = {'position': 'povor'}
# f = person.update(d)
# print(person)

# for key, value in person.items():
#     if value == 'Bishkek' and key == 'city':
#         print('3')
#     else:
#         print(key, value)




# people = {
#     'Алексей': 25,
#     'Елена': 17,
#     'Иван': 30,
#     'Мария': 20,
#     'Николай': 16
# }
#
# for name, age in people.items():
#     if age >= 18:
#         print(name, age)









# Напишите программу, которая принимает на вход словарь, содержащий названия
# продуктов и их стоимость, и выводит суммарную стоимость всех продуктов.


# products = {
#     'яблоки': 10,
#     'бананы': 15,
#     'апельсины': 12,
#     'груши': 8
# }
# total_cost = 0
# for price in products.values():
#     total_cost = total_cost + price
# print("Суммарная стоимость всех продуктов:", total_cost)
#
# print(sum(products.values()))





"""poduk = {'картошка': 35,
         'памидор': 45,
         'Алма': 23,
         'пияз': 43
}
p = 0
for i in poduk.values():
    p= p + i
print(p)"""



"=============================================================Тапшырма====================================================="

#1
"""student = {'Kamila': 12,
           'Боб': 23,
           'raxat': 43,
           'Алиса': 32}
print(student)"""

#2
"""students = {'Kamila': 12,
           'Боб': 23,
           'raxat': 43,
           'Алиса': 32}

for key, values in students.items():
    if values == 32 and key == 'Алиса':
        print(key, values)
"""

#3

"""students = {'Kamila': 12,
           'Боб': 23,
           'raxat': 43,
           'Алиса': 32}

d = {'Обо': 92}
f = students.update(d)
print(students)

for key, value in students.items():
    if value == 32 and key == 'Алиса':
        print(students)"""

#4
"""
students = {'Kamila': 12,
           'Боб': 23,
           'raxat': 43,
           'Алиса': 32}students = {'Kamila': 12,
           'Боб': 23,
           'raxat': 43,
           'Алиса': 32}


d = {'Боб': 88}
f = students.update(d)
print(students)

for key, value in students.items():
    if value == 12 and key == 'Kamila':
        print(students)"""

#5

"""students = {'Kamila': 12,
           'Боб': 23,
           'raxat': 43,
           'Алиса': 32}

for key in students:
    if 'Charlie' in key == 0:
        print("Студент с именем 'Charlie' найден в словаре students.")
    else:
        print("Студент с именем 'Charlie' не найдон в словаре students.")

"""

#6
"""students = {'Kamila': 12,
           'Боб': 23,
           'raxat': 43,
           'Алиса': 32}

del students['Kamila']
print(students)"""

#7
"""students = {'Kamila': 12,
           'Боб': 23,
           'raxat': 43,
           'Алиса': 32}

for name, precio in students.items():
    print(f"student: {name}, precio: {precio}")"""

