# shortcuts
# Ctrl+/
# Ctrl+D
# shift+shift
# alt+control+shift+J
# Alt+4
# Alt+X

# ---------------------------------------

# variable = a container for a value. Behaves as the value that it contains

# #string = a series of characters
# first_name = "Bro"
# last_name = "Code"
# full_name = first_name +" "+ last_name
# print("Hello "+full_name)
# print(type(first_name))
#
# #int = a whole integer
# age = 21
# age += 1
# print("Your age is: "+str(age))
# # print(type(age))
#
# #float = a decimal number
# height = 250.5
# print("Your height is: "+str(height)+"cm")
# # print(type(height))
#
# #boolean = True or False
# human = True
# print("Are you a human: "+str(human))
# print(type(human))

# ---------------------------------------
# multiple assignment = allows us to assign multiple variables at the same time in one line of code

# name = "Bro"
# age = 21
# attractive = True
#
# name, age, attractive = "Bro", 21, True
#
# print(name)
# print(age)
# print(attractive)
#
# # Spongebob = 30
# # Patrick = 30
# # Sandy = 30
# # Squidward = 30
#
# # Spongebob = Patrick = Sandy = Squidward = 30
#
# # print(Spongebob)
# # print(Patrick)
# # print(Sandy)
# # print(Squidward)

# ---------------------------------------
# string methods
# name = "Bro code"

# print(len(name))
# print(name.find("r"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o","s"))
# print(name*3)

# ---------------------------------------
# type cast

# x = 1    # int
# y = 2.0  # float
# z = "3"  # str
# w = True # Bool
# y = int(y)
# z = int(z)
# x = float(x)
# w = str(w)
#
# print(x)
# print(y)
# print(z*3)
# print(w*2)

# ---------------------------------------
# user input

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input(("How tall are you?: ")))
# age = age + 1
# print("Hello " +name)
# print("You are " +str(age)+" years old")
# print("you are " +str(height)+"cm tall")


# ---------------------------------------
# math functions

# import math

# pi = -3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x, y, z))
# print(min(x, y, z))


# ---------------------------------------
# string slicing

#            indexing[] or slice()
#            [start:stop:step]

# name = "Bro Code"
#
# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[::3]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

#
# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
#
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])


# ---------------------------------------
# if statements

# age = int(input("How old are you?: "))
# if age == 100:
#     print("You are centery old!")
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")

# ---------------------------------------
# logical operators (and, or, not)

# temp = int(input("what is the tempeture outside?: "))
#
# if not(temp >= 0 and temp <= 30):
#     print("the temperature is bad today!")
#     print("stay inside!")
#
# elif not(temp < 0 or temp > 30):
#     print("the temperture is good today!")
#     print("go outside!")


# ---------------------------------------
# while loops


# while 1==1:
#     print("Help! I'm stuck in a loop! ")

# name = ""
#
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Help!" + name)

# ----------------------------------------------
# for loop
#   wile loop = unlimited
#   for loop = limited

# for i in range(10+1):
#     print(i+1)

# for i in range(50, 100+1, 2):
#     print(i)

# for i in "Bro Code":
#     print(i)
# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# ----------------------------------------------
# nested loops

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# ----------------------------------------------
# loop Control Statements

# break
# continue
# pass

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)

# ----------------------------------------------
# list

# food = ["pizza", "hamburger", "hotdog", "spaghetti"]
#
# food[0] = "sushi"
#
# food.append("ice cream")
# food.remove("hotdog")
# food.pop()
# food.insert(0,"cake")
# food.sort()
# food.clear()


# print(food[0])

# for x in food:
#     print(x)


# ----------------------------------------------
# 2D list

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks, dinner, dessert]
#
# print(food[0][0])


# ----------------------------------------------
# tuple = unchangeable

# student = ("Bro", 21, "male")
#
# print(student.count("Bro"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
# if "Bro" in student:
#     print("Bro is here!")


# ----------------------------------------------
# set

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}
#
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)
# for x in dinner_table:
#     print(x)
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# for x in utensils:
#     print(x)

# ----------------------------------------------
# dictionary

# capitals = {'USA':'Wasington DC', 'India':'New Dehli', 'China':'Baijing', 'Russia':'Moscow'}
#
# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
#  capitals.clear()
#
#  print(capitals['Russia'])
#  print(capitals['Germany'])
#  print(capitals.get('Germany'))
#  print(capitals.keys())
#  print(capitals.values())
#  print(capitals.items())
#
# for key, value in  capitals.items():
#     print(key, value)

# ----------------------------------------------
# index operator

# name = "bro Code!"
# # if(name[0].islower()):
# #     name = name.capitalize()
#
# # print(name)
#
# first_name = name[:3].upper()
# last_name = name[4:].lower()
# last_character = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_character)


# ----------------------------------------------
# function

# def hello(first_name, last_name, age):
#     print("Hello!" + first_name +" "+last_name)
#     print("You are "+ str(age)+" Years old")
#     print("Have a nice day!")
#
# # hello()
# # hello()
# # hello("Bro")
# # my_name = "Bro"
# # hello(my_name)
#
# hello("Bro", "Code", 21)

# ----------------------------------------------
# return statemant

# def multiply(num1,num2):
# #    result = num1 * num2
# #    return result
#     return num1 * num2
# # print(multiply(6,8))
# x = multiply(6,8)
# print(x)

# ----------------------------------------------
# keyword arguments

# def hello(first, middle, last):
#     print("Hello "+first+" "+middle+" "+last)
#
# #hello("Bro", "Dude", "Code")
# hello(last="Bro",middle="Dude",first="Code")


# ----------------------------------------------
# nested functions calls

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))

# ----------------------------------------------
# scope
# L = local
# E = Enclosing
# G = Global
# B = Build-in

# name = "Bro" # global scope
# def display_name():
#    # name = "Code" # local scope
#     print(name)
# display_name()
# print(name)

# ----------------------------------------------
# *args

# def add(num1,num2):
#     sum = num1 + num2
#     return sum

