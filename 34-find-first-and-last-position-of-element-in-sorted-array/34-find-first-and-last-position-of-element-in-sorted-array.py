class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        l1=[-1,-1]
        l2=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
                continue
        if len(l)>2:
            b=l[0]
            c=l[len(l)-1]
            l2.append(b)
            l2.append(c)
            return l2
                
        if len(l)==1:
            a=l[0]
            l.append(a)
            return l
        
        if target not in nums:
            return l1
        return l
    
            
            
                