# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode|None, q: TreeNode|None) -> bool:
        if p is None or q is None:
            return p == q
        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left) or not self.isSameTree(p.right, q.right):
            return False
        return True


def examine()->None:
    root1: TreeNode = make_tree([1, 3, None])
    root2: TreeNode = make_tree([1, None, 3])
    print(Solution().isSameTree(root1, root2))

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

