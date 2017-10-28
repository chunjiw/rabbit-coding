import math


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorials = [math.factorial(i) for i in range(n, 0, -1)]
        permutations = [0 for i in range(n)]

        # decompose k into factorials
        k = k - 1

        while k:
            for i in range(n):
                if k >= factorials[i]:
                    permutations[i] += 1
                    k -= factorials[i]
                    break

        nums = list(range(1, n + 1))
        for i in range(n):
            if permutations[i]:
                nums[i - 1], nums[i - 1 + permutations[i]] = nums[i - 1 + permutations[i]], nums[i - 1]

        return "".join([str(num) for num in nums])



if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation(3,5))

