"""import datetime
data = datetime.date(2005, 13, 9)
print(data)
"""

"""from datetime import datetime
now = datetime.now()
print(now)
print(now.strftime("%d-%m-%y"))
"""
"""from datetime import datetime
n = datetime.now()
print(n)
d = timeda()
a = n + d
print(a)"""

# datetime

# import datetime
#
# date = datetime.date(2005, 2, 29)
# print(date)
#



# from datetime import date, time, datetime

# date

# today = date.today()
# print(today)
#
# print(f"{today.day}-{today.month}-{today.year}")


# time
# tm = time(17, 20, 14)
# print(tm)


# datetime

# dt = datetime(2023, 7, 31, 17, 22)
# print(dt)


# today = datetime.today()
# print(today)


# date format

# from datetime import datetime
#
# d = datetime.strptime("31/07/2023 17:30", "%d/%m/%Y %H:%M")
# print(d)


from datetime import datetime, timedelta

# now = datetime.now()
# print(now)
# print(now.strftime("%d-%m-%Y"))
# print(now.strftime("%d/%m/%Y"))
# print(now.strftime("%d/%m/%y"))
# print(now.strftime("%d %B %Y (%A)"))
# print(now.strftime("%d/%m/%y %I:%M"))

# now = datetime.now()
# print(now)
#
# dif = timedelta()
# ans = now + dif
# print(ans)



#deadline = datetime(2023, 8, 1)
#now = datetime.now()
#now = datetime(2023, 8, 1)
#print(deadline)
#print(now)
#
# if deadline > now:
#     print("You have time for work")
# else:
#     print("You don't have time")


"""date1 = datetime(2000, 12, 31)
date2 = datetime.now()
#
#
ans = (date2-date1).days
print(ans)"""


# import math
#
# print(math.sqrt(48))


"""now = datetime.now()
print(now)
print(f"{now.year+10}-{now.month}-{now.day}")
"""


# open

#
# file = open("hello.txt", "w")
#
# file.close()

# write
# try:
#     file = open("hello.txt", "w")
#     try:
#         file.write("Hello world")
#     except Exception as e:
#         print(e)
# except Exception as e:
#     print(e)

# append write
# file = open('hello.txt', "a")
# file.write(" Abdullakh")
# file.close()

# read
# file = open('hello.txt', "r")
# a = file.read()
# print(a)


# with open("hello.txt", "a") as file:
#     file.write(", Bek")
#
# with open("hello.txt", "a") as file:
#     file.write("\nHow old are you?")


# with open("hello.txt", "r") as file:
    # print(file.read())
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.readlines())

#1
"""from datetime import datetime
dada = datetime(2023, 9, 17)
n = datetime.now()
now = datetime(2023, 9, 17)

if dada > now:
    print("большой")
else:
  print("маленкий")
"""
#2
"""from datetime import datetime
now = datetime.now()
print(f"{now.year}-{now.month+2}-{now.day-14}")
"""
#3
"""a = open("hello.txt", "w")
a.write("Таалайбек кызы Камила \n 18лет")
with open("hello.txt", "r") as a:
    print(a.read())
"""

