"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        given a node in graph, 'clone' entire graph, creating new nodes with 
            same val/neighbors as original
        - when cloning neighbors, some might have already been cloned if they were
            neighbors of previously cloned nodes,
            - to mitigate, track which nodes have been cloned:
                hash map: original node -> cloned node
            - tracks visited by being key in hashmap
            - tracks clone

        clone first node by:
            clone with value
            clone each neighbor to be able to list neighbor clones as neighbors
        """
        if not node:
            return None

        visited = {}

        # clone initial node
        # copy = Node()
        # copy.val = node.val

        # helper
        def clone(n):
            if n in visited:
                return visited[n]
            c = Node()
            c.val = n.val
            visited[n] = c
        
            # for each neighbor, if not cloned, clone
            for neighbor in n.neighbors:
                # add cloned neighbor to neighbors var
                c.neighbors.append(clone(neighbor)) # recurse on each neighbor
            return c

        # how to do this for each neighbor as well nto just initial node- recurse?

        return clone(node)