class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        elif n>=0:
            
            q=n//5
            return q+self.trailingZeroes(n//5)
        else:
            return 0
        
