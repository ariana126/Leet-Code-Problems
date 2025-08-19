# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
# Definition for a binary tree node.
import math
from operator import index


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

def examine()->None:
    root: TreeNode = make_tree([3,9,20,None,None,15,7])

    # print_tree(root)

    solution = Solution()
    output: int = solution.maxDepth(root)
    print(output)

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

def print_tree(root: TreeNode | None) -> None:
    if root is None:
        print(None)
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)