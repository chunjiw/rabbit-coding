import time


class Solution:
    def get_combinations(self, total, coins):
        result = []
        counter = [0]
        t0 = time.time()
        self.dfs(total, coins, 0, result, [], counter)
        t1 = time.time()
        print("{} calls to dfs() in {} seconds with result {}".format(counter[0], t1 - t0, len(result)))
        t0 = time.time()
        dpr = self.dp(total, coins)
        t1 = time.time()
        print("dp in {} seconds with result {}".format(t1 - t0, dpr))

    def dp(self, target, coins):
        dp = [0 for i in range(target + 1)]
        for i in range(1, target + 1):
            for c in coins:
                if i - c > 0:
                    dp[i] += dp[i - c]
        return dp[-1]

    def dfs(self, target, coins, k, result, solution, counter):
        counter[0] += 1
        if len(solution) == len(coins):
            if target == 0:
                result.append(list(solution))
            return
        for i in range(int(target/coins[k]) + 1):
            solution.append(i)
            self.dfs(target - i * coins[k], coins, k + 1, result, solution, counter)
            solution.pop()


if __name__ == "__main__":
    sol = Solution()
    result = sol.get_combinations(9, [2, 3])
    print(result)