class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        while l<=r:
            mid=l+(r-l)//2
            if ((arr[mid-1]<arr[mid]) and (arr[mid]>arr[mid+1])):
                return mid
            elif (arr[mid-1]<arr[mid]<arr[mid+1]):
                l=mid
            else:
                r=mid