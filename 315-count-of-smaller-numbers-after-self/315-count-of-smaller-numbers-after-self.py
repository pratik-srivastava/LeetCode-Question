import bisect
class Solution(object):
    def countSmaller(self, nums):
        if len(nums) <1:
            return []
        arr = []
        res = []
        for num in nums[::-1]:
            index = bisect.bisect_left(arr, num)
            res.append(index)
            arr.insert(index, num)
        return res[::-1]