from itertools import chain
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l=list(chain.from_iterable(matrix))
        l.sort()
        return l[k-1]
        