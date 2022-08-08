class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l=[]
        for i in matrix:
            for j in i:
                l.append(j)
        l.sort()
        return l[k-1]
        