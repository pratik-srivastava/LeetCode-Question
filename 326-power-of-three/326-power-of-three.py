class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(50):
            if n==(3**i):
                return True
        
        return False
        