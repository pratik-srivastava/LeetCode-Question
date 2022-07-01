class Solution:
	def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
		boxTypes = sorted(boxTypes, key = lambda x : x[1], reverse = True)
		output = 0
		for no, units in boxTypes:
			if truckSize > no:
				truckSize -= no
				output += (no * units)
			else:
				output += (truckSize * units)
				break
		return output
