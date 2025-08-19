# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if 0 == len(nums):
            return None
        mid_index = len(nums) // 2
        root: TreeNode = TreeNode(nums[mid_index])
        root.left = self.sortedArrayToBST(nums[:mid_index])
        root.right = self.sortedArrayToBST(nums[mid_index + 1:])
        return root

def examine()->None:
    # nums = [1, 2, 3, 4, 5]
    nums = [-10,-3,0,5,9]
    root = Solution().sortedArrayToBST(nums)
    print_tree(root)

def print_tree(root: TreeNode)-> None:
    if root is None:
        return

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

    for i, depth in enumerate(bfs_log):
        print(depth)