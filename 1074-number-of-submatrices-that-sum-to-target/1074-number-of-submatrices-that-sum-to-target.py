class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        res, R, C = 0, len(matrix), len(matrix[0])
        for row in range(R):
            for col in range(1, C):
                matrix[row][col] += matrix[row][col - 1]
        for colPtr1 in range(C):
            for colPtr2 in range(colPtr1, C):
                cur, counter = 0, defaultdict(int)
                counter[0] = 1
                for row in range(R):
                    cur += matrix[row][colPtr2] - (matrix[row][colPtr1 - 1] if colPtr1 > 0 else 0)
                    res += counter[cur - target]
                    counter[cur] += 1
        return res
