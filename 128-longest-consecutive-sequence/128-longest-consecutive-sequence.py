class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        m=0
        c=0
        for i in nums:
            if i-1 not in s:
                k=i
                while k in s:
                    c+=1
                    k+=1
                m=max(c,m)
                c=0
        return m
