class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # 1. sort the arrays
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # 2. set initial values for max_width, max_height. 
		# They can only be the maximums between the lengths from reference (0) to 
		# the 1st cut horizontalCuts[0]/ verticalCuts[0] and the difference between h or w 
		# and last cut location from reference.
        max_width, max_height = max(horizontalCuts[0], h - horizontalCuts[-1]), max(verticalCuts[0], w - verticalCuts[-1])
        
        #3. Only when multiple cuts are made in cake:
			# This part is only required when there are multiple cuts otherwise
			# the initialization value will be sufficient to calculate the result.
        if len(horizontalCuts) > 1:
            for index_1 in range(1, len(horizontalCuts)):
                max_width = max(max_width, horizontalCuts[index_1] - horizontalCuts[index_1 - 1])
        if len(verticalCuts) > 1:
            for index_2 in range(1, len(verticalCuts)):
                max_height = max(max_height, verticalCuts[index_2] - verticalCuts[index_2 - 1])
                
        return (max_height * max_width) % (10**9 + 7)