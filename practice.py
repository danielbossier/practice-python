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

count = 0
for n in range(1, 10):
    if n % 2 == 0:
        count += 1
        print(n)
print(f"We have {count} even numbers")