"""def max1(max_1):
    print(max(max_1))

max1([1, 2, 3, 4, 5])

def max1(max_1):
    print(min(max_1))

max1([1, 2, 3, 4, 5])
"""

"""def nam(name):
    return name[::-1]
print(nam('Kamila'))
                     """


def even(x):
    for i in range(1, 101):
        if x % 2 == 0:
            print(i ** 2)
even(0)



"======================================+Тапшырма+============================================="
"min"
#1

"1"
"""def my_min(iterable, default=None, key=None):
    if not iterable:
        if default is not None:
            return default
        паднимат
        raise ValueError("min() arg is an empty sequence")

    min_value = None
    for item in iterable:
        if min_value is None or (key and key(item) < key(min_value)) or (not key and item < min_value):
            min_value = item
print(my_min(iterable='5'))"""


"2"
"""
numbers = [5, 2, 8, 1, 9]
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(minimum)"""

"3"

"""def min_custom(numbers):
    minimum = numbers[0]
    for num in numbers:
        minimum = num if num < minimum else minimum
    print(1, 2, 3, 4, 5)
"""
"max"
#2
"1"
"""def max_custom(numbers):
    maximum = numbers[0]
    for num in numbers:
        maximum = num if num >= maximum else maximum
    print(1,2,3,4,5)"""

"2"
"""numbers = [5, 2, 8, 1, 9]
maximum = numbers[0]
for num in numbers[1:]:
    if num > maximum:
        maximum = num
print(maximum)"""

"sum"
#3
"1"
"""def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [5, 2, 8, 1, 9]
result = calculate_sum(numbers)
print(result)
"""

"(================================================)"

"""def min_custom(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum
numbers = [5, 2, 8, 1, 9]
result = min_custom(numbers)
print(result)"""

"2"
"""def max_custom(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
numbers = [5, 2, 8, 1, 9]
result = max_custom(numbers)
print(result)"""



"3"
"""def cumsum(numbers):
    result = []
    total = 0
    for num in numbers:
        total += num
        result.append(total)
    return result
numbers = [1, 2, 3, 4, 5]
result = cumsum(numbers)
print(result)"""







