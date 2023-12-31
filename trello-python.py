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

# def _mesh(arr1, arr2):
#     i1 = 0
#     i2 = 0
#     output = []
#     while i1 < len(arr1):
#         while i2 < len(arr2):
#             output.append(arr1[i1] + arr2[i2])
#             i2 += 1
#         i1 += 1
#         i2 = 0
#     return output

# print(_mesh(["a", "b", "c"], ["d", "e", "f", "g"]))

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# def _multiples(n):
#     i = 0
#     threesAndFives = []
#     while i < n:
#         if i % 3 == 0 or i % 5 == 0:
#             threesAndFives.append(i)
#         i += 1
#     return sum(threesAndFives)

# print(_multiples(1000))

# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

# def _mesh2(arr):
#     i1 = 0
#     output = []
#     while i1 < len(arr):
#         i2 = 0
#         while i2 < len(arr):
#             if arr[i1] != arr[i2]:
#                 output.append(arr[i1] + arr[i2])
#             i2 += 1
#         i1 += 1
#     return output

# print (_mesh2(["a", "b", "c", "d"]))

# Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.

# Input: “abcdefghhijkkloooop”
# Output: “h”

# def dupe(string):
#     i = 0
#     while i < (len(string) - 1):
#         if string[i] == string[i+1]:
#             return string[i]
#         i += 1
#     print("no dupes")

# print(dupe("abcdefghijklop"))

# Given a string, find the most commonly occurring letter.

# Input: “peter piper picked a peck of pickled peppers”
# Output: “p”

# def most_frequent(string):
#     i = 0
#     letter_count = {}
#     most_frequent_letter = ""
#     most_frequent_count = 0

#     while i < len(string):
#         if string[i] in letter_count:
#             letter_count[string[i]] += 1
#         else:
#             letter_count[string[i]] = 1
        
#         if letter_count[string[i]] > most_frequent_count:
#             most_frequent_count = letter_count[string[i]]
#             most_frequent_letter = string[i]
#         i += 1
#     return most_frequent_letter

# print(most_frequent("peter piper picked a peck of pickled peppers"))

# Given an array of strings, return a hash that provides of a count of how many times each string occurs.

# Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

# Output: {"Dewey" => 6, "Truman" => 5}

# Explanation: "Dewey" occurs 6 times in the array, while "Truman" occurs 5 times.

# def votes(string):
#     i = 0
#     output = {}
#     while i < len(string):
#         if string[i] in output:
#             output[string[i]] += 1
#         else:
#             output[string[i]] = 1
#         i += 1
#     return output


# print(votes(["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]))

# Given a hash, where the keys are strings representing food items, and the values are numbers representing the price of each food, return the amount someone would pay if they'd order one of each food from the entire menu.

# Input: {"hot dog" => 2, "hamburger" => 3, "steak sandwich" => 5, "fries" => 1, "cole slaw" => 1, "soda" => 2}

# Output: 14

# Explanation: If someone would order one of everything on the menu, they'd pay a total of 14 (the sum of all the hash's values).

# def menu_total(menu):
#     output = 0
#     for _item, price in menu.items():
#         output += price
#     return output

# print(menu_total({ "hot dog": 2, "hamburger": 3, "steak sandwich": 5, "fries": 1, "cole slaw": 1, "soda": 2 }))

# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: "silent", "listen"
# Output: true

# Input: "frog", "bear"
# Output: false

# def is_anagram(string1, string2):
#     letter_count1 = {}
#     letter_count2 = {}
#     i = 0
#     while i < len(string1):
#         if string1[i] in letter_count1:
#             letter_count1[string1[1]] += 1
#         else:
#             letter_count1[string1[1]] = 1
#         i += 1
#     i = 0
#     while i < len(string2):
#         if string2[i] in letter_count2:
#             letter_count2[string2[1]] += 1
#         else:
#             letter_count2[string2[1]] = 1
#         i += 1
#     if letter_count1 == letter_count2:
#         return True
#     return False

# print(is_anagram("frog", "bear"))

