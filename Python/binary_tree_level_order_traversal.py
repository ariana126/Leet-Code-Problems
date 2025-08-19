# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        bfs_log: list[list[int]] = []
        current_depth_nodes: list[TreeNode] = [root]
        depth: int = 0
        while len(current_depth_nodes) > 0:
            next_depth_nodes: list[TreeNode] = []
            bfs_log.append([])
            for i, node in enumerate(current_depth_nodes):
                if node is None:
                    continue
                bfs_log[depth].append(node.val)
                next_depth_nodes.append(node.left)
                next_depth_nodes.append(node.right)
            depth += 1
            current_depth_nodes = next_depth_nodes
            if len(current_depth_nodes) == 0:
                bfs_log.pop()
        return bfs_log

def examine()->None:
    root = make_tree([1, 2, 3, None, 4, 5, 6, 7])
    # root = make_tree([3,9,20,None,None,15,7])

    solution = Solution()
    output = solution.levelOrder(root)
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

