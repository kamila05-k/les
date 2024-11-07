# decorator
#*args **gvargs
"""def select(input_func):
    def output():
        print("**************************************")
        input_func()
        print("************************************")
    return output

@select
def hello():
    print("Hello")

hello()"""

"""def check(input_func):
    def output(*args):
        name = args[0]
        age = args[1]
        if age < 0:
            age = 1

        input_func(name, age)
    return output
@check
def info(name, age):
    print(f"{name} = {age}")

info("Abbullakh", 15)
info("kamila",  18)
"""




# *args
"""def get_(*args):
    print(*args)

get_(1, 2,3)"""
# **kwargs

"""def fun(**kwargs):
    print(kwargs)

fun(name="Kamila", age=18)
"""

"""def fun(**kwargs):
    for key in kwargs:
        print(f"{key} - {kwargs[key]}")

fun(name="Kamila", age=18)"""
# decorator
#
# def select(input_func):
#     def output():
#         print("*************")
#         input_func()
#         print("*************")
#     return output
#
#
# @select
# def hello():
#     print("Hello")
#
# hello()


# def check(input_func):
#     def output(*args):
#         print("**********")
#         input_func(*args)
#         print("**********")
#     return output
#
#
# @check
# def print_person(name, age):
#     print(f"{name} - {age}")
#
# print_person("Abdullakh", 15)

#
# def check(input_func):
#     def output(*args):
#         name = args[0]
#         age = args[1]
#         if name == 'Saltanat':
#             name = 'Omurbek'
#
#         input_func(name, age)
#     return output
#
#
# @check
# def info(name, age):
#     print(f"{name} - {age}")
#
#
# info("Saltanat", 16)
# info('Abdullakh', -15)


# def check(input_func):
#     def output(*args):
#         result = input_func(*args)
#         if result < 0:
#             result = 0
#
#         return result
#     return output
#
#
# @check
# def get_sum(a, b):
#     return a + b
#
# print(get_sum(10, -15))


# for i in range(len(ls)):
#     ls[i] = ls[i]**2
#
# print(ls)

# l = [i**2 for i in ls]
# print(l)

# lm = list(map(lambda i: i ** 2, ls))
# print(lm)


# *args

# def get_obj(name):
#     print(name)
#
# get_obj('Omurbek', 'Bek')

# def get_objs(*args):
#     print(*args)
#
# get_objs(1, 2, 3, 4, 'Saltanat', True, [123,4, 43])


# **kwargs



# def fun(**kwargs):
#     print(kwargs)
#     # for key in kwargs:
#         # print(f"{key} = {kwargs[key]}")
#
# fun(name='Albina', age=23)


# ls = [] kwargs value name: Albina, ls = [Albina, 23]

"=========================================================Тапшырма========================================="
#1
"""def fun(**kwargs):
    return [(key, value) for key, value in kwargs.items()]

list1 = fun(name="Kamila", age=18)
print(list1)"""
#2
def decorat(func):
    def a1(*args):
        _numbers = [i ** 2 for i in args]
        return _numbers
    return a1

@decorat
def square(*args):
    return args
l2 = [1, 2, 3]
l1 = square(*l2)
print(l1)













