# EXERCISE ODD/EVEN LIST
# list = [10, 111, 24, 56, 78, 75, 65, 80]
# even_list = []
# odd_list = []
#
# for x in list:
#     if x % 2 == 0:
#         even_list.append(x)
#     else:
#         odd_list.append(x)
# print(even_list)
# print(odd_list)


# DICTIONARY
# student_1 = {
#     "name" : "Yin",
#     "stream" : "tech",
#     "completed_lessons": 500,
#     "completed_lesson_name": ["variables", "data_types", "set up"]
# }
# print(student_1["completed_lesson_name"][1])
# student_1["completed_lessons"] = 6
# print(student_1["completed_lessons"])
# student_1["completed_lesson_name"].remove("data_types")
# print(student_1["completed_lesson_name"])


# #SET
# car_parts = {"wheels", "doors", "exhaust"}
# print(car_parts)
# car_parts.add("windows")
# car_parts.discard("doors")
# print(car_parts)

# FROZEN SET
# x = frozenset([1,2,3,4])
# print(type(x))


# film_rating = input("What is the film rating?")
#
# if film_rating == "universal":
#     print("all age groups can watch this film")
# elif film_rating == "pg":
#     print("General viewing, but some scenes may be unsuitable for young children.")
# elif film_rating == "12" or film_rating == "12a":
#     print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
# elif film_rating.lower() == "15":
#     print("No one younger than 15 may see a 15 film in a cinema.")
# elif film_rating.lower() == "18":
#     print("No one younger than 18 may see an 18 film in a cinema.")
# else:
#     print("this is not a correct rating, please use universal, pg, 12, 12a, 15, 18")


# EXERCISE FIZZBUZZ
# x = int(input("Enter your number:"))
# # if x % 3 == 0 and x % 5 == 0:
# #     print("Fizzbuzz")
# # elif x % 3 == 0:
# #     print("Fizz")
# # elif x % 5 == 0:
# #     print("Buzz")
# # else:
# #     print("Sorry")


# EXERCISE FIZZBUZZ
# x = int(input("Enter your number:"))
# x_list = list(range(1, x + 1))
# for x in x_list:
#     if x % 3 == 0 and x % 5 == 0:
#         print("Fizzbuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print("Sorry")


# FOR LOOP
# no = [1, 2, 3, 4]
# fruits = ["apple", "banana", "cherry"]
# for x in no:
#     for y in fruits:
#         print(x, y)


# list_data = [1, 2, 3, 4, 5]
#  emb_lists = [[1, 2, 3], [4, 5, 6]]
#  for data in emb_lists:
#      print(data)
#      for num in data:
#         print(num)


# dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.35"},
#              3: {"name": "Roscoe", "money": "$1.14"}}
# for value in dict_data:
#     print(value)
# for item in dict_data.values():
#     print(item)
# for item in dict_data.values():
#     for emb_values in item.values():
#         print(emb_values)


# WHILE LOOP
#x = 1
# while x < 10:
#     print(f"it's working --> {x}")
#     if x == 4:
#         break
#     x = x + 1


#