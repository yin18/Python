# class Animal():
#     animal_kind = "Canine"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# #ENCAPSULATION
#     def __eat(self):
#         return ("{} says I am eating Chicken".format(self.name))
# #
# #
# class Reptile(Animal):
#
#     def __init__(self, name, age):
#         super().__init__(name,age)
#         self.name=name
#         self.age=age
#     def sleep(self):
#         return ('zzz I am sleeping')
#     def running(self, speed):
#         return ("I am running in {} speed".format(speed))


# rept1 = Reptile('Lizaard', 5)
# rept2 = Reptile('Mossy', 8)
# print(rept2.running(10))

# import time
# class person():
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     def talk(self):
#         age = input("How old are you? ")
#         time.sleep(1)
#         return ("My name is {} {} and I am {} years old".format(self.firstname, self.lastname, age))
#         time.sleep(1)
# p1 = person("Izzy", "Cakes")
# print(p1.talk())
#
#
# class student(person):
#     def __init__(self, firstname, lastname):
#         super().__init__(firstname, lastname)
#     def enjoy(self):
#         hobby = input("Give me a hobby yours: ")
#         print("{} enjoys {}!".format(self.firstname, hobby))
#         time.sleep(1)
#     def chill(self):
#         print("{} likes to chill!".format(self.firstname))
# s1 = student("Yu", "Bi")
# print(s1.talk())
# print(s1.enjoy())
# print(s1.chill())


# #LAMBDA FUNCTION
# def add(num1, num2):
#     return num1 + num2
# addition = lambda num1, num2:num1 + num2
#
# savings = [234, 567, 757, 354]
# bonus = list(map(lambda x: x * 1.1, savings))
# print(bonus)




