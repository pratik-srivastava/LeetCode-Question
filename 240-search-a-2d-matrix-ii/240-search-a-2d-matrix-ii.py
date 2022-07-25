class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        def bsearch(row):
            beg=0
            end=n-1
            while(beg<=end):
                mid=(beg+end)//2
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid]>target:
                    end=mid-1
                else:
                    beg=mid+1
            return False
        for row in range(m):
            if bsearch(row):
                return True
            
        return False
            
                
            