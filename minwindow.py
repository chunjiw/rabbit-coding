import collections


class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tcount = collections.Counter(t)

        # min window length, and their start and end index
        wlen = len(s) + 1
        left, right = 0, -1

        # queue for elements in t
        queue = []

        # number of elelments left
        toFound = len(t)

        for i in range(len(s)):
            if s[i] in tcount:
                tcount[s[i]] -= 1
                queue.append((s[i], i))
                if tcount[s[i]] >= 0:
                    toFound -= 1
                if toFound == 0:
                    if wlen > queue[-1][1] - queue[0][1] + 1:
                        wlen = queue[-1][1] - queue[0][1] + 1
                        left, right = queue[0][1], queue[-1][1]
                    while tcount[queue[0][0]] < 0:
                        if wlen > queue[-1][1] - queue[1][1] + 1:
                            wlen = queue[-1][1] - queue[1][1] + 1
                            left, right = queue[1][1], queue[-1][1]
                        tcount[queue[0][0]] += 1
                        del queue[0]
        return s[left:(right + 1)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("cabwefgewcwae", "cae"))