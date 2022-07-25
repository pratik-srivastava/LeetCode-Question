class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=self.start_index(nums,target)
        end=self.end_index(nums,target)
        return [start,end]
    def start_index(self, nums: List[int], target: int) -> List[int]:
        beg=0
        a=-1
        stop=len(nums)-1
        while(beg<=stop):
            mid=(beg+stop)//2
            if target == nums[mid]:
                a=mid
                stop = mid-1
            elif target<nums[mid]:
                stop=mid-1
            else:
                beg=mid+1
        return a
    
                
    def end_index(self, nums: List[int], target: int) -> List[int]:
        beg=0
        b=-1
        stop=len(nums)-1
        while(beg<=stop):
            mid=(beg+stop)//2
            if target == nums[mid]:
                b=mid
                beg= mid+1
            elif target<nums[mid]:
                stop=mid-1
            else:
                beg=mid+1
        return b
    