# Write a function that returns the reverse of a given string.

# Input: “abcde”
# Output: “edcba”

# def reverse(string):
#     i = -1
#     reverse_string = ""
#     while i > -(len(string)+ 1):
#         reverse_string += string[i]
#         i -= 1
#     return reverse_string

# print(reverse("abcde"))

# Given a string, write a function that returns true if the “$” character is contained within the string or false if it is not.

# Input: “i hate $ but i love money i know i know im crazy”
# Output: true

# Input: “abcdefghijklmnopqrstuvwxyz”
# Output: false

# def is_money(string):
#     for i in string:
#         if i == "$":
#             return True
#     return False
# print(is_money("i hate but i love money i know i know im crazy"))

# def is_money(string):
#     i = 0
#     while i < len(string):
#         if string[i] == "$":
#             return True
#         i += 1
#     return False

# print(is_money("abcdefghijklmnopqrstuvwxyz"))

# Given a string, write a function that returns a copy of the original string that has every other character capitalized. (Capitalization should begin with the second character.)

# Input: “hello, how are your porcupines today?”
# Output: “hElLo, HoW ArE YoUr pOrCuPiNeS ToDaY?”

# def cap_every_other(string):
#     result = ""
#     should_capitalize = True

#     for i, char in enumerate(string):
#         if char.isalpha():
#             if should_capitalize:
#                 result += char.upper()
#             else:
#                 result += char.lower()
#             should_capitalize = not should_capitalize
#         else:
#             result += char
#     return result

# print(cap_every_other("hello, how are your porcupines today?"))

# Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.

# Input: “abcdefghhijkkloooop”
# Output: “h”

# def first_dupe(string):
#     i = 0
#     dupe = "no dupes"
#     while i < len(string):
#         if string[i] == string[i+1]:
#             dupe = string[i]
#             return dupe
#         i += 1
#     return dupe
# print(first_dupe("abcdefghijkloooop"))

# Given a string, write a function that returns true if it is a palindrome, and false if it is not. (A palindrome is a word that reads the same both forward and backward.)

# Input: “racecar”
# Output: true

# Input: “baloney”
# Output: false

# def is_palindrome(string):
#     i1 = 0
#     i2 = -1
#     while i1 < len(string):
#         if string[i1] != string[i2]:
#             return False
#         i1 += 1
#         i2 -= 1
#     return True
# print(is_palindrome("oaao"))

# Given two strings of equal length, write a function that returns the number of characters that are different between the two strings.

# Input: "ABCDEFG", "ABCXEOG"
# Output: 2

# Explanation: While the A, B, C, E, and G are in the same place for both strings, they have different characters in the other spaces. Since there are 2 such spaces that are different (the D and F in the first string), we return 2.

# Input: "ABCDEFG", "ABCDEFG",
# Output: 0

# def hamming(string1, string2):
#     output = 0
#     i = 0
#     while i < len(string1):
#         if string1[i] != string2[i]:
#             output += 1
#         i += 1
#     return output

# print(hamming("ABCDEFG", "ABCXEOG"))

# def hamming(string1, string2):
#     output = 0
#     min_length = min(len(string1), len(string2))

#     for i in range(min_length):
#         if string1[i] != string2[i]:
#             output += 1
#     return output

# print(hamming("ABCDEFG", "ABCXEOG"))

# Given a string of words, write a function that returns a new string that contains the words in reverse order.

# Input: "popcorn is so cool isn’t it yeah i thought so"
# Output: "so thought i yeah it isn’t cool so is popcorn"

# def reverse_words(string):
#     output = ""
#     current_word = ""
#     for i in string:
#         if i != " ":
#             current_word += i
#         else:
#             output = current_word + " " + output
#             current_word = ""
#     output = current_word + " " + output
#     return output

# print(reverse_words("popcorn is so cool isn't it yeah i thought so"))

# Given a string of words, write a function that returns a new string that contains the words in reverse order.

# Input: "popcorn is so cool isn’t it yeah i thought so"
# Output: "so thought i yeah it isn’t cool so is popcorn"

