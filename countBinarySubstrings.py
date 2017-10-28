# LeetCode 696


class Solution(object):

    def countBinarySubstrings(self, s):
        # dp, O(n)
        if not s:
            return

        sublen = [0]
        result = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                sublen.append(1)
                result += 1
            else:
                if sublen[-1] and 0 <= i - 2 * sublen[-1] - 1 and s[i - 2 * sublen[-1] - 1] != s[i]:
                    result += 1
                    sublen.append(sublen[-1] + 1)
                else:
                    sublen.append(0)
        return result

    def countBinarySubstrings0(self, s):
        """
        :type s: str
        :rtype: int
        this version has time complexity worst case n^2, which is bad.
        """
        if not s:
            return

        result = 0
        for i in range(1, len(s)):
            times = 1
            j = i - 1
            while 0 <= j and s[j] == s[i]:
                j -= 1
                times += 1
            while 0 <= j and s[j] != s[i] and times:
                j -= 1
                times -= 1
            if not times:
                result += 1
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBinarySubstrings0('10'))
    print(sol.countBinarySubstrings('10'))