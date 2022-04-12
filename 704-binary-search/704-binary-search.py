class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target==nums[i]:
                return i
        else:
            return -1