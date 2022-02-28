class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1=sorted(s)
        t1=sorted(t)
        l=len(t1)
        for i in range(len(s1)):
            if s1[i] != t1[i]:
                return t1[i]
            else:
                continue
        return t1[l-1]
