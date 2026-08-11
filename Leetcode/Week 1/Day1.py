# https://leetcode.com/problems/binary-search/description/
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List
class Solution:
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

# solution = Solution()
# print(solution.search([-1,0,3,5,9,12], 9))
# print(solution.search([-1,0,3,5,9,12], 2))