# def add(*args):
#     sum = 0
#     args = list(args)
#     args[0] = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(1,2,3,4,5,6))

# ----------------------------------------------
# **kwargs
#
# def hello(**kwargs):
# #    print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("Hello",end=" ")
#     for key, value in kwargs.items():
#         print(value,end=" ")
# hello(title="Mr.",first="Bro",middle="Dude",last="Code")

# ----------------------------------------------
# str.format()

# animal = "cow"
# item = "moon"

# print("the "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over {1} the {0}".format(animal, item))
# print("The {nam2} jumped {nam2} over the {nam1}".format(nam2="cow", nam1="moon"))

# text = "the {} jumped over the {}"
# print(text.format(animal, item))

# name = "Bro"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))

# number = 3.14159
# number2 = 1000
# print("The number pi is {:.2f}".format(number))
# print("The number pi is {:.3f}".format(number2))
# print("The number pi is {:,}".format(number2))
# print("The number pi is {:b}".format(number2))
# print("The number pi is {:o}".format(number2))
# print("The number pi is {:x}".format(number2))
# print("The number pi is {:E}".format(number2))


# ----------------------------------------------
# random numbers

# import random
#
# x = random.randint(1,6)
# y = random.random()
#
# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)
#
# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
# random.shuffle(cards)
# print(x)
# print(y)
# print(z)
# print(cards)

# ----------------------------------------------
# exception

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denuminator = int(input("Enter a number to divide by: "))
#     result = numerator / denuminator
#     print(result)
#   except ZeroDivisionError:
#         print("You cannot divide by zero! idiot!")
#   except ValueError:
#         print("enter only numbers please")
# except Exception as e:
#     print(e)
#     print("something went wrong:(")
# else:
#     print(result)
# finally:
#     print("This will always execute")
#
# ----------------------------------------------

# import os
# path = "C:\\Users\\User\\Desktop\\test.txt"
# if os.path.exists(path):
#     print("that location exists!")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("That is a directory!")
# else:
#     print("that location doesn't exist!")

# ----------------------------------------------
#
# with open("test.txt") as file:
#     print(file.read())
#
# print(file.closed)
# ----------------------------------------------
#
# text = "yooooo\n This is some text\n Have a good one!"
# with open('test.txt','w') as file:
#     file.write(text)
# ----------------------------------------------

# import shutil
#
# shutil.copyfile('test.txt','copy.txt')

# ------------------------------------------------
# import os
#
# source = "test.txt"
# destination = "C:\\Users\\User\\Desktop\\test.txt"
#
# try:
#     if os.path.exists(destination):
#         print("there is already a file there")
#     else:
#         os.replace(source,destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+" was not found")
#

# ---------------------------------------------------
# import os
# import shutil
#
# path = "Folder"
# try:
#     # os.remove(path)
#     # os.rmdir(path)
#     # shutil.rmtree(path)
#
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that")
# else:
#     print(path+" was deleted")

# ---------------------------------------------------
#
# import module as msg
#
# msg.hello()
# msg.bye()

# help("modules")
# -------------------------Games----------------------


# import random
# while True:
#     choices = ["rock","paper","scissors"]
#     computer = random.choice(choices)
#     player = None
#     while player not in choices:
#         player = input("rock. paper, scissors?: ").lower()
#     if player == computer:
#         print("computer: ",computer)
#         print("player: ",player)
#         print("Tie!")
#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")
#     elif player == "scissors":
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")
#     elif player == "paper":
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")
#     play_again = input("Play again? (yes/no): ").lower()
#     if play_again !="yes":
#         break
# print("bye!:(")

# -----------------------------------------------------------

# def new_game():
#
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print("----------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C, D): ")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key),guess)
#         question_num += 1
#     display_score(correct_guesses, guesses)
#
#
# # -----------------------------
# def check_answer(answer, guess):
#     if answer == guess:
#         print("Correct!")
#         return 1
#     else:
#         print("Wrong!")
#         return 0
#
# # -----------------------------
#
# def display_score(correct_guesses, guesses):
#     print("-------------------------------")
#     print("Results")
#     print("-------------------------------")
#
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
#
#     print("guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()
#
#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: "+str(score)+"%")
#
# # -----------------------------
#
# def play_again():
#
#     response = input("Do you want to play again?: (yes or no): ")
#     response = response.upper()
#
#     if response == "YES":
#         return True
#     else:
#         return False
# # -----------------------------
#
# questions = {
#     "Who created Python? ": "A",
#     "What year was Python created?: ": "B",
#     "Python is tributed to which comedy group?: ": "C",
#     "Is the Earth round?: ": "A",
# }
#
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#            ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]
#
# new_game()
#
# while play_again():
#     new_game()
#
# print("Byeeee !")
# ---------------------OOP---------------------

# from Car import Car
#
# car_1 = Car("chevy","Corvette",2021,"blue")
# car_2 = Car("Ford","Mustang",2022,"red")
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
#
# car_2.drive()
# car_2.stop()

# --------------------inheritance-----------------------------

# class Animal:
#
#     alive = True
#
#     def eat(self):
#         print("This animal is eating")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running")
#
# class Fish(Animal):
#     def swim(self):
#         print("This fish can swimming")
#
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk can fly")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# # print(rabbit.alive)
# # fish.eat()
# # hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()
# ------------------------multi-level inheritance----------------
#
# class Organism:
#
#     alive = True
#
# class Animal(Organism):
#
#     def eat(self):
#         print("This animal is eating")
#
# class Dog(Animal):
#
#     def bark(self):
#         print("this dog is barking")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

#-----------multiple inheritance-----------------------------------
#
# class Prey:
#
#     def flee(self):
#         print("this animal flees")
#
# class Predator:
#
#     def hunt(self):
#         print("This animal is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()
# --------------------method overriding--------------------------------

# class Animal:
#
#     def eat(self):
#         print("This animal is eating")
#
# class Rabbit(Animal):
#     def eat(self):
#         print("This rabbit is eating a carrot")
#
# rabbit = Rabbit()
# rabbit.eat()

