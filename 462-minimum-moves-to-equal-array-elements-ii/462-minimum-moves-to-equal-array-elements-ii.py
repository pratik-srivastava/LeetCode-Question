class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)

        mid=nums[len(nums)//2]
        cnt=0
        for i in nums:
            cnt+=abs(mid-i)
        return cnt
            