# def reverse_words(string):
#     current_word = ""
#     output = ""
#     for i in string:
#         if i != " ":
#             current_word += i
#         else:
#             output = current_word + " " + output
#             current_word = ""        
#     return output

# print(reverse_words("popcorn is so cool isn't it yeah thought I"))

# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: "silent", "listen"
# Output: true

# Input: "frog", "bear"
# Output: false

# def is_anagram(string1, string2):
#     hash1 = {}
#     hash2 = {}
#     for i in string1:
#         if i in hash1:
#             hash1[i] += 1
#         else:
#             hash1[i] = 1

#     for i in string2:
#         if i in hash2:
#             hash2[i] += 1
#         else:
#             hash2[i] = 1
    
#     if hash1 == hash2:
#         return True
#     return False


# print(is_anagram("silent", "listen"))

# Given an array of strings, return a hash that provides of a count of how many times each string occurs.

# Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

# Output: {"Dewey" => 6, "Truman" => 5}

# Explanation: "Dewey" occurs 6 times in the array, while "Truman" occurs 5 times.

# def votes(array):
#     output = {}
#     for i in array:
#         if i in output:
#             output[i] += 1
#         else:
#             output[i] = 1
    
#     return output

# print(votes(["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]))

# Given a string of words, write a function that returns a new string that contains the words in reverse order.

# Input: "popcorn is so cool isn't it yeah i thought so"
# Output: "so thought i yeah it isn’t cool so is popcorn"

# def reverse_words(string):
#     output = ""
#     current_word = ""
#     for i in string:
#         if i != " ":
#             current_word += i
#         else:
#             output = current_word + " " + output
#             current_word = ""
#     return output

# print(reverse_words("popcorn is so cool isn't it yeah i thought so"))


# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: "silent", "listen"
# Output: true

# Input: "frog", "bear"
# Output: false

# def is_anagram(string1, string2):
#     word_count1 = {}
#     for i in string1:
#         if string1 in word_count1:
#             word_count1[i] += 1
#         else:
#             word_count1[i] = 1
    
#     word_count2 = {}
#     for i in string2:
#         if string2 in word_count2:
#             word_count2[i] += 1
#         else:
#             word_count2[i] = 1
    
#     if word_count1 == word_count2:
#         return True
#     return False  

# print(is_anagram("frog", "bear"))

# You are given two parameters, an array and a number. Return a hash whose keys are each of the values from the array parameter, and whose values are the number parameter.

# Input:

# First argument: ["a", "e", "i", "o", "u"]
# Second argument: 1

# Output:

# {
# 'a' => 1,
# 'e' => 1,
# 'i' => 1,
# 'o' => 1,
# 'u' => 1
# }

# def transform(array, number):
#     output = {}
#     for i in array:
#         output[i] = number
#     return output

# print(transform(["a", "e", "i", "o", "u"], 1))

# Given a hash, create a new hash that has the keys and values switched.

# Input: {"a" => 1, "b" => 2, "c" => 3}
# Output: {1 => "a", 2 => "b", 3 => "c"}

# def flip_hash(objects):
#     output = {}
#     for key, value in objects.items():
#         output[value] = key
#     return output


# print(flip_hash({"a" : 1, "b" : 2, "c" : 3}))

# You are given a hash in format #A, and you are to return the same data as a hash using format #B, as specified below:

# Input:

# {
# 1 => ["A", "E", "I", "O", "U"]
# }

# Output:

# {
# 'a' => 1,
# 'e' => 1,
# 'i' => 1,
# 'o' => 1,
# 'u' => 1
# }

# def alter_hash(input_hash):
#     output = {}
#     for key, values in input_hash.items():
#         for value in values:
#             output[value.lower()] = key
#     return output

# print(alter_hash({1 : ["A", "E", "I", "O", "U"]}))

# Given a hash, create a new hash that has the keys and values switched.

# Input: {"a" => 1, "b" => 2, "c" => 3}
# Output: {1 => "a", 2 => "b", 3 => "c"}

# def new_hash(input_hash):
#     flip_hash = {}
    
