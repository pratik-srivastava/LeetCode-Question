class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        length1=len(nums1)
        length2=len(nums2)
        for i in range(length1):
            for  j in range(length2):
                if nums1[i]==nums2[j]:
                    l.append(nums1[i])
        
        return set(l)