# https://leetcode.com/problems/two-sum/
from typing import List

# Brute force:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# One-pass Hash Table:
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []

# https://leetcode.com/problems/contains-duplicate/description/

# using hash map
def containDuplicate(nums):
    seen = {}

    for i, num in enumerate(nums):
        if num in seen:
            return True
        
        seen[num] = i
    return False

# using hash set
def containDuplicate2(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
    left, right = 0, 1
    maxProfit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right += 1

    return maxProfit