# --------------method chaining---------------------------

# class Car:
#
#     def turn_on(self):
#         print("you start the engine")
#         return self
#
#     def drive(self):
#         print("you drive the car")
#         return self
#
#     def brake(self):
#         print("you step on the brakes")
#         return self
#     def turn_off(self):
#         print("you turn off the engine")
#         return self
#
# car = Car()
#
# # car.turn_on().drive()
#
# # car.brake().turn_off()
#
# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()

# ----------------super() = Function------------------------------
#
# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         super().__init__(length,width)
#     def area(self):
#         return self.length*self.width
#
# class Cube(Rectangle):
#
#     def __init__(self, length, width, height):
#         super().__init__(length,width)
#         self.height = height
#     def volume(self):
#         return self.length*self.width*self.height
#
# square = Square(3, 3)
# cube = Cube(3, 3, 3)
#
# print(square.area())
# print(cube.volume())

# -----------------abstract classes, methods---------------------------
#
# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def go(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#
#     def go(self):
#         print("you drive the car")
#
#     def stop(self):
#         print("This car is stopped")
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print("you ride the motorcycle")
#
#     def stop(self):
#         print("This motorcycle is stopped")
#
# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# vehicle.go()
# car.go()
# motorcycle.go()
# car.stop()
# motorcycle.stop()

# -----------------------------------------------------

# class Car:
#
#     color = None
#
# class Motorcycle:
#
#     color = None
#
# def change_color(vehicle,color):
#     vehicle.color = color
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# bike_1 = Motorcycle()
#
# change_color(car_1,"red")
# change_color(car_2,"white")
# change_color(car_3,"blue")
# change_color(bike_1,"purple")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)

# ---------------------Dock typing---------------------------------
#
# class Duck:
#
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is qwuacking")
#
# class Chicken:
#
#     def walk(self):
#         print("This chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
# class Person():
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter !")
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(duck)

#------------------walrus operator :=-----------------------

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

#
# foods = list()
# while food := input("What food do you like?: ") !="quit":
#     foods.append(food)
# ----------------------------------------------------------

# def hello():
#     print("Hello")
# hello()
# print(hello)
# hi = hello
# hello()
# hi()
# print(hi)



# say = print
# say("Whoa! I can't believe this works! :O")

# -------------Higher Order Function-------------------------

# def loud(text):
#     return text.upper()
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
# hello(loud)
# hello(quiet)

# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend
#
# divide = divisor(2)
# print(divide(10))
#

# ---------------lambda function-------------------------

# def double(x):
#     return x * 2
#
# print(double(5))
#
#
# double = lambda x:x * 2
# multiply = lambda x, y: x * y
# add = lambda x, y, z: x * y *z
# full_name = lambda first_name, last_name:first_name +" "+last_name
# age_name = lambda age:True if age >= 18 else False
#
# print(double(5))
# print(multiply(5,6))
# print(add(5,6,7))
# print(full_name("bro", "Cod"))
# print(age_name(19))

# ----------------------sort()------------------------------------

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]
#
# # students.sort(reverse=True)
# sorted_students = sorted(students,reverse=True)
#
# for i in sorted_students:
#     print(i)

#
# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr.Krabs", "C", 78)]
# grade = lambda grades:grades[1]
# students.sort(key=grade,reverse=True)
#
# for i in students:
#     print(i)

# ---------------------map------------------------------------

# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]
#
# to_euros = lambda data: (data[0],data[1]*0.82)
# store_euros = list(map(to_euros, store))
# for i in store_euros:
#     print(i)

# ---------------------filter--------------------------------

# friends = [("Rachel", 19),
#            ("Monice", 18),
#            ("Phoebe", 17),
#            ("Joey", 16),
#            ("Chandler", 21),
#            ("Ross", 20)]
#
# age = lambda data:data[1] >= 18
# drinking_buddies = list(filter(age, friends))
# for i in drinking_buddies:
#     print(i)

# -----------------reduce---------------------------------

# import functools
# # latters = ["H", "E", "L", "O"]
# # word = functools.reduce(lambda x, y,:x + y,latters)
# # print(word)
#
# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y,:x * y,factorial)
# print(result)

# -------------------list comprehansion---------------------------

# squares = []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)
#
# squares = [i*i for i in range(1,11)]
# print(squares)

# students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
# passed_students = list(filter(lambda x: x >= 60, students))
# print(passed_students)

# students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
# passed_students = [i if i >= 60 else "FAILED" for i in students]
# print(passed_students)

# -----------------dictionary comprehension-----------------------

# cities_in_F = {'New york': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)

# weather = {'New york': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
#
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# cities = {'New york': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)


#
# def check_temp(value):
#     if value >=70:
#         return "HOT"
#     elif 69 >= value >= 40:
#         return "WARM"
#     else:
#         return "COLD"
#
# cities = {'New york': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)

# -------------------------zip-----------------------------

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ["p@ssword", "abc123", "guest"]
#
# users = dict(zip(usernames, passwords))
# print(type(users))
# for key,value in users.items():
#
#     print(key+" : "+value)


# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")
# login_date = ["1/1/2021","1/2/2021","1/3/2021"]
#
# users = zip(usernames,passwords,login_date)
# for i in users:
#     print(i)


# ----------------------if __name__ == '__main__'--------------------
#
# if __name__ == '__main__':
#     pass

# import module_two
# print(__name__)
# print(module_two.__name__)

# ---------------------import time--------------------------

import time

# print(time.ctime(1000000000))

# print(time.time())

# print(time.ctime(time.time()))

# time_object = time.localtime()
# time_object = time.gmtime()
# print(time_object)
#
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)


# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# ------------------------multithreading--------------------------------

# import threading
# import time
#
# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")
#
# def drink_coffee():
#     time.sleep(4)
#     print("You drank coffee")
#
# def study():
#     time.sleep(5)
#     print("You finish studying")
#
# x = threading.Thread(target=eat_breakfast(), args=())
# x.start()
#
# y = threading.Thread(target=drink_coffee(), args=())
# y.start()
#
# z = threading.Thread(target=study(), args=())
# z.start()
#
# x.join()
# y.join()
# z.join()
#
# # eat_breakfast()
# # drink_coffee()
# # study()
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())

