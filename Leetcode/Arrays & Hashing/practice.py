from typing import List
from collections import defaultdict

## Two sum

# brute force : time complexity - O(N²) quadratice time, space complexity o(1) constant time
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if  nums[i] + nums[j] == target:
                    return [i, j]
        return []

# hash table: time complexity - O(N) linear time, space complexity O(N) linear time
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

## contains duplicate

# hash map
def containsDuplicate(nums):
    seen = {}

    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen[num] = i
    return False

# hash set
def containsDuplicate2(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

## Best Time to Buy and Sell Stock
