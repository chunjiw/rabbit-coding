import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        if k == 1:
            return "".join([str(num) for num in range(1, n + 1)])

        start = 1
        while k > math.factorial(start):
            start += 1
        start -= 1

        nums = list(range(1, n + 1))
        nums[-start], nums[-start - 1] = nums[-start - 1], nums[-start]

        for i in range(k - math.factorial(start) - 1):
            self.nextPermutation(nums)
        return "".join([str(num) for num in nums])


    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        nums.reverse()
        found = False

        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                found = True
                p = i + 1
                break
        if not found:
            return

        for i in range(0, p):
            if nums[i] > nums[p]:
                q = i
                break
        nums[p], nums[q] = nums[q], nums[p]
        self.reverse(nums, 0, p - 1)
        nums.reverse()
        return

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

if __name__ == "__main__":
    sol = Solution()
    array = [1,3,2]
    sol.nextPermutation(array)
    print(sol.getPermutation(4,8))