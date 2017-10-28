# LeetCode 697
# 5:51

from collections import Counter

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n)
        """
        c = Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        deg = max(c.values())
        minlen = len(nums)
        for num in nums:
            if c[num] == deg:
                minlen = min(minlen, last[num] - first[num] + 1)
        return minlen

if __name__ == "__main__":
    sol = Solution()
    print(sol.findShortestSubArray([1,2,2,3,1]))