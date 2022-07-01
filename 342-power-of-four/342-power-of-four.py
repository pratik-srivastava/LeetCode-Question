class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(20):
            if n== 4**i:
                return True
        return False