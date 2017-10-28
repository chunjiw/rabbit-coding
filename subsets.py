import collections


class Solution():

    def subsetsWithDup(self, nums):
        c = collections.Counter(nums)
        nums = []
        for i in c:
            nums.append((i, c[i]))
        result, solution = [], []
        self.ss(nums, 0, result, solution)
        return result

    def ss(self, nums, k, result, solution):
        if len(nums) == k:
            result.append(list(solution))
            return
        for i in range(nums[k][1] + 1):
            for j in range(i):
                solution.append(nums[k][0])
            self.ss(nums, k + 1, result, solution)
            for j in range(i):
                solution.pop()

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2]))