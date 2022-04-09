class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

# freq dict
        d = {}
        for num in nums:
	        if num in d:
		        d[num] += 1
	        else:
		        d[num] = 1

# insert k items into heap O(nlog(k))
        h = []
        from heapq import heappush, heappop
        for key in d: # O(N)
	        heappush(h, (d[key], key)) # freq, item - O(log(k))
	        if len(h) > k:
		        heappop(h)

        res = []
        while h: # O(k)
	        frq, item = heappop(h) # O(logk)
	        res.append(item)
        return res