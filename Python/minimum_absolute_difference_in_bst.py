# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
from utils.examination import Examiner, Testcase, Logger
from utils.tree import TreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode|None) -> int:
        min_diff: int = float('inf')
        if root is None:
            return min_diff

        biggest_node_in_left: TreeNode|None = root.left
        while biggest_node_in_left is not None and biggest_node_in_left.right is not None:
            biggest_node_in_left = biggest_node_in_left.right
        if biggest_node_in_left is not None:
            min_diff = min(min_diff, abs(biggest_node_in_left.val - root.val))
            if 1 == min_diff:
                return 1

        smallest_node_in_right: TreeNode|None = root.right
        while smallest_node_in_right is not None and smallest_node_in_right.left is not None:
            smallest_node_in_right = smallest_node_in_right.left
        if smallest_node_in_right is not None:
            min_diff = min(min_diff, abs(smallest_node_in_right.val - root.val))
            if 1 == min_diff:
                return 1

        return min(min_diff, self.getMinimumDifference(root.left), self.getMinimumDifference(root.right))


def examine()->None:
    Examiner(Solution(), 'getMinimumDifference').run((
        Testcase((TreeNode.from_list([236,104,701,None,227,None,911]),), 9),
        Testcase((TreeNode.from_list([4,2,6,1,3]),), 1),
        Testcase((TreeNode.from_list([1,0,48,None,None,12,49]),), 1),
    ))