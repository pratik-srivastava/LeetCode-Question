#Copied
class Solution:
    
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def f(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if word1[i]==word2[j]:
                return 0+f(i-1,j-1)
            insert=1+f(i,j-1)
            delete=1+f(i-1,j)
            replace=1+f(i-1,j-1)
            return min(insert,min(delete,replace))
        n=len(word1)
        m=len(word2)
        return f(n-1,m-1)