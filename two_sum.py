# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#  
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
#
# Constraints:
#
# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # print(i)
            a = nums[i]
            # print(a)
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if a + b == target:
                    return [i, j]
                else:
                    continue

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        dct ={}
        for index, number in enumerate(nums):
            cp = target-number
            if cp in dct:
                return [dct[cp],index]
            else:
                dct[number] = index


nums = (2, 7, 11, 15)
target = 9
# sol1 = Solution.twoSum(Solution, nums, target)
# print(sol1)
sol2 = Solution.twoSum1(Solution,nums, target)
print(sol2)