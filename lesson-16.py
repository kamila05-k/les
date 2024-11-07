# function

"""def sey_hello():
    print("Hello")

sey_hello()"""

"""def sey_hello():
    print("Hello")

def sey_goodbye():
    print("Goot bye")
sey_hello()
sey_goodbye()"""

"""
def main():
    sey_hello()
    sey_goodbye()

def sey_hello():
    print("Hello")

def sey_goodbye():
    print("Goot bye")

main()"""


"""def info(first_name, last_name):
    print(f"My name is {first_name}:{last_name}" )

info("Kamila", "Таалайбек кызы")"""

# function

#
# def say_hello():
#     print("Hello")
#
#
# def say_goodbye():
#     print("Good Bye")

# say_hello()
# say_goodbye()


# def print_message():
#     def say_hello(): print("Hello")
#     def say_goodbye(): print("Good bye")
#
#     say_hello()
#     say_goodbye()
#     print("Finish")
#
# print_message()


# def main():
#     say_hello()
#     say_goodbye()
#
#
# def say_hello():
#     print("Hello")
#
#
# def say_goodbye():
#     print("Good Bye")
#
# main()


# def info(first_name, last_name):
#     print(f"My name is {first_name}-{last_name}")
#
#
# def welcome(first_name, last_name):
#     info(first_name, last_name)
#     print(f"Welcome MR. {first_name}-{last_name}")
#
#
# welcome('Bek', 'Beishekeev')


# def say_hello():
#     print("Hello")
#
#
# def how_are_you():
#     say_hello()
#     print("How are you?")
#
#
# how_are_you()


# def omurbek(name):
#     if name == 'Omurbek':
#         print("My heart is free")
#     else:
#         print("My heart is not free")
#
#
# omurbek('Abdullakh')

# names = ['Saltanat', 'Madina', 'Muhammed', 'Bekzat', 'Albina', 'Manas', 'Bek', 'Abdullakh', 'Abubakr', 'Kamila', 'Omurbek', 'Meerim']
#
#
# def len_names(ls):
#     for i in range(len(ls)):
#         names[i] += ' ' + str(i+1)
#
#
# len_names(names)
#
# print(names)




"""def a(x, y):
    return x + y

def b(x, y):
    return x - y

def c(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль!"
"""
"""
print("Доступные операции:")
print("1. кошуу")
print("2. кемитуу")
print("3. кобойтуу")

a4 = int(input("Выберите операцию: "))
num1 = input("Введите первое число:  ")
num2 = input("Введите второе число: ")

if a4 == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif a4 == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif a4 == '3':
    print(num1, "*", num2, "=", divide(num1, num2))
else:
    print("неправильный выбор операции!")
"""

"""def cate(a, b, c):

    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
cate(15, 5, '+')"""

"""def calc(a, b, c):
    print(eval(f"{a} + {b} + {c}"))
calc(12, 3)"""



"+=====================================================+Тапшырма+==========================================================================="
"1"

#1 Мисал
"""def name(firs_name, last_name, age, gender):
    return f'{firs_name}, {last_name}, {age}, {gender}'
firs_name = input()
last_name = input()
age = input()
gender = input()
print(name(firs_name, last_name, age, gender))"""
#2 МИСАЛ
"""def name(firs_name, last_name, age, gender):
    return firs_name, last_name, age, gender
print(name(firs_name = 'Камила', last_name = 'Таалайбек кызы', age = 18, gender = 'femenino'))"""

"2"
# 1 Мисал
"""
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def f():
    for i in b:
        if i % 2 == 0:
            print(i)
    return 'жуп сан'
a = f()
print(a)


#2 Мисал
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def f():
    for i in b:
        if i % 2 != 0:
            print(i)
    return 'так сан'
a = f()
print(a)
"""

#3 Мисал
"""b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = []
f = []
def a3():
    for i in b:
        if i % 2 == 0:
            a.append(i)
        else:
            f.append(i)
        a1 = a
        f1 = f
    return('жуп сан')
print(a3())
print(a)
print("Так сан")
print(f)"""