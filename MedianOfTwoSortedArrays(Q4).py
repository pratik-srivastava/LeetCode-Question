class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lis=nums1 + nums2
        lis.sort()
        l=len (lis)
        if l%2==0:
            l1=lis[(l//2)-1]
            l2=lis[(l//2)]
            sums=(l1+l2)/2
            return sums
        else:
            l3=lis[((l+1)//2)-1]
            return l3
