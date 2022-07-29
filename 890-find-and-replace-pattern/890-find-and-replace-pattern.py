class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            if len(set(pattern)) == len(set(word)):
                tempDict = {}
                Flag = False
                for i in range(len(pattern)):
                    if pattern[i] not in tempDict:
                        Flag= True
                        tempDict[pattern[i]] = word[i]
                    elif pattern[i] in tempDict and tempDict[pattern[i]] != word[i]:
                        Flag = False
                        break
                if Flag== True:
                    result.append(word)
        return result
        
            
        
        
        
        
        
        
        
#         ans = []
#         d = {}
#         for i in pattern:
#             d[i] = d.get(i , 0) + 1
#         #print(d)
                
#         for i in words:
#             d1 = {}
#             for j in i:
#                 d1[j] = d1.get(j , 0) + 1
#             a = list(d.values())
#             b = list(d1.values())
#             #print(a , b)
#             #a.sort()
#             #b.sort()
#             if a == b:
#                 ans.append(i)
#         return ans