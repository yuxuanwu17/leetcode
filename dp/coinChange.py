from typing import List
import sys


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = (amount + 1) * [-666]

        def helper(coins: List[int], amount: int) -> int:
            # base case
            if amount == 0: return 0
            if amount < 0: return -1
            # memo iteration
            if memo[amount] != -666: return memo[amount]

            res = sys.maxsize
            for coin in coins:
                subProblems = helper(coins, amount - coin)
                if subProblems < 0: continue
                res = min(res, subProblems + 1)

            return -1 if res == sys.maxsize else res

        return helper(coins, amount)


if __name__ == '__main__':
    sol = Solution()
    result = sol.coinChange([1, 2, 5], 11)
    print(result)
