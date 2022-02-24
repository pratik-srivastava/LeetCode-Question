class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_num=len(nums)
        i=0
        while(i<len_num):
            if nums[i]==val:
                del nums[i]
                len_num -=1
            else:
                i+=1
            
        return len_num
    
