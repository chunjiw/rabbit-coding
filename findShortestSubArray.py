# LeetCode 697
# 5:51

from collections import Counter

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(kn), where k is the number of most frequent elements in nums
        """
        c = Counter(nums)
        freq = [(t[1],t[0]) for t in c.items()]
        freq.sort(reverse=True)
        result = len(nums)
        for t in freq:
            if t[0] == freq[0][0]:
                result = min(result, self.helper(nums, t[1]))
        return result

    def helper(self, nums, target):
        i, j = 0, len(nums) - 1
        while nums[i] != target:
            i += 1
        while nums[j] != target:
            j -= 1
        return j - i + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.findShortestSubArray([1,2,2,3,1]))