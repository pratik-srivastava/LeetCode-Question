class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum1=0
        l=len(salary)
        for i in range(1,l-1):
            sum1+=salary[i]
        return sum1/(l-2)
        
