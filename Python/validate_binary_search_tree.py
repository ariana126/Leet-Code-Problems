# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode, small: int | None = None, big: int | None = None) -> bool:
        if root is None:
            return True
        if small is not None and root.val <= small:
            return False
        if big is not None and root.val >= big:
            return False
        return self.isValidBST(root.left, small, root.val) and self.isValidBST(root.right, root.val, big)

def examine()->None:
    root = make_tree([2, 1, 3, 0, None, None, None])
    # root = make_tree([5,4,6,None,None,3,7])

    solution = Solution()
    output = solution.isValidBST(root)
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
