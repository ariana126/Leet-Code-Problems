# https://leetcode.com/problems/path-sum/description/
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode|None, targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum1(self, root: TreeNode|None, targetSum: int) -> bool:
        if root is None:
            return False
        current_nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        while 0 != len(current_nodes):
            for node in current_nodes:
                if targetSum == node.val and node.left is None and node.right is None:
                    return True
                if not node.left is None:
                    node.left.val = node.val + node.left.val
                    next_nodes.append(node.left)
                if not node.right is None:
                    node.right.val = node.val + node.right.val
                    next_nodes.append(node.right)
            current_nodes = next_nodes
            next_nodes = []
        return False


def examine()->None:
    root = make_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    print(Solution().hasPathSum(root, 22))

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

