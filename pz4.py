'''
square = lambda x: x ** 2
print(square(3))
print(square(4)) 
print(square(5)) 
'''
'''
numbers = [2, 4, 6, 8, 10]
num = list(map(lambda x: x / 2, numbers))
print(num) 
'''
'''
numbers = [5, 10, 15, 20, 25]
num = list(filter(lambda x: x < 20, numbers))
print(num) 
'''
'''
uppercase = lambda s: s.upper()
print(uppercase("hello"))
print(uppercase("world"))
'''
'''
fruits = ["apple", "banana", "cherry"]
lengths = list(map(lambda s: len(s), fruits))
print(lengths)
'''
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = list(filter(lambda x: x % 2 == 0, numbers))
print(num)
'''
'''
strings = ["APPLE", "BANANA", "CHERRY", "DATE"]
str = list(map(lambda s: s.lower(), strings))
print(str)
'''
'''
numbers = [12, 15, 18, 20, 24, 30]
num = list(map(lambda x: x + 3 if x % 5 == 0 else x, numbers))
print(num)
'''
'''
def difference(a, b):
    return a - b

list1 = [10, 20, 30]
list2 = [4, 5, 6]
result = list(map(difference, list1, list2))
print(result)
'''
