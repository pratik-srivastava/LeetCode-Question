class Solution:
    def shortestPalindrome(self, s: str) -> str:
        l=list(s)
        n=len(s)
        if n<=1 or l==l[::-1]:
            return "".join(l)
        for i in range(n):
            l.insert(i,l[n-1])
            if l==l[::-1]:
                return "".join(l)
            
            