# ---------------------daemon thread-------------------------

# import threading
# import time
#
# def timer():
#     print()
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for:", count, "seconds")
#
# x = threading.Thread(target=timer, daemon=True)
# x.start()
#
# answer = input("Do you wish to exit?")

# -------------------multiprocessing-------------------------------

# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
#
#
# def main():
#
#     print(cpu_count())
#
#     a = Process(target=counter, args=(500000000,))
#     b = Process(target=counter, args=(500000000,))
#
#     a.start()
#     b.start()
#
#     a.join()
#     b.join()
#
#     print("finished in:",time.perf_counter(), "seconds")
#
# if  __name__ == '__main__':
#     main()

# ---------------------GUI program-----------------

# from tkinter import *
#
# window = Tk()
# window.geometry("420x420")
# window.title("Bro Code")
# icon = PhotoImage(file='Logo.png')
# window.iconphoto(True,icon)
# window.config(background="#5cfcff")
# window.mainloop()

# --------------Label-------------------------


# from tkinter import *
#
# window = Tk()
#
# photo =PhotoImage(file='Logo.png')
#
# label = Label(window,
#               text='Hello World',
#               font=('Arial',40,'bold'),
#               fg='#00FF00',
#               bg='black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=30,
#               image=photo,
#               compound='bottom')
#
# label.pack()
#
# # label.place(x=0,y=0)
#
# window.mainloop()

# -------------------------button----------------------------------

# from tkinter import *
#
# count = 0
#
# def click():
#     global count
#     count+=1
#     print(count,"You clicked the button!")
# window = Tk()
# photo = PhotoImage(file="Logo.png")
#
# button = Button(window,
#                 text="click me!",
#                 command=click,
#                 font=("Comic Sans",30),
#                 fg="#00FF00",
#                 bg="black",
#                 activeforeground="#FFFF00",
#                 activebackground="#00FFFF",
#                 state=ACTIVE,
#                 image=photo,
#                 compound="bottom")
# button.pack()
# window.mainloop()

# ----------------------------entery widget-------------------------------------

# from tkinter import *
#
# def submit():
#     username = entry.get()
#     print("Hello "+username)
#     entry.config(state=DISABLED)
#
#
# def delete():
#     entry.delete(0,END)
#
# def backspace():
#     entry.delete(len(entry.get())-1,END)
#
#
# window = Tk()
#
# entry = Entry(window,
#               font=("Arial",50),
#               fg="#00FF00",
#               bg="black",
#               show="*")
#
# entry.insert(0,'Spongebob')
# entry.pack(side=LEFT)
# submit_button = Button(window,text="submit",command=submit)
# submit_button.pack(side=RIGHT)
#
# delete_button = Button(window,text="delete",command=delete)
# delete_button.pack(side=RIGHT)
#
#
# backspace_button = Button(window,text="backspace",command=backspace)
# backspace_button.pack(side=RIGHT)
#
# window.mainloop()

# ----------------------check button---------------------------------

# from tkinter import *
# def display():
#     if(x.get()):
#         print("You agree!")
#     else:
#         print("You don't agree :(")
# window = Tk()
#
# x = BooleanVar()
# python_photo = PhotoImage(file='Python.png')
#
# check_button = Checkbutton(window,
#                            text='I agree to something',
#                            variable=x,
#                            onvalue=True,
#                            offvalue=False,
#                            command=display,
#                            font=('Arial',20),
#                            fg='#00FF00',
#                            bg='black',
#                            activeforeground='#00FF00',
#                            activebackground='black',
#                            padx=25,
#                            pady=10,
#                            image=python_photo,
#                            compound='left')
#
# check_button.pack()
# window.mainloop()

# ------------------------radio button--------------------------------------

# from tkinter import *
#
# food = ["pizza","hamburger","hotdog"]
#
# def order():
#     if(x.get()==0):
#         print("You ordered pizza!")
#     elif(x.get()==1):
#         print("You ordered a hamburger!")
#     elif(x.get()==2):
#         print("You ordered hotdog!")
#     else:
#         print("huh?")
#
# window = Tk()
#
# pizzaImage = PhotoImage(file='pizza.png')
# hamburgerImage = PhotoImage(file='hamburger.png')
# hotdogImage = PhotoImage(file='hot-dog.png')
# foodImages = [pizzaImage, hamburgerImage, hotdogImage]
#
# x = IntVar()
#
# for index in range(len(food)):
#     radiobutton = Radiobutton(window,
#                               text=food[index], #adds text to radio button
#                               variable=x,       #groups radiobuttons together if they share the same variable
#                               value=index,      #assigns each radiobutton a different value
#                               padx = 25,        #adds padding on x-axis
#                               pady = 30,
#                               font=("Impact",50),
#                               image = foodImages[index], #adds image to radiobutton
#                               compound = 'left',
#                               indicatoron=0,
#                               width = 550,
#                               command=order
#                               )
#     radiobutton.pack(anchor=W)
#
# window.mainloop()

# -------------------------slider-------------------------------------

# from tkinter import *
# def submit():
#     print("The temperature is: "+str(scale.get())+ "degrees C")
#
# window = Tk()
#
# hotImage = PhotoImage(file='hot.png')
# hotLabel = Label(image=hotImage)
# hotLabel.pack()
#
# scale = Scale(window,
#               from_=100,
#               to=0,
#               length=600,
#               orient=VERTICAL, #orientation of scale
#               font = ('Consolas',20),
#               tickinterval = 10, #adds numeric indicators for value
#               #showvalue = 0, #hide corrent value
#               resolution = 5, #increment of slider
#               troughcolor = '#69EFFF',
#               fg = '#FF1C00',
#               bg = '#111111'
#               )
#
# scale.set((scale['from']-scale['to'])/2+scale['to'])
#
#
# scale.pack()
#
# coldImage = PhotoImage(file='cold.png')
# coldLabel = Label(image=coldImage)
# coldLabel.pack()


