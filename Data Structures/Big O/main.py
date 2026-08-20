# Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Bubble Sort

def bubble_sort(arr):
    unsorted_until_index = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        unsorted_until_index -= 1
    return arr