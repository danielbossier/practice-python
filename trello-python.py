# Write a function that returns the sum of all numbers in a given array.

# Input: [1, 2, 3, 4]
# Output: 10

# def _sum(array):
#     output = 0
#     for n in array:
#         output += n
#     print(output)
#     return output

# _sum([1, 2, 3, 4])

# Given an array of numbers, write a function that returns a new array that contains all numbers from the original array that are less than 100.

# Input: [99, 101, 88, 4, 2000, 50]
# Output: [99, 88, 4, 50]

# def less_than_100(arr):
#     output = []
#     for i in arr:
#         if i < 100:
#             output.append(i)
#     print(output)

# less_than_100([99, 101, 88, 4, 2000, 50])

# def less_than_100(arr):
#     i = 0
#     output = []
#     while i < len(arr):
#         if arr[i] < 100:
#             output.append(arr[i])
#         i += 1
#     print(output)

# less_than_100([99, 101, 88, 4, 2000, 50])


# Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.

# Input: [4, 2, 5, 99, -4]
# Output: [8, 4, 10, 198, -8]

# def _double(arr):
#     output = []
#     for i in arr:
#         i = i * 2
#         output.append(i)
#     print(output)

# _double([4, 2, 5, 99, -4])

# Write a function that returns the greatest value from an array of numbers.

# Input: [5, 17, -4, 20, 12]
# Output: 20

# def _greatest(arr):
#     output = 0
#     for i in arr:
#         if i > output:
#             output = i
#     print(output)

# _greatest([5, 17, -4, 20, 12])

# Write a function that accepts an array of numbers and returns the product of all the numbers.

# Input: [1, 2, 3, 4]
# Output: 24

# Given an array, write a function that returns an array that contains the original array’s values in reverse.

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
