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

# def _product(arr):
#     output = arr[0]
#     for i in arr:
#         output = output * i
#     print(output)
        
# _product([1, 2, 3, 4])

# Given an array, write a function that returns an array that contains the original array’s values in reverse.

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# def _reverse(arr):
#     output = []
#     for i in reversed(arr):
#         output.append(i)
#     print(output)

# _reverse([1, 2, 3, 4, 5])



# WORKING ON THIS ONE, REVIEW ENUMERATE
# Input:
# [2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2]

# Output:
# [2, 3, 1, 2, 2, 1, 5, 2, 2]

# def _skip_it(arr):
#     output = []
#     output.append(arr[0])
#     i = 0
#     for i in range(0, len(arr)):
#         i += output[-1]
#         output.append(arr[i])
#         print(output)
#     print(output)


# _skip_it([2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2])


# Write a function that returns whether a given number is a prime number.

# def is_prime(n):
#      if n < 2:
#           return False
#      i = 2
#      while i < n and n > 1:
#           if n % i == 0:
#                return False
#           i += 1
#      return True

# print(is_prime(9))

# Given two arrays of strings, return a new string that contains every combination of a string from the first array concatenated with a string from the second array.

# Input: ["a", "b", "c"], ["d", "e", "f", "g"]
# Output: ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]

def _mesh(arr1, arr2):
    i1 = 0
    i2 = 0
    output = []
    while i1 < len(arr1):
        while i2 < len(arr2):
            output.append(arr1[i1] + arr2[i2])
            i2 += 1
        i1 += 1
        i2 = 0
    return output

print(_mesh(["a", "b", "c"], ["d", "e", "f", "g"]))