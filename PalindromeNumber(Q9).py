class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1 = ""
        for i in str(x):
            s1 = i + s1
        return str(x) == str(s1)
