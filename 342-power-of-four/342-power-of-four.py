class Solution:
    def isPowerOfFour(self, n: int) -> bool:
    
        i=0
        while 1:
            if n > pow(4,i):
                i+=1
                continue
            elif n<pow(4,i):
                return False
            else:
                return True