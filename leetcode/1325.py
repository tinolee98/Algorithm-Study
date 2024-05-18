# 1325. Delete Leaves With a Given Value
# https://leetcode.com/problems/delete-leaves-with-a-given-value/description/?envType=daily-question&envId=2024-05-18

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def canRemoveNode(node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
            if node == None:
                return None

            node.left = canRemoveNode(node.left, target)
            node.right = canRemoveNode(node.right, target)

            if node.val == target and node.left == None and node.right == None:
                return None
                
            return node

        return canRemoveNode(root, target)
                