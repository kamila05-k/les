#lambda

"""f = lambda x: x * x
print(f(5))

f = lambda x, y: x * y
print(f(5, 3))"""

"""list1 = [{"name": "Madina", "age": 20},
         {"name": "Kamila", "age": 18},
         {"name": "Omurbek", "age": 17}]
print(sorted(list1, key=lambda i: i ["age"] ))"""

"""f = lambda x: x ** 2
print(f(2))

a = lambda name: (name.splid()[0], name1.splid([1]))
name = "Таалайбек кызы"
name1 ="Kamila"
print(name, name1)"""

#map
"""list_of = ["one", "tvo", "list"]
s = list(map(str.upper, list_of))
print(s)"""

"""
list_of = ['1', '2', '5', '6']
ls = list(map(int, list_of))
print(ls)
"""
"""
list1 = ['1', '2', '3', '4']
ls = list(map(lambda x: int(x)**2, list1))
print(ls)"""

#filter
"""list1 = ["one", "two", "list", "", "dict"]
ls = list(filter(lambda x: x.strip() =="", list1))
print(ls)"""

# lambda

# f = lambda x: x * 2
#
# print(f(5))
#
#
# def f(x):
#     return x * 2
# print(f(5))


# f = lambda x, y: x * y
#
# print(f(10, 2))

# f = lambda: True
#
# print(f())
#
# def f():
#     return True
#
# print(f())

# ls = [2, 3, 1, 7, 4]
# print(sorted(ls))


# list = [{"name": "Madina", "age": 20},
#        {"name": "Kamila", "age": 18},
#        {"name": "Omurbek", "age": 17}]
#
#
# print(sorted(list, key=lambda i: i['age']))

#
# list_of_words = ['one', 'two', 'list', 'dict']
#
# for i in range(len(list_of_words)):
#     list_of_words[i] = list_of_words[i].upper()
#
# print(list_of_words)

# map
# list_of_words = ['one', 'two', 'list', 'dict']
# ls = list(map(str.upper, list_of_words))

# list_of_str = ['1', '2', '5', '10']
#
# ls = list(map(lambda x: int(x)**2, list_of_str))
# print(ls)

# vlans = [100, 110, 150, 200, 201, 202]
#
# f = list(map(lambda x: f"vlan {x}", vlans))
# print(f)


# nums = [1, 2, 3, 4, 5]
#
# nums2 = [100, 200, 300, 400, 500]
#
#
# ls = list(map(lambda x, y: x * y, nums, nums2))
# print(ls)

# names = ['Omurbek', 'Madina', "Bek"]
# ages = [17, 18, 23]
#
# dc = list(map(lambda x, y: f"{x} - {y}", names, ages))
# print(dc)


# filter

"""list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']

ls = list(filter(lambda x: len(x) == 0, list_of_strings))
print(ls)"""

# ls = [i for i in list_of_strings if i.isdigit()]
# print(ls)

# ls = list(filter(str.isalpha, list_of_strings))
# print(ls)

# list_int = [10, 111, 102, 213, 314, 515]
#
# ls = list(filter(lambda x: x % 2 == 0, list_int))
# print(ls)

# ls = list(filter(lambda x: len(x) > 2, list_of_strings))
# print(ls)
#
# ls2 = [i for i in list_of_strings if len(i) > 2]
# print(ls2)


""""("================================================================================================================================")"""
"""lambda"""
#1
"""c = lambda a, b: a + " " + b
print(c("Hello", "World"))"""

#2
"""Tru Fols"""
"""i = lambda x: x > 0
print(i(7))
print(i(-2)) """

#3
"""Key dict"""
"""k = ['a', 'b', 'c']
v = [1, 2, 3]

diction = dict(zip(k, v))
print(diction)"""

#4
"""calendar"""
"""import calendar

y = 2023
m = 7

cal = calendar.monthcalendar(y, m)

for w in cal:
    print(w)"""

#5
"""Месяць"""
"""get_month = lambda month1: [
    None, "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
][month1]

month1 = 7
month2 = get_month(month1)

print(month2)"""

"""map"""
#1
"""numbers = [1, 2, 3, 4, 5]
mapp = map(str, numbers)
print(list(mapp))
"""

#2
"""Key dict"""
"""names = ['Alice', 'Bob', 'Charlie']
ages = [25, 32, 28]

diction = dict(map(lambda name, age: (name, age), names, ages))
print(diction)"""

#3
"""calendar"""
"""import calendar

year = 2023

cal = calendar.calendar(year)
cal_lin = cal.split("\n")[2:]
cal_ = map(str.split, cal_lin)
cal_ = list(map(lambda row: row[1:], cal_))

calendar = []
for month_ in cal_:
    month = month_[:7]
    calendar.append(month)

for month in calendar:
    print(month)"""

"""filter"""
#1
"""Key dict"""
"""numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

filt_dict = dict(filter(lambda i: i[1] > 2, numbers.items()))
print(filt_dict)"""

#2
"""Игра"""
"""import random
def generate_():
    return random.randint(1, 100)

def get_guess():
    return int(input("Угадайте число: "))

def check_guess(secret_number, guess):
    if guess < secret_number:
        return "Слишком маленькое число!"
    elif guess > secret_number:
        return "Слишком большое число!"
    else:
        return "Поздравляю, вы угадали число!"

def play_game():
    secret_number = generate_()
    attempts = 0
    while True:
        guess = get_guess()
        result = check_guess(secret_number, guess)
        print(result)
        attempts += 1
        if result == "Поздравляю, вы угадали число!":
            break
    print("Игра завершена. Вы угадали число за", attempts, "попыток.")
play_game()"""




