# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start =1
        end =n
        
        while start<=end:
            mid = (start+end)//2
            if (isBadVersion(mid) and not isBadVersion(mid-1)): #optimization using second parameter
                return mid
            elif(not isBadVersion(mid)):
                start = mid+1 
            else:
                end = (mid-1)