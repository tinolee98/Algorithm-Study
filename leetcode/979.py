# 979. Distribute Coins in Binary Tree
# https://leetcode.com/problems/distribute-coins-in-binary-tree/description/?envType=daily-question&envId=2024-05-18

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        move_count = 0

        def distribute(parent: Optional[TreeNode], node: TreeNode) -> (int, int):
            # return new_parent_val, move_count
            curr_move_count = 0

            # leaf node
            if node.left == None and node.right == None:
                # only root
                if parent == None:
                    return 0, 0
                return parent.val + node.val - 1, abs(node.val - 1)
            if node.left != None:
                node.val, temp = distribute(node, node.left)
                curr_move_count += temp

            if node.right != None:
                node.val, temp = distribute(node, node.right)
                curr_move_count += temp

            if parent == None:
                return node.val - 1, curr_move_count + abs(node.val - 1)

            return parent.val + node.val - 1, curr_move_count + abs(node.val - 1)
        
        _, move_count = distribute(None, root)
        return move_count
        