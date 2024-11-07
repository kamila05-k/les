"""name = input("Enter name: ")
a1 = input("Enter vowel: ")
for i in name:
    if i != a1:
        print(i)
"""

"""count =0
for i in range(1, 11):
    count += i
print(count)

"""

#for

# name = 'Abdullakh'
#
# for i in name:
#     print(i)
#

# i = 0
#
# while i < len(name):
#     print(name[i])
#     i += 1


# for i in range(1, 11):
#     print(i)


# for i in range(len(name)):
#     print(name[i])


# for i in range(31):
#     if i % 2 == 0 and i % 3 == 0:
#         print(i)
#
#
# for i in range(len(name)):
#     if i % 2 == 0:
#         print(name[i], i)

# tasks

# s = 'Hello1 World! How2 are$ you?'
#
#
# sl = s.split()
# print(sl)
#
# ans = ''
#
# for i in sl:
#     if not i.isalpha():
#         ans = ans + ' ' + i.strip('1!2$?')
#
# print(ans)


# name = 'Kamila'
#
# for i in range(len(name)):
#     if i % 2 != 0:
#         print(name[i])

#
# name = 'Abdullakh'
#
# for i in name:
#     # if i != 'a' and i != 'A':
#     if i not in 'a' and i not in 'A':
#         print(i)


# count = 0
# for i in range(1, 11):
#     count = count + i
#
# print(count)

# print(sum(range(1, 11)))

"===============================Тапшырма================================="

#1
# count = 0
# number = 1245465698235
# number1 = str(number)
# for i in range(number):
#     if i % 2 != 0:
#         print(number1[i])


#2
# for i in range(1, 11):
#     for j in range(1, 11):
#         result = i * j
#         result = i * j
#         print(f"{i} x {j} = {result}")
# print(result)
#
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")

for i in range(1, 11):
    for j in range(1, 11):
        indent = ' ' * (j - 1)
        print(f"{indent}{i} * {j} = {i * j}")
    print() 

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j:2}", end="\")
#     print()

















