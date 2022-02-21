class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[c]:
                c+=1
                nums[c]=nums[i]
        return c+1
