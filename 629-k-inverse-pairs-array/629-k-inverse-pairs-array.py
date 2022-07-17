class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        if k == 0: return 1
        memo = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            memo[i][0] = 1
        if n < 2:
            return memo[n][k]
        memo[2][1] = 1

        for i in range(3, n + 1):
            mx = min(k, (n * (n - 1)) // 2)
            for j in range(1, mx + 1):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

                if j >= i:
                    memo[i][j] -= memo[i - 1][j - i]
        return memo[n][k] % mod
