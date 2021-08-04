from typing import List


class Solution:


    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def recursion(nums: [int], i: int) -> int:
            if i in memo:
                return memo[i]
            # base case
            if i == len(nums) - 1:
                return 1

            maxSubLength = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    maxSubLength = max(maxSubLength, recursion(nums, j) + 1)
                memo[i] = maxSubLength

            return maxSubLength

        return max(recursion(nums, i) for i in range(len(nums)))



if __name__ == '__main__':
    sol = Solution
    nums = [7, 7, 7, 7, 7, 7, 7]
    print(sol.lengthOfLIS(sol, nums))
