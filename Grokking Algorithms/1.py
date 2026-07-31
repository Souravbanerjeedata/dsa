# In this file: Binary search || Logarithms || Running time || Big O notation || The traveling salesperson

# Binary Search (page: 3)
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# my_list = [1, 3, 5, 7, 9]

# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))

# EXERCISES
# 1.1   Suppose you have a sorted list of 128 names, and you’re searching 
# through it using binary search. What’s the maximum number of 
# steps it would take?
# 1.2   Suppose you double the size of the list. What’s the maximum 
# number of steps now?

# Problem 1: 7 steps
# Problem 2: 8 steps
# Binary search works on a sorted list by repeatedly checking the middle element and discarding half the remaining elements each time. The worst-case number of steps is $  \log_2 n  $ (base-2 logarithm of the list size).

# For n = 128 = 2^7 , log_2 128 = 7 .
# Doubling the list gives n = 256 = 2^8 , so log_2 256 = 8 .

# EXERCISES
# Give the run time for each of these scenarios in terms of big O.
# 1.3   You have a name, and you want to find the person’s phone number 
# in the phone book. 
# 1.4   You have a phone number, and you want to find the person’s name 
# in the phone book. (Hint: You’ll have to search through the whole 
# book!)
# 1.5   You want to read the numbers of every person in the phone book.
# 1.6   You want to read the numbers of just the As. (This is a tricky one! 
# It involves concepts that are covered more in chapter 4. Read the 
# answer—you may be surprised!)

# Recap
# •  Binary search is a lot faster than simple search as your array gets bigger.
# •  O(log n) is faster than O(n), and it gets a lot faster once the list items you’re searching through grows.
# •  Algorithm speed isn’t measured in seconds.
# •  Algorithm times are measured in terms of growth of an algorithm.
# •  Algorithm times are written in big O notation