# button = Button(window,text='submit',command=submit)
# button.pack()
# window.mainloop()

# -----------------------listbox------------------------------

# def submit():
#
#     food = []
#
#     for index in listbox.curselection():
#         food.insert(index,listbox.get(index))
#
#     print("You have ordered: ")
#     for index in food:
#         print(index)
#
#     #print(listbox.get(listbox.curselection()))
#
# def add():
#     listbox.insert(listbox.size(),entryBox.get())
#     listbox.config(height=listbox.size())
#
# def delete():
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)
#
#     # listbox.delete(listbox.curselection())
#     listbox.config(height=listbox.size())
#
# from tkinter import *
#
# window = Tk()
#
# listbox = Listbox(window,
#                   bg="#f7ffde",
#                   font=("Constantia",35),
#                   width=12,
#                   selectmode=MULTIPLE
#                   )
# listbox.pack()
#
# listbox.insert(1,"pizza")
# listbox.insert(2,"pasta")
# listbox.insert(3,"garlic bread")
# listbox.insert(4,"soup")
# listbox.insert(5,"salad")
#
# listbox.config(height=listbox.size())
#
# entryBox = Entry(window)
# entryBox.pack()
#
# addButton = Button(window,text="add",command=add)
# addButton.pack()
#
# deleteButton = Button(window,text="delete",command=delete)
# deleteButton.pack()
#
# submitButton = Button(window,text="submit",command=submit)
# submitButton.pack()
#
# window.mainloop()

# ------------------messagebox-----------------------------

from tkinter import *

from tkinter import messagebox #import messagebox library
# def click():

    # messagebox.showinfo(title='This is a info message box',message='You are a person')
    # messagebox.showwarning(title='WARNING!',message='You have a VIRUS!!!')
    # messagebox.showerror(title='ERROR!',message='someting went wrong :(')
    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
    #     print('You did a thing!')
    # else:
    #     print('You canceled a thing! :(')
    # if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the thing?'):
    #     print('You retried a thing!')
    # else:
    #     print('You canceled a thing! :(')






# window = Tk()
# button = Button(window,command=click,text='click me')
# button.pack()
# window.mainloop()

# -------------------colorchooser----------------------------------

# from tkinter import *
# from tkinter import colorchooser  #submodule
#
# def click():
#     # color = colorchooser.askcolor()
#     # print(color)
#     # colorHex = color[1]
#     # print(colorHex)
#     window.config(bg=colorchooser.askcolor()[1])  #change background color
#
# window = Tk()
#
# window.geometry("420x420")
#
# button = Button(text='click me',command=click)
# button.pack()

# window.mainloop()

# ---------------------text widget---------------------------------
#
# from tkinter import *
# def submit():
#     input = text.get("1.0",END)
#     print(input)
# window = Tk()
# text = Text(window,
#             bg="light yellow",
#             font=("Ink Free",25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20,
#             fg="purple")
# text.pack()
# button = Button(window,text="submit",command=submit)
# button.pack()
# window.mainloop()

# -------------------------file dialog-------------------------------------
#
# from tkinter import *
#
# from tkinter import filedialog
#
# def openFile():
#     filepath=filedialog.askopenfilename(initialdir="C:\\Users\\",
#                                         title="Open file okay?",
#                                         filetypes=(("text files","*.txt"),
#                                         ("all files","*.*")))
#     file = open(filepath,'r')
#     print(file.read())
#     file.close()
#
# window = Tk()
# button = Button(text="Open",command=openFile)
# button.pack()
# window.mainloop()

# -------------------save file--------------------------------

# from tkinter import *
# from tkinter import filedialog
#
# def saveFile():
#     file = filedialog.asksaveasfile(initialdir="C:\\Users\\User\\PycharmProjects\\BroCode",
#                                     defaultextension='.txt',
#                                     filetypes=[
#                                         ("Text file",".txt"),
#                                         ("HTML file", ".html"),
#                                         ("All files", ".*"),
#                                     ])
#
#     if file is None:
#         return
#     filetext = str(text.get(1.0,END))
#     # filetext = input("Enter some text I guess: ")
#     file.write(filetext)
#     file.close()
#
#
# window = Tk()
# button = Button(text='save',command=saveFile)
# button.pack()
# text = Text(window)
# text.pack()
#
# window.mainloop()

# ---------------------Menu Bar-------------------------------

# from tkinter import *
#
# def openFile():
#     print("File has been opened!")
#
# def saveFile():
#     print("File has been saved!")
#
# def cut():
#     print("you cut some text!")
#
# def copy():
#     print("you copy some text!")
#
# def paste():
#     print("you paste some text!")
#
# window = Tk()
#
# openImage = PhotoImage(file="file.png")
# saveImage = PhotoImage(file="save.png")
# exitImage = PhotoImage(file="exit.png")
#
# menubar = Menu(window)
# window.config(menu=menubar)
#
# fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="File",menu=fileMenu)
# fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
# fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
# fileMenu.add_separator()
# fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')
#
# editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="Edit",menu=editMenu)
# editMenu.add_command(label="Cut",command=cut)
# editMenu.add_command(label="Copy",command=copy)
# editMenu.add_command(label="Paste",command=paste)
#
# window.mainloop()

# -----------------------frame-----------------------------

# from tkinter import *
# window = Tk()
#
# frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# # frame.pack(side=BOTTOM)
# frame.place(x=100,y=100)
#
#
# Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
# Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)
#
#
# window.mainloop()

# -----------------------------new window-------------------------------
#
# from tkinter import *
#
#
# def create_window():
#     # new_window = Toplevel()
#     new_window = Tk()
#     old_window.destroy()
#
# old_window = Tk()
# # window = Tk()
# Button(old_window,text="create new window",command=create_window).pack()
#
# old_window.mainloop()

# ---------------------Tabs--------------------------------

