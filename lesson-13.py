# for

# name = 'Almaz'
# name2 = 'Alisa'
#
# count = 0

# for i in name:
#     if i == 'a':
#         count += 1
#
#
# print(count)
# print(name.count('a'))

#
# for i in name:
#     if i in name2:
#         print(i)


# for i in range(len(name)):
#     if name[i] == name2[i]:
#         print(name[i])


# while

# count = 5

# name = 'Manas'
#
# i = 0
#
#
# while i < len(name):
#     if name[i] == 'a':
#         print(name[i])
#
#     i += 1


# list comprehension

# ans = []
#
# for i in range(10):
#     ans.append(i)
#
# print("first method", ans)
#
# print("=============")
#
# ls = [i for i in range(10)]
# print("second method", ls)

# ls = [i for i in range(10) if i % 2 != 0]
# print(ls)


"""name = 'Manas'

ans = []

for i in name:
    if i != 'a':
        ans.append(i)
    else:
        ans.append('q')

print(ans)

ls = [i if i != 'a' else 'q' for i in name]
print(ls)
"""

"""name = 'Kamila'

ls = [i for i in name if i == 'a']
print(ls)"""

"""ls = [i for i in range(0, 101, 10)]
print(ls)"""

"===================================================Тапшырма============================================================================"
#1
"""s = 'Hello! How1 are you?'
ls = [i for i in s if not i.isalpha()]
print(ls)"""

#2
"""s = 'Hello! How1 are you?'
ls = [i for i in s if i.isalpha()]
print(ls)"""





















