class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(x, y):
            # Base case
            # If current [x, y] is invalid (not 1 or explored]), return 0
            if (
                x < 0
                or x >= len(grid)
                or y < 0
                or y >= len(grid[x])
                or grid[x][y] == 0
            ):
                return 0

            grid[x][y] = 0
            # Conditions, besides the [x, y] that was coming from, explore toching [x, y]
            # Sum up the exploration
            area = (1
            +explore(x + 1, y)
            +explore(x - 1, y)
            +explore(x, y + 1)
            +explore(x, y - 1)
            )

            return area

        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    max_area = max(max_area, explore(x, y))

        return max_area
