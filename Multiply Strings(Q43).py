class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.str_to_int(num1)*self.str_to_int(num2))
    def str_to_int(self,n):
        res=0
        for i in range(len(n)):
            res=res*10+ord(n[i])-ord('0')
        return res
    
