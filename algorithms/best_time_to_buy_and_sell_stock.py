class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        l = 0
        maxSum = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxSum = max(profit, maxSum)
            else:
                l = r
            r += 1
        return maxSum
