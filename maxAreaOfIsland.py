# LeetCode 695


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def getArea(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + getArea(i - 1, j) + getArea(i + 1, j) + getArea(i, j - 1) + getArea(i, j + 1)
            return 0

        area = [getArea(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(area) if area else 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))