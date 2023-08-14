# for n in range(1, 10, 2):
#     print("Attempt", n, n * ".")

# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# for x in range(5):
#     for y in range(3):
#         print(f"({x + 1}, {y + 1})")

# print(type(5))
# print(type(range(5)))

# ranges are iterable
# output = 0
# for x in [1, 2, 3, 4]:
#     output += x
# print(output)

# count = 0
# for n in range(1, 10):
#     if n % 2 == 0:
#         count += 1
#         print(n)
# print(f"We have {count} even numbers")

# name = input("What is your name? ")
# print("Hello " + name)

# first = input("First: ")
# second = input("Second: ")
# result = int(first) * int(second)
# print(result)

# course = 'Python for Beginners'
# print(course.replace('for', '4'))

# x = 3 != 2
# print(x)

# logical operators: and, or, not

# don't need "end" statement for if or while loops/statements

# temperature = 25

# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print("Done")

# Excercise with inputs and conversion of data types

# weight = int(input("Weight: "))
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))
# elif unit.upper() == "L":
#     converted = weight * 0.45
#     print("Weight in Kgs: " + str(converted))

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# lists

# names = ["John", "Bob", "Dan", "Sam", "Mary"]
# names[0] = "Jon"
# print(names[0:3])
# print(names)

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# numbers.insert(0, -1)
# print(numbers)

# len.numbers
# numbers.replace

# ranges
# numbers = range(5, 10) # can also add third input as a step
# for n in numbers:
#     print(n)

# for number in range(5):
#     print(number)