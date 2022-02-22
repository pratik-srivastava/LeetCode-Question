class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        dic = {'(':')','[':']','{':'}'}
        stack=[]
        g=dic.keys()
        for c in s:
            if c in dic.keys():
                stack.append(c)
            else:
                if stack==[]:
                    return False
                a = stack.pop()
                if c!=dic[a]:
                    return False
        return stack == []
        
