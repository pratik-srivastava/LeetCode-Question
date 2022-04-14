class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res=1
        while True:
            q=res*res
            if q==num:
                return True
            elif q>num:
                return False
            res+=1
        