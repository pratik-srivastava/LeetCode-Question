class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0 
        i, j = 0, 0 
        while i < len(nums1) and j < len(nums2):
            if nums2[j] >= nums1[i]:
                res = max(res, j-i)
                j += 1 
            else: 
                i += 1
            
        return res 
