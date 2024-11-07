#zip
"""ls1 = [1, 2, 3]
ls2 = [100, 200, 300]

z = list(zip(ls1, ls2))
print(z)"""

"""d_keys = ["name", "last_name", "age"]
d_values = ["Kamila", "Таалайбек кызы", 18]

dict1 = dict(zip(d_keys, d_values))
print(dict1)"""

#Exception
"""def get_age(age):
    try:
        print(int(age))
    except:
        print("Nou")
get_age("Kamila")
"""

"""ls = [1, 2, 3, 4, 5]
try:
    print(ls[5])
except:
    print("index not sound")
    """

"""
ls = [1, '1', '2', 'Alina', '83', 'as']
ans = []
for i in ls:
    try:
        ans.append(int(i))
    except:
        continue
print(ans)
"""

d_keys = ["name", "last_name", "age", "gender"]
d_values = ["Kamila", "Таалайбек кызы", 18]

_dict = {}

for i in range(len(d_keys)):
    try:
        key = d_keys[i]
        value = d_values[i]
        _dict[key] = value
    except:
        continue

print(_dict)


