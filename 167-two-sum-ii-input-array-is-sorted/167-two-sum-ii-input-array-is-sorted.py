class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=[]
        i=0
        j=len(numbers)-1
        while (i<j):
            if (numbers[i]+numbers[j] == target):
                l.append (i+1)
                l.append(j+1)
                break
            elif (numbers[i]+numbers[j]>target):
                j-=1
            else:
                i+=1
            
        return l
    
        