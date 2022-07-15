class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        
        def helper(row, col):
            nonlocal max_area, area
			
            if row >= rows or row < 0 or col >= cols or  col < 0 or grid[row][col] != 1:
                return
			
            area = area + 1
            grid[row][col] = '#'
			
            helper(row + 1, col)
            helper(row - 1, col)
            helper(row, col + 1)
            helper(row, col - 1)
            
		
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
				   
                    area = 0
                    helper(row, col)
                    max_area = max(area, max_area)
        return max_area