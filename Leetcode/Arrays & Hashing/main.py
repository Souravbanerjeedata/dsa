# https://leetcode.com/problems/two-sum/
from typing import List
from collections import defaultdict

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

# https://leetcode.com/problems/valid-anagram/description/

# Brute Force
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# 1 Hash Map
def isAnagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counter = {}

    for char in s:
        counter[char] = counter.get(char, 0) + 1

    for char in t:
        if char not in counter or counter[char] == 0:
            return False 

        counter[char] -= 1
    return True

# 2 Hash Map
def isAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_counter = {}
    t_counter = {}

    for i in range(len(s)):
        s_counter[s[i]] = 1 + s_counter.get(s[i], 0)
        t_counter[s[i]] = 1 + t_counter.get(t[i], 0)

    return s_counter == t_counter

# https://leetcode.com/problems/group-anagrams/

# Sorting
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)

    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)

    return list(res.values())

# Hash Table
def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        res[tuple(count)].append(s)

    return list(res.values())

# https://leetcode.com/problems/top-k-frequent-elements/description/

# Sorting
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    arr = []
    for num, cnt in count.items():
        arr.append([cnt, num])
    arr.sort()

    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    return res

# Bucket Sort
