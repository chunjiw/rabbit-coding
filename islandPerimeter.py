class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return 0
        width, depth, peri = len(grid), len(grid[0]), 0

        for i in range(width):
            for j in range(depth):
                if i == 0:
                    if grid[i][j] == 1:
                        peri += 1
                else:
                    peri += (grid[i - 1][j] != grid[i][j])
                if i == width - 1 and grid[i][j] == 1:
                    peri += 1

                if j == 0:
                    if grid[i][j] == 1:
                        peri += 1
                else:
                    peri += (grid[i][j - 1] != grid[i][j])
                if j == depth - 1 and grid[i][j] == 1:
                    peri += 1

        return peri

if __name__ == "__main__":
    sol = Solution()
    print(sol.islandPerimeter([]))
    print(sol.islandPerimeter([[0,1], [1,1]]))