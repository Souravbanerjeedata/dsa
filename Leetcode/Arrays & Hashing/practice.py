from typing import List
from collections import defaultdict

## Two sum

# brute force : time complexity - O(N²) quadratice time, space complexity o(1) constant time
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
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

# brute force time O(n2) | space O(1)
def maxProfit1(prices):
    res = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell = prices[j]
            res = max(res, sell - buy)
    return res

# two pointers - Time complexity: O(n) Space complexity: O(1)

def maxProfit2(prices):
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

## Valid Anagram

# sorting: Time complexity: O(nlog⁡n+mlog⁡m), Space complexity: O(1) or O(n+m) depending on the sorting algorithm.

def isAnagram(s,t):
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

# Hash map: Time complexity: O(n+m), Space complexity: O(1)

def isAnagram1(s,t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

## Group Anagrams

# sorting: Time complexity: O(m∗nlogn), Space complexity: O(m∗n)

def groupAnagrams1(strs):
    res = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())

