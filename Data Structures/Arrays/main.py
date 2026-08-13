# trying to create an array structure manually

class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data.get(index)   # returns None if missing

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        if self.length == 0:
            return None

        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        if index < 0 or index >= self.length:
            return None

        item = self.data[index]
        self._shift_items(index)
        return item

    def _shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


# Create a function that reverses a string
def reverse(str):
    if not str or len(str) < 2 or not isinstance(str, str):
        return str          # or return ""

    backwards = []
    for i in range(len(str) - 1, -1, -1):
        backwards.append(str[i])
    
    return "".join(backwards)

# Cleaner / more Pythonic alternatives (for reference)
# 1. Slicing (most common in real code)
def reverse1(str):
    return str[::-1]

# 2. Using reversed()
def reverse2(str):
    return "".join(reversed(str))


# Create one sorted list by merging two sorted list

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# print(merge_sorted_arrays([0, 3, 5, 7, 31], [4, 6, 30]))