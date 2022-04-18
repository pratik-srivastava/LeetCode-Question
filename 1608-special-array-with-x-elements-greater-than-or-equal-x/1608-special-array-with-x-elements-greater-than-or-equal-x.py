class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if n<=nums[0]:
            return n
        
        for i in range(1,n):
            count = n-i       #counts number of elements in nums greater than equal i
            if nums[i]>=(count) and (count)>nums[i-1]:
                return count 
        return -1

        