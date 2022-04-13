class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        up, down, left, right = 0, n-1, 0, n-1
        
        num = 1
        while num <= (n * n):
            for idx in range(left, right + 1):
                matrix[up][idx] = num
                num+=1
            
            for idx in range(up + 1, down + 1):
                matrix[idx][right] = num
                num+=1
            
            # not the same row
            if up != down:
                for idx in range(right - 1, left - 1, -1):
                    matrix[down][idx] = num
                    num+=1
            #not the same column
            if left != right:
                for idx in range(down - 1, up, -1):
                    matrix[idx][left] = num
                    num+=1
            
            left+=1
            up+=1
            right-=1
            down-=1
        return matrix
