class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        dfs check state, mark state, recurse on neighbors, return boolean
        - false if cycle, true if no cycle
        - three states: visited, visiting, unvisited
        - 
        """
        # bases?
        if not prerequisites: 
            return True

        # build adjacency list 
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)

        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False

            if node in visited:
                return True
            
            # if unvisited, mark visiting/add to path
            visiting.add(node)

            # recurse
            for neighbor in adj[node]:
                if not dfs(neighbor): # uses result of recursive dfs call
                    return False

            # mark visited
            visiting.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True