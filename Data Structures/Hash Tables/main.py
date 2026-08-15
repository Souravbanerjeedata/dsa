# Given an array arr, find the first repeating item in it and return it. If it does not exist, return undefined.

# Brute force
def first_recurring_character(arr):
    seen = set()

    for item in arr:
        if item in seen:
            return item
        seen.add(item)

    return None

# Hash Map
def first_recurring_character2(arr):
    map = {}

    for item in arr:
        if item in map:
            return item
        map[item] = True   # we only care that it exists

    return None