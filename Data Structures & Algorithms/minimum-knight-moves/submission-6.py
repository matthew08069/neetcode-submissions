from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
                # Use symmetry
        x = abs(x)
        y = abs(y)

        directions = [
            (1, 2), (2, 1),
            (-1, 2), (-2, 1),
            (1, -2), (2, -1),
            (-1, -2), (-2, -1)
        ]

        queue = deque([(0, 0)])
        visited = {(0, 0)}
        step = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                cur_x, cur_y = queue.popleft()

                if cur_x == x and cur_y == y:
                    return step

                for dx, dy in directions:
                    next_x = cur_x + dx
                    next_y = cur_y + dy

                    # Only explore the useful region
                    if (-2 <= next_x <= x + 2 
                    and -2 <= next_y <= y + 2 
                    and (next_x, next_y) not in visited
                    ):
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))

            step += 1
