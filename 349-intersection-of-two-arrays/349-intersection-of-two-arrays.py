class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        length1=len(nums1)
        length2=len(nums2)
        for i in nums1:
            if i in nums2:
                l.append(i)
        
        return set(l)