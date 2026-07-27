class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        basically: find length of shortest path from 
            rotten fruit to furthest fresh fruit
        - or is it compute distances from rot to fresh fruits 
            and return max
        
        imp: similar to num of islands where if found fresh:
            - min += 1?
            - mark rotten
            - how to handle empty?
            - start at rotten?

        cases confusing me:
            how to handle if multiple rotted at start

        base: 
            - no rotten fruits
        
        other -1 case:
            - disconnected rotten fruits
            - handled through implementation?

        use bfs to traverse
        loop over grid applying bfs?

        structure clarification
        1. Scan grid, add all rotten oranges to queue, 
            count fresh oranges
        2. BFS from all sources simultaneously
        3. Each time a fresh orange rots, 
            decrement fresh count, track minutes
        4. After BFS: if fresh count > 0, 
            return -1, else return minutes
        """

        # if no rotten fruits exist
        # rot = 2
        # if not any(rot in row for row in grid):
        #     return -1

        from collections import deque

        fresh = 0
        queue = deque() # (r, c, min)
        # scan grid queueing rots, counting fresh
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))

        if fresh == 0:
            return 0
        # base: if no rotten
        if not queue:
            return -1
        

        def bfs(queue, fresh):
            minutes = 0
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                r, c, mins = queue.popleft()

                for vert, horz in directions:
                    row, col = r + vert, c + horz

                    # out of bounds
                    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                        continue
                    
                    # if not fresh
                    if grid[row][col] != 1:
                        continue

                    # rot this orange
                    grid[row][col] = 2
                    fresh -= 1
                    minutes = mins + 1
                    queue.append((row, col, minutes))
            
            return minutes, fresh

        time = 0
        time, remaining = bfs(queue, fresh)

        if remaining > 0:
            return -1

        return time

        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 1: # if fresh
        #             grid[r][c] == 2
        #             mins = 1 + minutes
        #             queue.append([r, c, mins])
        #             fresh -= 1
            
        # return minutes