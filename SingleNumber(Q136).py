from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        for key,i in count.items():
            if i==1:
                return key
            
        
