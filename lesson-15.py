#set comprehension
"""ls = [1, 2, 3, 3, 5, 7, 12, 12, 90, 90]

s = {i**2 for i in ls}
s = {i for i in ls if i > 5}
print(s)"""

"""names = ['Saltanat', 'Madina', 'Muhammed', 'Bekzat', 'Albina', 'Manas', 'Bek', 'Abdullakh', 'Abubakr', 'Kamila', 'Omurbek', 'Meerim']
name = {names[i] + str(i) for i in range(len(names))}
print(name)"""

"""name = ['Saltanat', 'Madina', 'Muhammed', 'Bekzat', 'Albina', 'Manas', 'Bek', 'Abdullakh', 'Abubakr', 'Kamila', 'Omurbek', 'Meerim']
lens = [8, 6, 8, 6, 6, 5, 6, 9, 7, 6, 7, 6]
name1 = {name[i] + str(lens[i]) for i in range(len(lens))}
print(name1)"""
"""
name = 'Kamila'
print(iter(name))
i = iter(name)
print(next(i))
"""
# set comprehension


# s = set()
#
# ls = [1, 2, 3, 3, 5, 7, 12, 12, 90, 90]
#
# for i in ls:
#     s.add(i**2)
#
# print(s)
#
#
# s = {i for i in ls if i > 5}
# print(s)
# print(type(s))
# print(list(s))

# {'Saltanat0', Madina1, Muhammed2 ...........}

# s = {names[i]+str(i) for i in range(len(names))}
# print(s)

# names = ['Saltanat', 'Madina', 'Muhammed', 'Bekzat', 'Albina', 'Manas', 'Bek ', 'Abdullakh', 'Abubakr', 'Kamila', 'Omurbek', 'Meerim']
# lens = [8, 6, 8, 6, 6, 5, 4, 9, 7, 6, 7, 6]
#
# # {'Saltanat8', Madina6, Muhammed8 ...........}
#
# s = {names[i]+str(lens[i]) for i in range(len(names))}
# print(s)
#


# iter
# ls = [1, 2, 3]
# print(iter(ls))
# i = iter(ls)
#
# print(next(i))
# print(next(i))
# print(next(i))


# for i in ls:
#     print(i)


# generator

# ls = [i for i in range(10)]
# print(ls)

# t = (i for i in range(5))
# print(t)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))

# names = ['Saltanat', 'Madina', 'Muhammed', 'Bekzat', 'Albina', 'Manas', 'Bek ', 'Abdullakh', 'Abubakr', 'Kamila', 'Omurbek', 'Meerim']
#
# print(names)
# t = (names[i]+str(len(names[i])) for i in range(len(names)))
# print(t)
#
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))


"""name = 'Abdullakh'"""

# A0
# b1
# d2



"============================================Тапшырма============================================"
"""name = 'Kamila'
a = (name[i] + str(i) for i in range(len(name)))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
"""