#     for key, value in input_hash.items():
#         flip_hash[value] = key
    
#     return flip_hash

# print(new_hash({"a" : 1, "b" : 2, "c" : 3}))

# You are given a hash in format #A, and you are to return the same data as a hash using format #B, as specified below:

# Input:

# {
# 1 => ["A", "E", "I", "O", "U"]
# }

# Output:

# {
# 'a' => 1,
# 'e' => 1,
# 'i' => 1,
# 'o' => 1,
# 'u' => 1
# }

# def re_format(input_hash):
#     output_hash = {}

#     for key, values in input_hash.items():
#         for value in values:
#             output_hash[value] = key
        
#     return output_hash

# print(re_format({1 : ["A", "E", "I", "O", "U"]}))

# Given a list of books provided in this format:

# [
# {title: "The Lord of the Rings", author: "J. R. R. Tolkien", year: 1954 },
# {title: "To Kill a Mockingbird", author: "Harper Lee", year: 1960 },
# {title: "1984", author: "George Orwell", year: 1949 },
# {title: "Go Set a Watchman", author: "Harper Lee", year: 2015 },
# {title: "The Hobbit", author: "J. R. R. Tolkien", year: 1937 },
# {title: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 1925 },
# {title: "The Two Towers", author: "J. R. R. Tolkien", year: 1954 }
# ]

# return the data in this new author-centric format:

# { "J. R. R. Tolkien" => [
# {title: "The Lord of the Rings", year: 1954 },
# {title: "The Hobbit", year: 1937 },
# {title: "The Two Towers", year: 1954 }
# ],
# "Harper Lee" => [
# {title: "To Kill a Mockingbird", year: 1960 },
# {title: "Go Set a Watchman", year: 2015 }
# ],
# "George Orwell" => [
# {title: "1984", year: 1949 }
# ],
# "F. Scott Fitzgerald" => [
# {title: "The Great Gatsby", year: 1925 }
# ]
# }

# def authors_hash(input_hash):
#     author_dict = {}

#     for book in input_hash:
#         author = book["author"]
#         book_data = {"title" : book["title"], "year" : book["year"] }

#         if author in author_dict:
#             author_dict[author].append(book_data)
#         else:
#             author_dict[author] = [book_data]

#     return author_dict
    
# books = [
# {"title": "The Lord of the Rings", "author": "J. R. R. Tolkien", "year": 1954 },
# {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960 },
# {"title": "1984", "author": "George Orwell", "year": 1949 },
# {"title": "Go Set a Watchman", "author": "Harper Lee", "year": 2015 },
# {"title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937 },
# {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925 },
# {"title": "The Two Towers", "author": "J. R. R. Tolkien", "year": 1954 }
# ]

# print(authors_hash(books))

# Given an array of numbers, return a new array containing just two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.

# Specifically use nested loops to solve this exercise even though there are other approaches as well.

# Input: [2, 5, 3, 1, 0, 7, 11]
# Output: [3, 7]

# Input: [1, 2, 3, 4, 5]
# Output: false (While 1, 2, 3, and 4 altogether add up to 10, we're seeking just one pair of numbers.)

# def sum_ten(array):
#     output = 0
#     i1 = 0
#     i2 = 1
#     while i1 < len(array):
#         while i2 < len(array):
#             if i1 + i2 == 10:
#                 output = i1 + i2
#                 return output
#             i2 += 1
#         i1 += 1
#         i2 = i1 + 1
#     return False    

# print(sum_ten([1, 2, 3, 4, 5]))

# streamlined alternative:

# def sum_ten(array):
#     output = 0
#     for i1 in range(len(array)):
#         for i2 in range(i1 + 1, len(array)):
#             if i1 + i2 == 10:
#                 output = i1 + i2
#                 return output
#     return False

# print(sum_ten([2, 5, 3, 1, 0, 11]))

# Given a list of books provided in this format:

