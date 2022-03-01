class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        a=0
        flag=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                diff=nums[j]-nums[i]
                if nums[i]<nums[j] and diff>a:
                    flag=1
                    a=diff
        if flag==0:
            return -1
        return a
            
