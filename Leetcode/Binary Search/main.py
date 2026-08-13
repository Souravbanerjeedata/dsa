# https://leetcode.com/problems/binary-search/description/
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            elif guess < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1 

# solution1 = Solution1()
# print(solution1.search([-1,0,3,5,9,12], 9))
# print(solution1.search([-1,0,3,5,9,12], 2))

# https://leetcode.com/problems/search-insert-position/

class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            elif guess < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = 1
        
        while left<=right:
            mid = (left+right)//2
            if isBadVersion(mid) == False:
                left = mid+1
            else:
                right = mid-1
                result = mid
                
        return result
    