# [
# {title: "The Lord of the Rings", author: "J. R. R. Tolkien", year: 1954 },
# {title: "To Kill a Mockingbird", author: "Harper Lee", year: 1960 },
# {title: "1984", author: "George Orwell", year: 1949 },
# {title: "Go Set a Watchman", author: "Harper Lee", year: 2015 },
# {title: "The Hobbit", author: "J. R. R. Tolkien", year: 1937 },
# {title: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 1925 },
# {title: "The Two Towers", author: "J. R. R. Tolkien", year: 1954 }
# ]

# return the data in this new author-centric format:

# { "J. R. R. Tolkien" => [
# {title: "The Lord of the Rings", year: 1954 },
# {title: "The Hobbit", year: 1937 },
# {title: "The Two Towers", year: 1954 }
# ],
# "Harper Lee" => [
# {title: "To Kill a Mockingbird", year: 1960 },
# {title: "Go Set a Watchman", year: 2015 }
# ],
# "George Orwell" => [
# {title: "1984", year: 1949 }
# ],
# "F. Scott Fitzgerald" => [
# {title: "The Great Gatsby", year: 1925 }
# ]
# }

# def authors_hash(books_hash):
#     authors_dict = {}

#     for book in books_hash:
#         author = book["author"]
#         book_data = { "title" : book["title"], "year" : book["year"] }

#         if author in authors_dict:
#             authors_dict[author].append(book_data)
#         else:
#             authors_dict[author] = [book_data]
    
#     return authors_dict        

# books = [{"title": "The Lord of the Rings", "author": "J. R. R. Tolkien", "year": 1954 },
# {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960 },
# {"title": "1984", "author": "George Orwell", "year": 1949 },
# {"title": "Go Set a Watchman", "author": "Harper Lee", "year": 2015 },
# {"title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937 },
# {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925 },
# {"title": "The Two Towers", "author": "J. R. R. Tolkien", "year": 1954 }]

# print(authors_hash(books))

# Given a list of books provided in this format:

# [
# {title: "The Lord of the Rings", author: "J. R. R. Tolkien", year: 1954 },
# {title: "To Kill a Mockingbird", author: "Harper Lee", year: 1960 },
# {title: "1984", author: "George Orwell", year: 1949 },
# {title: "Go Set a Watchman", author: "Harper Lee", year: 2015 },
# {title: "The Hobbit", author: "J. R. R. Tolkien", year: 1937 },
# {title: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 1925 },
# {title: "The Two Towers", author: "J. R. R. Tolkien", year: 1954 }
# ]

# def authors_hash(input_data):
#     authors_dict = {}

#     for book in input_data:
#         author = book["author"]
#         book_data = { "title" : book["title"], "year" : book["year"] }

#         if author in authors_dict:
#             authors_dict[author].append(book_data)
#         else:
#             authors_dict[author] = [book_data]

#     return authors_dict

# books = [
# {"title": "The Lord of the Rings", "author": "J. R. R. Tolkien", "year": 1954 },
# {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960 },
# {"title": "1984", "author": "George Orwell", "year": 1949 },
# {"title": "Go Set a Watchman", "author": "Harper Lee", "year": 2015 },
# {"title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937 },
# {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925 },
# {"title": "The Two Towers", "author": "J. R. R. Tolkien", "year": 1954 }
# ]

# print(authors_hash(books))

# Given an array of numbers, return a new array containing just two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.

# Specifically use nested loops to solve this exercise even though there are other approaches as well.

# Input: [2, 5, 3, 1, 0, 7, 11]
# Output: [3, 7]

# Input: [1, 2, 3, 4, 5]
# Output: false (While 1, 2, 3, and 4 altogether add up to 10, we're seeking just one pair of numbers.)

# def sum_ten(arr):
#     output = 0
#     for i1 in range(len(arr)):
#         for i2 in range(i1 + 1, len(arr)):
#             if i1 + i2 == 10:
#                 output = i1 + i2
#                 return output
#     return False

# print(sum_ten([2, 5, 1, 0, 7, 11]))


# a cool method in Python is zip() which allows you to easily combine two arrays together alternating inputs
# this allows you to create dictionaries very easily

