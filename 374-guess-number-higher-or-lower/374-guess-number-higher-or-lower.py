# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        h=n
        while l<=h:
            m=(l+h)//2
            r=guess(m)
            if r<0:
                h=m-1
            elif r>0:
                l=m+1
            else:
                return m
        
        
