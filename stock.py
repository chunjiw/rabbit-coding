class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices.insert(0, float('inf'))
        prices.append(float('-inf'))
        i, j = 0, 1
        count = list(prices)
        count[i] = 0
        while j < len(prices):
            if prices[j] != prices[i]:
                i += 1
                prices[i] = prices[j]
                j += 1
                count[i] = 0
            else:
                j += 1
                count[i] += 1
        prices = prices[0: i + 1]
        count = count[0: i + 1]

        minp, maxp = [], []
        for i in range(1, len(prices) - 1):
            if prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:
                minp.append(i)
            if prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:
                maxp.append(i)

        profit = 0
        for i in range(len(minp)):
            profit += prices[maxp[i]] - prices[minp[i]]

        return profit

if __name__ == '__main__':
    sol = Solution()
    a = sol.maxProfit([8,6,4,3,3,2,3,5,8,3,8,2,6])
    print(a)