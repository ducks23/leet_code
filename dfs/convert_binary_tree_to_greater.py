# leet code: https://leetcode.com/problems/convert-bst-to-greater-tree/submissions/969764649/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def reverse(self, node):
            if not node:
                return

            reverse(self, node.right)
            temp = self.total
            self.total += node.val
            node.val = temp + node.val


            reverse(self, node.left)


            
            return

        reverse(self, root)
        return root