# from tkinter import *
# from tkinter import ttk
#
# window = Tk()
# notebook = ttk.Notebook(window)
#
# tab1 = Frame(notebook)
# tab2 = Frame(notebook)
#
# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True, fill="both")
#
# Label(tab1,text="Hello, this is tab#1", width=50,height=25).pack()
# Label(tab2,text="Hello, this is tab#2", width=50,height=25).pack()
#
#
# window.mainloop()

# -----------------geometry manager------------------------------
#
# from tkinter import *
#
# window = Tk()
#
# titleLabel = Label(window,text="Enter your info", font=("Arial",25)).grid(row=0,column=0,columnspan=2)
#
# firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
# firstNameEntry = Entry(window).grid(row=1,column=1)
#
# lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
# lastNameEntry = Entry(window).grid(row=2,column=1)
#
# emailNameLabel = Label(window,text="email: ",bg="blue",width=30).grid(row=3,column=0)
# emailNameEntry = Entry(window).grid(row=3,column=1)
#
# submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)
#
#
#
# window.mainloop()


# -----------------Progress bar---------------------------

# from tkinter import *
# from tkinter.ttk import *
# import time
#
# def start():
#     GB = 50
#     download = 0
#     speed = 2
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)*100))+"%")
#         text.set(str(download)+"/"+str(GB)+" GB completed")
#         window.update_idletasks()
#
# window = Tk()
#
# percent = StringVar()
# text = StringVar()
#
#
# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)
#
# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()
#
# button = Button(window,text="download",command=start).pack()
#
# window.mainloop()

# ------------------------canvas------------------------------------
#
# from tkinter import *
# window = Tk()
#
# canvas = Canvas(window,height=500,width=500)
# blueLine = canvas.create_line(0,0,500,500,fill="blue",width=5)
# redLine = canvas.create_line(0,500,500,0,fill="red",width=5)
# canvas.create_rectangle(50,50,250,250,fill="purple")
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points,fill="yellow",outline="black",width=3)
# canvas.create_arc(0,0,500,500,style=PIESLICE,start=130,extent=180)
# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
# canvas.create_oval(190,190,310,310,fill="white",width=10)
#
# canvas.pack()
#
# window.mainloop()

# -------------------Key event---------------------------------------
#
# from tkinter import *
# def doSomething(event):
#     # print("You pressed: " + event.keysym)
#     label.config(text=event.keysym)
#
# window = Tk()
# window.bind("<Key>",doSomething)
#
# label = Label(window,font=("Helvetica",100))
# label.pack()
#
# window.mainloop()


# --------------------Mouse events-------------------------------

# from tkinter import *
# def doSomething(event):
#     print("Mouse cordinates: "+str(event.x)+","+str(event.y))
#
# window = Tk()
#
# # window.bind("<Button-1>",doSomething)
# # window.bind("<Button-2>",doSomething)
# # window.bind("<ButtonRelease>",doSomething)
# # window.bind("<Enter>",doSomething)
# # window.bind("<Leave>",doSomething)
# window.bind("<Motion>",doSomething)
#
# window.mainloop()

# --------------------widget----------------------------
#
# from tkinter import *
#
# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y
#
# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)
#
#
#
# window = Tk()
#
# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)
#
# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)
#
# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)
#
# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)
#
# window.mainloop()

# ---------------------------moveing image-------------------------------

# from tkinter import *
#
# def move_up(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()-10)
# def move_down(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()+10)
# def move_left(event):
#     label.place(x=label.winfo_x()-10,y=label.winfo_y())
# def move_right(event):
#     label.place(x=label.winfo_x()+10,y=label.winfo_y())
#
# window = Tk()
# window.geometry("500x500")
#
# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
#
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)
#
# myimage = PhotoImage(file='pizza.png')
# label = Label(window,image=myimage,bg="red")
# label.place(x=0,y=0)
#
#
# window.mainloop()
# -------------------------------
#
#
# from tkinter import *
#
# def move_up(event):
#     canvas.move(myimage,0,-10)
# def move_down(event):
#     canvas.move(myimage, 0, 10)
# def move_left(event):
#     canvas.move(myimage, -10, 0)
# def move_right(event):
#     canvas.move(myimage, 10, 0)
#
#
# window = Tk()
#
# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
#
#
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)
#
#
# canvas = Canvas(window,width=500,height=500)
# canvas.pack()
#
# photoimage = PhotoImage(file='pizza.png')
# myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)
#
#
# window.mainloop()

# ---------------------Animation----------------------

# from tkinter import *
# import time
#
# WIDTH = 500
# HEIGHT = 500
# xVelocity =3
# yVelocity =2
#
# window = Tk()
#
# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()
#
# background_photo = PhotoImage(file='pizza.png')
# background = canvas.create_image(0,0,image=photo_image,anchor=NW)
#
# photo_image = PhotoImage(file='pizza.png')
# my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)
#
# image_width = photo_image.width()
# image_height = photo_image.height()
#
# while True:
#     coordinates = canvas.coords(my_image)
#     print(coordinates)
#     if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#         xVelocity = -xVelocity
#     if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
#         yVelocity = -yVelocity
#     canvas.move(my_image,xVelocity,yVelocity)
#     window.update()
#     time.sleep(0.01)
#
#
#
#
# window.mainloop()

# -----------------------multiple animation-------------------------------
#
# from tkinter import *
# from Ball import *
#
# import time
#
# window = Tk()
# WIDTH = 500
# HEIGHT = 500
#
# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()
#
# volley_ball = Ball(canvas,0,0,100,5,2,"white")
# tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
# basket_ball = Ball(canvas,0,0,125,8,7,"orange")
#
# while True:
#     volley_ball.move()
#     tennis_ball.move()
#     basket_ball.move()
#     window.update()
#     time.sleep(0.01)
#
#
# window.mainloop()

