class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s or len(s) == 1:
            return s
        s = list(s)
        start = 0
        while start + 2 * k <= len(s):
            self.reverse(s, start, start + k)
            start += 2 * k
        if start + k > len(s):
            self.reverse(s, start, len(s))
        else:
            self.reverse(s, start, start + k)
        return ''.join(s)

    def reverse(self, s, i, j):
        while j - i > 1:
            s[i], s[j - 1] = s[j - 1], s[i]
            i += 1
            j -= 1
        return

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseStr('abcdefg', 8))