# keys = ["a", "b", "c"]
# values = [1, 2, 3]

# data_dict = dict(zip(keys, values))
# print(data_dict)

# bears = ["Britty", "Honey", "Yawny"]
# birth_months = ["May", "September", "August"]

# bear_dict = dict(zip(bears, birth_months))
# print(bear_dict)

# Given an array of strings, return a hash that provides of a count of how many times each string occurs.

# Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

# Output: {"Dewey" => 6, "Truman" => 5}

# def votes(input):
#     output = {}
#     for i in input:
#         if i in output:
#             output[i] += 1
#         else:
#             output[i] = 1
#     return output

# print(votes(["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]))

# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

# def all_combos(array):
#     output = []
#     for i1 in array:
#         for i2 in array:
#             output.append(i1 + i2)
#     return output
# print(all_combos(["a", "b", "c", "d"]))

# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

# def all_combos(array):
#     output = []
#     for i1 in array:
#         for i2 in array:
#             output.append(i1 + i2)
#     return output
# print(all_combos(["a", "b", "c", "d"]))

# Given an array of strings, return a hash that provides of a count of how many times each string occurs.

# Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

# Output: {"Dewey" => 6, "Truman" => 5}

# def count_votes(array):
#     output = {}
#     for i in array:
#         if i in output:
#             output[i] += 1
#         else:
#             output[i] = 1
#     return output

# print(count_votes(["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]))


# Given a hash, create a new hash that has the keys and values switched.

# Input: {"a" => 1, "b" => 2, "c" => 3}
# Output: {1 => "a", 2 => "b", 3 => "c"}

# def flip_hash(og_hash):
#     flipped = {}
#     for key, value in og_hash.items():
#         flipped[value] = key
#     return flipped

# print(flip_hash({"a" : 1, "b" : 2, "c" : 3}))

# Given a string, write a function that returns true if it is a palindrome, and false if it is not. (A palindrome is a word that reads the same both forward and backward.)

# Input: “racecar”
# Output: true

# Input: “baloney”
# Output: false

# def is_palindrome(string):
#     for i in range(len(string) // 2):
#         if string[i] != string[len(string) - i - 1]:
#             return False
#     return True
# print(is_palindrome("racecar"))

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# def multiple(input):
#     sum = 0
#     for i in range(input):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#     return sum

# print(multiple(1000))

# Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.

# Input: [4, 2, 5, 99, -4]
# Output: [8, 4, 10, 198, -8]

# def double(array):
#     output = []
#     for i in array:
#         i = i * 2
#         output.append(i)
#     return output

# print(double([4, 2, 5, 99, -4]))

# Write a function that returns whether a given number is a prime number.
# import math

# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0:
#         return False
    
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
        
# print(is_prime(21))

# Given an array of numbers, return a new array containing just two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.

# Specifically use nested loops to solve this exercise even though there are other approaches as well.

# Input: [2, 5, 3, 1, 0, 7, 11]
# Output: [3, 7]

# Input: [1, 2, 3, 4, 5]
# Output: false (While 1, 2, 3, and 4 altogether add up to 10, we're seeking just one pair of numbers.)

# this function checks all number combonations, including the same index with itself
# def equal_ten(array):
#     output = []
#     for i in array:
#         for i2 in array:
#             if i + i2 == 10:
#                 output.append((i, i2))
#                 return output
#     return False

# print(equal_ten([1, 2, 3, 4, 5]))

# Write a function that prints out every number from 1 to N, with the following exceptions:

# If the number is divisible by 3, print out "FIZZ".
# If the number is divisible by 5, print out "BUZZ".
# If the number is divisible by both 3 and 5, print out "FIZZBUZZ".

# def fizzbuzz(n):
#     i = 1
#     while i <= n:
#         if i % 3 == 0 and i % 5 == 0:
#             print("FIZZBUZZ")
#         elif i % 3 == 0:
#             print("FIZZ")
#         elif i % 5 == 0:
#             print("BUZZ")
#         else:
#             print(i)
#         i += 1


# print(fizzbuzz(30))