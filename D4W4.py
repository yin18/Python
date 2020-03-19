# def hello():
#     print("Hello")
# hello()


# def func(a, b):
#     return a + b
# print("The sum is", func(10,20))

# def func(a=10, b=30):
#     return a + b
# print("The sum is", func(20,40))

# EXERCISE
# def add(a,b):
#     return a+b
# print(add(2,6))
#
# def mult(a,b):
#     return a*b
# print(mult(3,5))
#
# def minus(a,b):
#     return a-b
# print(minus(10,8))
#
# def div(a,b):
#         return a/b
# print(div(3,5))


# CLASS
# class Dog:
#     animal_kind = "canine"
#
#     def bark():
#         return "woof"
# print(Dog.animal_kind)
# print(Dog.bark())


#
# class Fizzbuzz:
#
#     def cal(num):
#         if int(num) % 3 == 0 and int(num) % 5 == 0:
#             print("Fizz")
#         elif int(num) % 3 == 0:
#             print("Fizz")
#         elif int(num) % 5 == 0:
#             print("Buzz")
#         else:
#             print("Incorrect value")
#
#
# print(Fizzbuzz.cal(15))


# class student:
#     student_type = "Trainee"
#     def mes():
#         return "Hi there!"
# print(student.mes())
# print(student.student_type)


# class Dog:
#
#     def __init__(self, name, age, action):
#         self.name = name
#         self.age = age
#         self.action = action
#
#     def bark(self):
#         return "Woof"
#     def eat(self):
#         return ("{} is eating chicken".format(self.name))
#
#
# x = Dog('fido', 8, 'run')
# y = Dog('Dido', 4, 'jump')
# print(x.name)
# print(x.age)
# print(x.action)
# print(x.bark())
# print(x.eat())


# class student:
#     def __init__(self, type, name, course):
#         self.type=type
#         self.name=name
#         self.course=course
#     def enrol(self):
#         return self.type
#     def intro(self):
#         return ("My name is {} and I am enrolled onto the {} course".format(self.name, self.course))
# x = student('Trainee', 'Yin', 'Data')
# print(x.enrol())
# print(x.intro())

name = "Yin"
import random
import time


def get_tof_statements():
    statements = []
    statements.append(["Penguins can fly", "F"])
    statements.append(["Jupiter is the fifth planet from the sun", "T"])
    statements.append(["Sydney is the capital of Australia", "F"])
    return statements


def play_tof_quiz():
    # generate tof statements
    tof_statements = get_tof_statements()
    # shuffle into the statements and randomises
    random.shuffle(tof_statements)
    score = 0
    for x in tof_statements:
        print("True or False: " + x[0])
        guess = input("Enter T or F: ").upper()
        if guess == x[1]:
            print("Correct :)")
            score = score + 1
            time.sleep(1)
        else:
            print("Incorrect :(")
            time.sleep(1)
    if score == len(tof_statements):
        print("You aced it {}! Well done :)".format(name))
        restart = input("Would you like to play again?").lower()
        if restart == "Yes":
            play_tof_quiz()
        else:
            quit()

    else:
        print("Thank you for playing {}, your final score is: {}/".format(name, score) + str(len(tof_statements)))


        restart = input("Would you like to play again?").lower()
        if restart == "Yes":
            play_tof_quiz()
        else:
            quit()


play_tof_quiz()