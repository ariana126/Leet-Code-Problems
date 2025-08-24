# https://leetcode.com/problems/sum-of-left-leaves/
# Definition for a binary tree node.
from binary_tree_level_order_traversal import make_tree
from convert_sorted_array_to_binary_search_tree import print_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode|None) -> int:
        if root is None:
            return 0
        sum: int = 0
        if not root.left is None and root.left.left is None and root.left.right is None:
            sum += root.left.val
        elif not root.left is None:
            sum += self.sumOfLeftLeaves(root.left)
        if not root.right is None:
            sum += self.sumOfLeftLeaves(root.right)
        return sum

def examine()->None:
    root = make_tree([3,9,20,None,None,15,7])
    print(Solution().sumOfLeftLeaves(root))