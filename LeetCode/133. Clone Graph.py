"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        startVal = node.val
        start = dummy = Node(startVal, [])
        stack, seen = [(node, dummy)], {node: dummy}
        while stack:
            currentNode, currentDummy = stack.pop()
            for n in currentNode.neighbors:
                if n in seen:
                    currentDummy.neighbors.append(seen[n])
                else:
                    currentDummy.neighbors.append(Node(n.val, []))
                    stack.append((n, currentDummy.neighbors[-1]))
                    seen[n] = currentDummy.neighbors[-1]
        return start
