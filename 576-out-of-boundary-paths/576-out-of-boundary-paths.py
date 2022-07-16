class Solution:
		def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

			@lru_cache(None)
			def moves(move,row,col):
				if row==m or row<0 or col<0 or col==n:
					return 1
				if move==0:
					return 0
				move-=1

				return (moves(move,row+1,col)+moves(move,row,col+1)+moves(move,row-1,col)+moves(move,row,col-1))%((10**9)+7)


			return moves(maxMove,startRow,startColumn)