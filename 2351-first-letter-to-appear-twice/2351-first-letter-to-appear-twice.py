class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                return i
            else:
                d[i]=1
         