# --------------Clock GUI----------------------------------
#
# from tkinter import *
# from time import *
#
# def update():
#     time_string = strftime("%I : %M : %S %p")
#     time_label.config(text=time_string)
#
#     day_string = strftime("%A")
#     day_label.config(text=day_string)
#
#     date_string = strftime("%B %d, %Y")
#     date_label.config(text=date_string)
#
#     window.after(1000,update)
#
# window = Tk()
#
# time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()
#
# day_label = Label(window,font=("Ink Free",25))
# day_label.pack()
#
# date_label = Label(window,font=("Ink Free",30))
# date_label.pack()
#
# update()
#
# window.mainloop()

# --------------------email-----------------------------------

# import smtplib
#
#
# sender = "sender@gmail.com"
# receiver = "receiver@gmail.com"
# password = "password123"
# subject = "Python email test"
# body = "I wrote an email! :D"
#
#
# # header
# message = f"""From: Snoop Dogg{sender}
# To: Nicholas Cage{receiver}
# Subject: {subject}\n
# {body}
# """
#
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
#
# try:
#     server.login(sender,password)
#     print("Logged in...")
#     server.sendmail(sender, receiver, message)
#     print("Email has been sent!")
#
# except smtplib.SMTPAuthenticationError:
#     print("unable to sign in")

# -----------------------run python with cmd----------------------------

# print("Hellow World!")
# name = input("What is your name?: ")
# print("Hello "+name)

# ---------------------------Python pip----------------------------------

# -------------------------py convert to exe--------------------------------------------
# 0. pip install pyinstaller
# 1. cd to directory that contains your .py file
#
# 2. pyinstaller -F -w -i icon.ico clock.py
#
#   -F   (all in 1 file)
#   -w   (removes terminal window)
#   -i icon.ico  (adds custom icon to .exe)
#   clock.py  (name of your main python file)
#
# 3. exe is located in the dist folder

# ----------------------Calculiator program---------------------------------
#
# from tkinter import *
#
# def button_press(num):
#
#     global equation_text
#
#     equation_text = equation_text + str(num)
#
#     equation_label.set(equation_text)
#
# def equals():
#
#     global equation_text
#
#     try:
#
#         total = str(eval(equation_text))
#
#         equation_label.set(total)
#
#         equation_text = total
#
#     except SyntaxError:
#
#         equation_label.set("syntax error")
#
#         equation_text = ""
#
#     except ZeroDivisionError:
#
#         equation_label.set("arithmetic error")
#
#         equation_text = ""
#
# def clear():
#
#     global equation_text
#
#     equation_label.set("")
#
#     equation_text = ""
#
#
# window = Tk()
# window.title("Calculator program")
# window.geometry("500x600")
#
# equation_text = ""
#
# equation_label = StringVar()
#
# label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
# label.pack()
#
# frame = Frame(window)
# frame.pack()
#
# button1 = Button(frame, text=1, height=4, width=9, font=35,
#                  command=lambda: button_press(1))
# button1.grid(row=0, column=0)
#
# button2 = Button(frame, text=2, height=4, width=9, font=35,
#                  command=lambda: button_press(2))
# button2.grid(row=0, column=1)
#
# button3 = Button(frame, text=3, height=4, width=9, font=35,
#                  command=lambda: button_press(3))
# button3.grid(row=0, column=2)
#
# button4 = Button(frame, text=4, height=4, width=9, font=35,
#                  command=lambda: button_press(4))
# button4.grid(row=1, column=0)
#
# button5 = Button(frame, text=5, height=4, width=9, font=35,
#                  command=lambda: button_press(5))
# button5.grid(row=1, column=1)
#
# button6 = Button(frame, text=6, height=4, width=9, font=35,
#                  command=lambda: button_press(6))
# button6.grid(row=1, column=2)
#
# button7 = Button(frame, text=7, height=4, width=9, font=35,
#                  command=lambda: button_press(7))
# button7.grid(row=2, column=0)
#
# button8 = Button(frame, text=8, height=4, width=9, font=35,
#                  command=lambda: button_press(8))
# button8.grid(row=2, column=1)
#
# button9 = Button(frame, text=9, height=4, width=9, font=35,
#                  command=lambda: button_press(9))
# button9.grid(row=2, column=2)
#
# button0 = Button(frame, text=0, height=4, width=9, font=35,
#                  command=lambda: button_press(0))
# button0.grid(row=3, column=0)
#
# plus = Button(frame, text='+', height=4, width=9, font=35,
#                  command=lambda: button_press('+'))
# plus.grid(row=0, column=3)
#
# minus = Button(frame, text='-', height=4, width=9, font=35,
#                  command=lambda: button_press('-'))
# minus.grid(row=1, column=3)
#
# multiply = Button(frame, text='*', height=4, width=9, font=35,
#                  command=lambda: button_press('*'))
# multiply.grid(row=2, column=3)
#
# divide = Button(frame, text='/', height=4, width=9, font=35,
#                  command=lambda: button_press('/'))
# divide.grid(row=3, column=3)
#
# equal = Button(frame, text='=', height=4, width=9, font=35,
#                  command=equals)
# equal.grid(row=3, column=2)
#
# decimal = Button(frame, text='.', height=4, width=9, font=35,
#                  command=lambda: button_press('.'))
# decimal.grid(row=3, column=1)
#
# clear = Button(window, text='clear', height=4, width=12, font=35,
#                  command=clear)
# clear.pack()
#
# window.mainloop()

