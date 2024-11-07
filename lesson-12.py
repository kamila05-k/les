"""a = {4, 2, 3}

a = {}
d = set(a)
print(type(d))"""


"""a = {1, 3, 5}
d = {8, 4, 6, 5}
f = a.update(d)
print(f)
print(a)"""

"""a = {1, 3, 5, 7}
a.pop()
print(a)"""

"""a = {1, 3, 5, 7, 8}
a.clear()
print(a)"""

"""a = {1, 3, 5, 7, 8}
a.add(4)
print(a)"""

"""a = {1, 3, 5, 7, 8}
a.discard(3)
print(a)"""

"""a = {1, 64, 5, 7, 8}
a1 = {64, 9, 2}
h = a.difference(a1)
print(h)
"""
"""a = {1, 64, 5, 7, 8}
a1 = {64, 9, 2, 5}
"h = a.intersection(a1)
h = a & a1
print(h)"""

"""a = {1, 64, 5, 7, 8}
a1 = {64, 9, 2, 5}
#f = a.union(a1)
f = a | a1
print(f)"""

"""a = {1, 64, 5, 7, 8}
g = a.remove(8)
print(a)"""

"""a = {'hello', True, (1, 2, 3)}
print(a)"""

"""a = {'one', 'two', 'three', 'six', 'seven'}
for i in a:
    if i == 'seven':
        print('7')
    else:
        print(i)"""

"""a = {'Kamila', 34, 67, 23, 'Asan'}
a1 = {34, 65, 98, 'Kamila', 32}
a2 = a.intersection(a1)
print(a2)"""


"""a1 = {'Nursultan', 'Omurbek', 'Manas'}
a2 = {'Madina', 'Saltanat', 'Kamila'}
f = a1.update(a2)
print(a1)
g = a1.remove('Nursultan')
g1 = a2.remove('Kamila')
print(a1)
print(a2)"""


"""farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
f = farm_1.intersection(farm_2)
print(f)

farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
f = farm_1.difference(farm_2)
print(f)"""


"=============================================================================Тапшырма============================================="
#1

"""months = {"Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"}

for i in months:
    print(i)
"""

#2
"""thisset = {"Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"}
print("July" in thisset)
print("Kamila" in thisset)
"""

#3
"""numbers = {1, 2, 2, 2, 3, 3, 4, 4, 5, 6}

for number in numbers:
    if number & 2 == 0:
        print(number)"""

#4
"""s_1 = {1, 2, 3}
s_2 = {1, 2, 5, 3}

for n in s_1:
    if s_1 <= s_2:
        print(True)"""

#5
"""s_1 = {1, 2, 3}
s_2 = {1, 2, 3, 4}

for number in s_2:
    if s_2 <= s_1:
        print(True)
    else:
        print(False)"""

