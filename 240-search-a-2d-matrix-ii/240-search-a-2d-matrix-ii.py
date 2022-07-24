class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for j in i:
                if target == j:
                    return True
        return False
                
                
        