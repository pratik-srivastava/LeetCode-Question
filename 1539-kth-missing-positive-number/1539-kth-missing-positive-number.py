class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        dummy_arr=arr[::-1]
        l=[]
        cnt=k+dummy_arr[0]
        for i in range(1,cnt+1):
            if i not in arr:
                l.append(i)
        return l[k-1]
                