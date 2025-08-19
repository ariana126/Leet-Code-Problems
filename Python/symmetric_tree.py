# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # TODO
        return False

    def isSymmetric1(self, root: TreeNode) -> bool:
        def check(left: TreeNode | None, right: TreeNode | None)-> bool:
            if left is None and right is None:
                return True
            if (left is not None and right is None) or (right is not None and left is None):
                return False
            if left.val != right.val:
                return False
            if not check(left.left, right.right):
                return False
            if not check(left.right, right.left):
                return False
            return True
        return check(root.left, root.right)

def examine()->None:
    # root = make_tree([1,2,2,None,3,None,3])
    # root = make_tree([1,2,2,3,4,4,3])
    root = make_tree([1, None, 1])

    solution = Solution()
    output = solution.isSymmetric(root)
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