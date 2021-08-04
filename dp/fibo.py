from typing import List


class Solution:
    def fib(self, n: int) -> int:
        memo = (n + 1) * [0]

        def helper(memo: List[int], n: int) -> int:
            # memo
            if memo[n] != 0:
                return memo[n]

            # base case
            if n == 1 or n == 0:
                return n

            memo[n] = helper(memo, n - 1) + helper(memo, n - 2)

            return memo[n]

        return helper(memo, n)

    def fib2(self, n: int) -> int:
        if n == 0: return 0
        dp = (n + 1) * [0]

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    sol = Solution
    print(sol.fib(sol, 3))
    print(sol.fib2(sol, 3))
