class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0 
        elif len(haystack) < len(needle) or needle not in haystack:
            return -1
        else:
            x = len(needle)
            for i in range(len(haystack)):
                if haystack[i:i+x]==needle:
                    return i
            return -1
