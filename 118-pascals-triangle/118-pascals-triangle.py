class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        trow = [1]
        y = [0]
        l=[]
        for x in range(max(numRows,0)):
            l.append(trow)
            trow=[l+r for l,r in zip(trow+y, y+trow)]
        return l