class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """

        """

        # base
        if not heights:
            return None

        # create queue
        from collections import deque
        pacific_queue = deque()
        atlantic_queue = deque()

        # create sets for cells that can reach each ocean
        pacific = set()
        atlantic = set()

        # add border cells to queue and to sets
        for r in range(len(heights)): 
            pacific_queue.append((r, 0))
            pacific.add((r, 0))

            atlantic_queue.append((r, len(heights[0])-1))
            atlantic.add((r, len(heights[0])-1))
        
        for c in range(len(heights[0])):
            pacific_queue.append((0, c))
            pacific.add((0, c))

            atlantic_queue.append((len(heights)-1, c))
            atlantic.add((len(heights)-1, c))

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)] 
        # bfs algorithm
        def bfs(queue, s):
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    row =  r + dr
                    col = c + dc

                    # if invalid
                    if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]):
                        continue

                    # if not already valid
                    if (row, col) not in s and heights[row][col] >= heights[r][c]: 
                        s.add((row, col))
                        queue.append((row, col))

        # first pass for pacific ocean
        bfs(pacific_queue, pacific)
        
        # second pass for atlantic ocean
        bfs(atlantic_queue, atlantic)

        return list(pacific & atlantic)
