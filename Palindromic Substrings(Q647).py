class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        l=[]
        n=len(s)
        def substring(s,n):
            for i in range(n):
                for j in range(i+1,n+1):
                    l.append(s[i:j])
        substring(s,n)
        for i in l:
            if i == i[::-1]:
                count+=1
        return count
