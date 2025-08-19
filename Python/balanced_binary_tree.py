# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        self.traverse(root.left)
        self.traverse(root.right)
        return self.is_balanced_dp(root)

    def is_balanced_dp(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is None:
            left = 0
        else:
            left = root.left.val
        if root.right is None:
            right = 0
        else:
            right = root.right.val

        if abs(left - right) > 1:
            return False
        return self.is_balanced_dp(root.left) and self.is_balanced_dp(root.right)

    def traverse(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 1 + max(self.traverse(root.left), self.traverse(root.right))
        root.val = depth
        return depth

def examine()->None:
    root = make_tree([1,2,2,3,None,None,3,4,None,None,4])
    print(Solution().isBalanced(root))
def make_tree(nodes: list[int | None]) -> TreeNode:
    root: TreeNode = TreeNode(nodes[0])
    depth: int = int(math.log((len(nodes) + 1), 2))
    depth_nodes: list[TreeNode | None] = [root]
    for i in range(1, depth):
        new_depth_node: list[TreeNode | None] = []
        current_index: int = 2 ** i - 1
        for j, root_node in enumerate(depth_nodes):
            if root_node is None:
                current_index += 2
                continue
            left: TreeNode | None = None
            if nodes[current_index] is not None:
                left = TreeNode(nodes[current_index])
            right: TreeNode | None = None
            if nodes[current_index + 1] is not None:
                right = TreeNode(nodes[current_index + 1])

            root_node.left = left
            root_node.right = right

            new_depth_node.append(left)
            new_depth_node.append(right)

            current_index += 2
        depth_nodes = new_depth_node
    return root
