# leetcode : https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = ''
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def pre_order(self, node):

            if node:
                
                self.result += '('
                self.result += str(node.val)

                if not node.left and node.right:
                    self.result += '()'
                left = pre_order(self, node.left)
                right = pre_order(self, node.right)
                self.result += ')'


        pre_order(self, root)
        return self.result[1:-1]

