class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mc = Counter()
        for w in words2:
            t = Counter(w)
            for i in t:
                mc[i] = max(mc[i],t[i])

        ans = []
        for w in words1:
            t = Counter(w)
            for i in mc:
                if mc[i]>t[i]:
                    break
            else:
                ans.append(w)
        return ans
                
                    