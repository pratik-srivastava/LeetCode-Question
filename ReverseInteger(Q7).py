class Solution:
    def reverse(self, x: int) -> int:
        r=int(str(abs(x))[::-1])
        if r.bit_length()>31:
            return 0
        return -1*r if x<0 else r
