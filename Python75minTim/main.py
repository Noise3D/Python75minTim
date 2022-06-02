# Python as fast as possible

# -----------------Data Types----------------------------
# Int

# 4553345
# -9
# 1020

# Float

# 23.3
# 1.0
# -234.2

# String

# '5.4'
# 'hello'
# 'hello"'
# "hello"

# Bool

# True  1
# False 0
# ----------------------outputs------------------------------

# print('Hello World!', end='\n   ')
# print('4.5',"Hello",87,    False)

# ---------------------variables------------------------------
#
# hello = 'tim'
# world = 'world'
# world = hello
# hello = 'no'
#
# print(hello, world)

# hello_world34
# 9hello  X

# ---------------------------input------------------

# name = input('Name: ')
# age = input('Age: ')
# print("hello", name, 'you are ', age, 'years old')

#-------------Arithmetic operators----------------------

# x = 10
# y = 3
# result = int(x / y)
# result = x ** y
# result = x // y
# result = x % y
# result = (x % y)*2
#
# print(result)
# B
# E
# D
# M
# A
# S
#
# num = input('Number: ') #-> string
# print(int(num) - 5)

# --------------string methods-------------------------

# hello = 'hello'.upper()
# hello = 'hello world'.lower()

# print(hello.count('l'))
# print(hello.capitalize())
# print(hello.upper())

# -------------------conditional operator--------------
# x = 'hello'
# y = 'yes'
# y = 3
#
# print(x * y)
# print(x + y)
# print(x, y)

#
# ==
# !=
# True
# False
# <=
# >=
#
# x = "hello"
# y = 'hello'
# print(x == y)

# print('a' > 'Z')
# print(ord('a'))

# print(7.0>7)

# result = 6 == 6
# print(result)

# -------------------chained conditionals--------------------------

# x = 7
# y = 8
# z = 0
#
# result1 = x == y
# result2 = y > x
# result3 = z < x + 2
#
# # and
# # or
# # not
#
# result4 = result1 or not result2 or result3
# print(result4)
# # print(not (False or True))
# print(not (False and True))

# ------------------------if/else/elif------------------------

# x = input('Name: ')
#
# # if conditon:
# if x == 'Tim':
#     print('You are great!')
#     if ...
# elif x == 'Joe':
#     print('bye Joe')
#
# elif x == 'Sarah':
#     print('bye Sarah')
#
# else:
#     print('No')
#
#
# print('Always do this')

# ----------------------List/Tuples------------------------

# stop
# start, stop
# start, stop, step

# x = [4, True, 'hi']
# x.append('hello')
# x.extend([4,5,3,6])
# x.pop(2)
# x[3] = 'bye'
# y = 'hi'
# z = x[:] #copy a list
# print(len(x), len(y))
# print(x[4])
# print(x)


# x = (1,4,2,2)
# x[0] = 7 #TypeError: 'tuple' object does not support item assignment
# print(x[0])

# x = [[], (), [[], [], [3,4,5,7]]]

# -------------------------For Loops----------------------

# range(start,stop,step)
#
# for i in range(10):
#     print(i)

# for i in range(10, -1, -1):
#     print(i)
#
# for i in [3,4,43,5,6,7]:
#     print(i)
#
# x = [3,54,676,78,7765,556]
#
# for i in range(len(x)):
#     print(x[i])

# for i, element in enumerate(x):
#     print(i, element)

# print(len(x))

# -----------------------While Loops----------------------------
# x = [3,4,42,3,2,5]

# while condition == True:
# i = 0
# while i < 10:
#     print('run')
#     i += 1
#     i *= 2
#
# while True:
#     print('bye')
#     i += 1
#     while True:
#         if i ==10:
#             break



# -----------------------Slice Operator-------------------------
# x = [0,1,2,3,4,5,6,7,8]
# y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
# s = "hello"
#
# # slice = [start:stop:step]
# # slice = x[0:4:2]
# # slice = x[::-1]
# # slice = s[::2]
# slice = (1,2,3,4,5,6,7,8)[::2]
#
# print(slice)
# -----------------------Sets-----------------------------------
# x = set(2,4,6,7,2,6,4,7)
# s = {4,32,2,2}
# s2 = [3,4,22,1]#slow
#
# print(s.union(s2))
# print(s.difference(s2))
# print(s.intersection(s2))
# print(s.symmetric_difference(s2))
# print(type({}))
# s.add(5)
# s.remove(32)
# print(s)
# print(4 in s)

# print(2 in s2)#slow

# ------------------------Dicts---------------------------------
# # x = {'key':Value}
# x = {'key':4}
# # print(x['key'])
# # x['key2'] = 5
# # x[2] = [3,7,9,1]
# # x[1] = [2,2]
# # print(x)
# # del x['key']
# # print(x)
# # print('key' in x)
# # print(x.values())
# # print(list(x.values()))
# # print(list(x.keys()))
# # for key, value in x.items():
# #     print(key, value)
# for key in x:
#     print(key, x[key])

# ------------------------Comprehensions------------------------
# new_list = [x for x in range(100)]
# print(new_list)