# --------------------Text editor-------------------------------
#
# import os
# from tkinter import *
# from tkinter import filedialog, colorchooser, font
# from tkinter.messagebox import *
# from tkinter.filedialog import *
#
# def change_color():
#     color = colorchooser.askcolor(title="pick a color...or else")
#     text_area.config(fg=color[1])
#
# def change_font(*args):
#     text_area.config(font=(font_name.get(), size_box.get()))
#
# def new_file():
#     window.title("Untitled")
#     text_area.delete(1.0, END)
#
# def open_file():
#     file = askopenfilename(defaultextension=".txt",
#                            file=[("All file", "*.*"),
#                                 ("Text Documents", "*.txe")])
#     try:
#         window.title(os.path.basename(file))
#         text_area.delete(1.0, END)
#
#         file = open(file, "r")
#
#         text_area.insert(1.0, file.read())
#
#     except Exception:
#         print("couldn't read file")
#
#     finally:
#         file.close()
#
# def save_file():
#     file = filedialog.asksaveasfilename(initialfile='unitiled.txt',
#                                         defaultextension=".txt",
#                                         filetypes=[("All Files", "*.*"),
#                                                    ("Text Documents", "*.txt")])
#     if file is None:
#         return
#
#     else:
#         try:
#             window.title(os.path.basename(file))
#             file = open(file, "w")
#
#             file.write(text_area.get(1.0, END))
#
#         except Exception:
#             print("couldn't save file")
#
# def cut():
#     text_area.event_generate("<<Cut>>")
#
# def copy():
#     text_area.event_generate("<<Copy>>")
#
# def paste():
#     text_area.event_generate("<<Paste>>")
#
# def about():
#     showinfo("About this program", "This is a program written by youu !!!")
#
# def quit():
#     window.destroy()
#
# window = Tk()
#
# window.title("Text editor program")
# file = None
#
# window_width = 500
# window_height = 500
#
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
#
# x = int((screen_width/2)-(window_width/2))
# y = int((screen_height/2)-(window_height/2))
#
# window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
#
# font_name = StringVar(window)
# font_name.set("Arial")
#
# font_size = StringVar(window)
# font_size.set("25")
#
# text_area = Text(window, font=(font_name.get(), font_size.get()))
# scroll_bar = Scrollbar(text_area)
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)
# text_area.grid(sticky=N + E + S + W)
#
# scroll_bar.pack(side=RIGHT, fill=Y)
# text_area.config(yscrollcommand=scroll_bar.set)
#
#
# frame = Frame(window)
# frame.grid()
#
#
#
# color_button = Button(frame, text="color", command=change_color)
# color_button.grid(row=0, column=0)
#
# font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
# font_box.grid(row=0, column=1)
#
# size_box = Spinbox(frame, font_=1, to=100, textvariable=font_size, command=change_font)
# size_box.grid(row=0, column=2)
#
# menu_bar = Menu(window)
# window.config(menu=menu_bar)
#
# file_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New", command=new_file)
# file_menu.add_command(label="Open", command=open_file)
# file_menu.add_command(label="Save", command=save_file)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=quit)
#
# edit_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Cut", command=cut)
# edit_menu.add_command(label="Coopy", command=copy)
# edit_menu.add_command(label="Paste", command=paste)
#
#
# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Help", menu=help_menu)
# help_menu.add_command(label="About", command=about)
#
# window.mainloop()


# ---------------------------Game Tic-Tac-Toe---------------------------------
#
# from tkinter import *
# import random
#
# def next_turn(row, column):
#     global player
#     if buttons[row][column]['text'] == "" and check_winner() is False:
#
#         if player == players[0]:
#             buttons[row][column]['text'] = player
#
#             if check_winner() is False:
#                 player = players[1]
#                 label.config(text=(players[1]+" turn"))
#
#             elif check_winner() is True:
#                 label.config(text=(players[0]+" wins"))
#
#             elif check_winner() == "Tie":
#                 label.config(text=("Tie!"))
#
#         else:
#
#             buttons[row][column]['text'] = player
#
#             if check_winner() is False:
#                 player = players[0]
#                 label.config(text=(players[0]+" turn"))
#
#             elif check_winner() is True:
#                 label.config(text=(players[1]+" wins"))
#
#             elif check_winner() == "Tie":
#                 label.config(text=("Tie!"))
#
# def check_winner():
#     for row in range(3):
#         if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
#             buttons[row][0].config(bg="green")
#             buttons[row][1].config(bg="green")
#             buttons[row][2].config(bg="green")
#             return True
#
#     for column in range(3):
#         if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
#             buttons[0][column].config(bg="green")
#             buttons[1][column].config(bg="green")
#             buttons[2][column].config(bg="green")
#             return True
#
#     if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
#         buttons[0][0].config(bg="green")
#         buttons[1][1].config(bg="green")
#         buttons[2][2].config(bg="green")
#         return True
#
#     elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
#         buttons[0][2].config(bg="green")
#         buttons[1][1].config(bg="green")
#         buttons[2][0].config(bg="green")
#         return True
#
#     elif empty_spaces() is False:
#
#         for row in range(3):
#             for column in range(3):
#                 buttons[row][column].config(bg="yellow")
#         return "Tie"
#
#     else:
#         return False
#
#
# def empty_spaces():
#     spaces = 9
#
#     for row in range(3):
#         for column in range(3):
#             if buttons [row][column]['text'] != "":
#                 spaces -=1
#
#     if spaces == 0:
#         return False
#     else:
#         return True
#
# def new_game():
#
#     global player
#
#     player = random.choice(players)
#
#     label.config(text=player+" turn")
#
#     for row in range(3):
#         for column in range(3):
#             buttons[row][column].config(text="",bg="#F0F0F0")
#
# window = Tk()
# window.title("Tic-Tac-Toe")
# players = ["x","o"]
# player = random.choice(players)
# buttons = [[0,0,0],
#            [0,0,0],
#            [0,0,0]]
#
# label = Label(text= player + " turn", font=('consolas',40))
# label.pack(side="top")
#
# reset_button = Button(text="restart", font=('consolas',20), command=new_game)
# reset_button.pack()
#
# frame = Frame(window)
# frame.pack()
#
# for row in range(3):
#     for column in range(3):
#         buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
#                                       command= lambda row=row, column=column: next_turn(row,column))
#         buttons[row][column].grid(row=row,column=column)
#
# window.mainloop()

# -------------------------Snake game---------------------------------


from tkinter import *

import random

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 200
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])


        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")



def next_turn(snake, food):

    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:

        return True
    elif y < 0 or y >= GAME_HEIGHT:

        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:

            return True

    return False

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")



window = Tk()

window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()

next_turn(snake, food)
window.mainloop()