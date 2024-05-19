# 2331. Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/description/?envType=daily-question&envId=2024-05-16

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        booleans = [0, 1]

        def evaluate(node: Optional[TreeNode]) -> bool:
            if node.val in booleans:
                return node.val == 1
            
            left, right = evaluate(node.left), evaluate(node.right)
            if node.val == 2:
                return left or right
            
            return left and right
        
        return evaluate(root)
