class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp = min(nums)
        if 1 not in nums:
            return 1
        else:
            nums = set(nums)
            m=max(nums)
            for i in range(2,m+1):
                if i not in nums:
                    return i
            else:
                return m+1
        
        
