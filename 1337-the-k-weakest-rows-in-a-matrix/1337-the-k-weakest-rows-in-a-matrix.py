class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            t = (sum(row), i)
            heapq.heappush(heap, t)
        
        res = []
        for i in range(k):
            row = heapq.heappop(heap)
            res.append(row[1])
        return res
