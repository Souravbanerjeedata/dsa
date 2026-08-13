# In this file: Binary search || Logarithms || Running time || Big O notation || The traveling salesperson || Linked List || Arrays || Selection sort (chapter 1 - 4)

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

# Linked List & Arrays

# In Python a basic linked list looks like this:
class Node:
 def __init__(self, value):
    self.value = value
    self.next = None
# Build a short linked list: 10 → 20 → 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Suppose you’re building an app to keep track of your finances. 
 
# Every day, you write down everything you spent money on. At the 
# end of the month, you review your expenses and sum up how much 
# you spent. So you have lots of inserts and a few reads. Should you 
# use an array or a list?
# Answer: Linked Lists are better for insertion or deletion.

# Exercise:
# 2.2 Suppose you’re building an app for restaurants to take customer orders. Your app needs to store a list of orders. Servers keep adding orders to this list, and chefs take orders off the list and make them. It’s an order queue: servers add orders to the back of the queue, and the chef takes the first order off the queue and cooks it. Would you use an array or a linked list to implement this queue? (Hint: Linked lists are good for inserts/deletes, and arrays are good for random access. Which one are you going to be doing here?) 

# Answer: Linked list.
# You’re only doing inserts at the back (enqueue) and deletes from the front (dequeue). You never need random access to an arbitrary order in the middle. Linked list (especially with a tail pointer): both enqueue and dequeue are $  O(1)  $. Just update a couple of pointers. Array: enqueue at the end is fine ($  O(1)  $ amortized), but dequeue from the front forces you to shift every remaining element one position left, which is $  O(n)  $. That gets expensive as the queue grows. So a linked list is the natural fit for a classic queue. (In practice many languages also offer circular buffers / ring buffers on arrays that can make both ends efficient, but the book’s point is the basic arrays-vs-linked-lists trade-off.)

#  2.3  Let’s run a thought experiment. Suppose Facebook keeps a list of usernames. When someone tries to log in to Facebook, a search is done for their username. If their name is in the list of usernames, they can log in. People log in to Facebook pretty often, so there are a lot of searches through this list of usernames. Suppose Facebook uses binary search to search the list. Binary search needs random access—you need to be able to get to the middle of the list of usernames instantly. Knowing this, would you implement the list as an array or a linked list? 

# Answer: Array.
# Binary search depends on being able to jump straight to the middle element (and then the middle of the remaining half, and so on). That requires random access in $  O(1)  $ time. 
# Array: element at index $  i  $ is available instantly.
# Linked list: reaching the middle means walking node-by-node from the head, which is $  O(n)  $. Doing that repeatedly would destroy the $  O(\log n)  $ advantage of binary search and make it no better than a linear scan.
# So for a frequently searched, sorted list of usernames where binary search is used, an array (or a structure built on top of random-access storage) is the right choice.

# 2.4 People sign up for Facebook pretty often, too. Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? In particular, suppose you’re using binary search to search for logins. What happens when you add new users to an array? 

# Answer: Downsides of using an array for inserts (especially while keeping binary search working):

# Inserts are slow ($  O(n)  $) To keep the list sorted (required for binary search), a new username can’t just be appended at the end. You must:
# Find the correct sorted position, and Shift every element after that position one slot to the right to make room. Shifting is linear in the size of the array, so frequent sign-ups become expensive. Resizing is also costly Arrays have fixed capacity. When the array fills up you have to:
# Allocate a larger array, Copy every existing username into it, which is another $  O(n)  $ operation.

# What happens when you add new users while still wanting binary search?
# Every insertion forces you to maintain sorted order. That means the cheap $  O(1)  $ append you get with an unsorted array disappears; inserts become $  O(n)  $ shifts (plus occasional full copies on resize). The more users sign up, the more expensive those insertions get, even though searches remain fast ($  O(\log n)  $). This is the classic trade-off the book is highlighting: arrays give you fast random access (great for binary search) but slow inserts/deletes; linked lists give you fast inserts/deletes but slow random access.

# Selection Sort

def findSmallest(arr): 
  smallest = arr[0]    
  smallest_index = 0    
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

# Now you can use this function to write selection sort:
def selectionSort(arr):
    # Sorts an array
  newArr = []
  copiedArr = list(arr) #copy array before mutating
  for i in range(len(copiedArr)):
      smallest = findSmallest(copiedArr)  
      newArr.append(copiedArr.pop(smallest))
  return newArr

# Recap
# •  Your computer’s memory is like a giant set of drawers.
# •  When you want to store multiple elements, use an array or a linked list.
# •  With an array, all your elements are stored right next to each other.
# •  With a linked list, elements are strewn all over, and one element stores the address of the next one.
# •  Arrays allow fast reads.
# •  Linked lists allow fast inserts and deletes.