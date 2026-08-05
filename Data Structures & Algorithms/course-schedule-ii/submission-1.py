class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if not prerequisites:
            return list(range(numCourses))

        result = []


        # build adjacency list
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
            
        visited = set()
        visiting = set()

        def dfs(c):
            if c in visited:
                return True
            
            if c in visiting:
                return False

            visiting.add(c)

            for n in adj[c]:
                if not dfs(n):
                    return False

            visiting.remove(c)
            visited.add(c)
            result.append(c)
            return True

        for i in range(numCourses):
        # instead of just dfs(i)...
            if not dfs(i):
                return []
        
        return result
