class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candies = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
        return sum(candies)