# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode|None) -> int:
        if root is None:
            return 0
        min_depth: int = 0
        nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        first_leaf_founded: bool = False
        while not first_leaf_founded:
            for node in nodes:
                if node is None:
                    continue
                if node.left is None and node.right is None:
                    first_leaf_founded = True
                    break
                next_nodes.append(node.right)
                next_nodes.append(node.left)
            min_depth += 1
            nodes = next_nodes
            next_nodes = []
        return min_depth

    def minDepth1(self, root: TreeNode|None) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left: int = self.minDepth(root.left)
        right: int = self.minDepth(root.right)
        if 0 != left and 0 != right:
            return 1 + min(left, right)
        if 0 != left:
            return 1 + left
        else:
            return 1 + right

def examine()->None:
    root: TreeNode = make_tree([3,9,20,None,None,15,7])
    print(Solution().minDepth(root))

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
