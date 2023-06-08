"""
problem:

https://leetcode.com/problems/balanced-binary-tree/
"""
class Solution:
    def isBalanced(self, root) -> bool:

        def dfs(node):
            balanced = True
            if not node:
                return True, 0

            l = dfs(node.left)
            r = dfs(node.right)
            

            if l and r:
                if abs(l[1] - r[1]) > 1:
                    balanced = False
            
            return balanced, max(l[1],r[1]) + 1

        return dfs(root)[0]