# x = [x%5 for x in range(5)]
# x = [[0 for x in range(100)] for x in range(5)]
# x = [i for i in range(100) if i % 5 == 0]
# x = {i for i in range(100) if i % 5 == 0}
# x = {i:0 for i in range(100) if i % 5 == 0}
# x = tuple(i for i in range(100) if i % 5 == 0)
# print(x)
# ------------------------Functions-----------------------------
# def func(x,y, z=None):
#     print('run', x, y, z)
#     return x * y, x / y
# r1, r2 = func(5,6,7)
# print(r1, r2)
# print(func(5,6))

# def func(x):
#     def func2():
#         print(x)
#
#     return func2
# # print(func(3)())
# x = func(3)
# x()

# ------------------------*args & **kwargs----------------------
# def func(*args, **kwargs):
#     pass
#
# x = [1,23,2345,4344]
# # print(x)
# print(*x)
# def func(x, y):
#     print(x,y)
#
# pairs = [(1,2), (3,4)]
#
# for pair in pairs:
#     func(*pair)   # * for List/Tuples
# for pair in pairs:
#     func(**{'x':2, 'y':5})#  ** for dectionares

#
# def func(*args, **kwargs):
#     print(args, kwargs)
#
# func(1,2,3,4,5,one=0, two=1)

# ------------------------Scope & Globals------------------------
# x = 'tim'
# def func(name):
#     x = name
# print(x)
# func('changed')
# print(x)

# x = 'tim'
# def func(name):
#     global x
#     x = name
# print(x)
# func('changed')
# print(x)

# ------------------------Exceptions-----------------------------
# raise Exception('Bad')
# raise FileExistsError('')
# ------------------------Handling Exceptions--------------------
# try:
#     x = 7 / 0
# except Exception as e:
#     print(e)
# finally:
#     print('finally')

# ------------------------Lambda---------------------------------
# x = lambda x: x + 5
# print(x(2))
# x = lambda x, y: x + y
# print(x(2, 32))

# ------------------------Map and Filter-------------------------
# x = [1,2,4,5,3,3,21,2,21,2,54,54,6565,6]
# mp = map(lambda i: i + 2, x)
# print(list(mp))

# x = [1,2,4,5,3,3,21,2,21,2,54,54,6565,6]
# mp = filter(lambda i: i % 2 == 0, x)
# print(list(mp))


# x = [1,2,4,5,3,3,21,2,21,2,54,54,6565,6]
# def func(i):
#     i = i * 3
#     return i % 2 == 0
#
# mp = filter(lambda i: i % 2 == 0, x)
# print(list(mp))

# ------------------------F Strings------------------------------
# tim = 89
# x = f'hello {6 + 8}{tim}   {34}'
# print(x)

# ------------------------Conclusion-----------------------------
# 📘 List of Topics 📘
# - Variables
# - Conditions
# - Chained Conditionals
# - Operators
# - Control Flow (If/Else)
# - Loops and Iterables
# - Basic Data Structures
# - Functions
# - Mutable vs Immutable
# - Common Methods
# - File IO
#---------------------------------
# - Object Oriented Programming
# - Data Structures
# - Comprehensions
# - Lambda Functions
# - Map, Filter
# - Collections
# - *args & **kwargs
# - Inheritance
# - Dunder Methods
# - PIP
# - Environments
# - Modules
# - Async IO
#--------------------------------
# - Decorators
# - Generators
# - Context Managers
# - Metaclasses
# - Concurrency
# - Parallelism
# - Testing
# - Packages
# - Cython

# -------------Object Oriented Programming (OOP)------------------
#
# # attributes = is/has
# # ex. name, age, height
#
# # methods = actions
# # ex. eat, sleep, make Youtube videos
#
# from car import Car
#
# car_1 = Car("Chevy","Corvette",2021,"blue")
# car_2 = Car("Ford","Mustang",2022,"red")
#
# # print(car_1.make)
# # print(car_1.model)
# # print(car_1.year)
# # print(car_1.color)
# #
# # car_1.drive()
# # car_1.stop()
#
#
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
#
# car_2.drive()
# car_2.stop()

# --------------------------------
#
# def hello():
#     print("hello")

# x = 1
# y = "hello"
#
# print(x + y)

# string = "hello"
# x = 1
# print(x.upper())

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # print(name)
#     def get_name(self):
#         return self.name
#
#     def meow(self, x):
#         return "meow" + str(x)
#
#     def bark(self):
#         print("bark")
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
#
# d = Dog("Tim", 34)
# print(d.get_age())
# d2 = Dog("Bill", 46)
# print(d2.get_name())
# d.set_age(23)
# print(d.get_age())
#
# # d.bark()
# # print(d.meow(5))
# #
# #
# # print(type(d))
# #




class Student:
    def __init__(self, name, age, grade):
        self.name = name    #             )
        self.age = age      #             > Atribut
        self.grade = grade  # 0-100       )

    def get_grade(self):    #             )
        return self.grade   #             > Metode
                            #             )

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, stundent):
        if len(self.students) < self.max_students:
            self.students.append(stundent)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
# print(course.students[0].name)
print(course.add_student(s3))
print(course.get_average_grade())



