# https://leetcode.com/problems/invert-binary-tree/description/
from utils.examination import Examiner, Testcase
from utils.tree import TreeNode


class Solution:
    def invertTree(self, root: TreeNode|None) -> TreeNode|None:
        if root is None:
            return None
        left: TreeNode|None = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        return root

def examine()->None:
    Examiner(Solution(), 'invertTree').run((
        Testcase((TreeNode.from_list([]),), TreeNode.from_list([])),
        Testcase((TreeNode.from_list([2,1,3]),), TreeNode.from_list([2,3,1])),
        Testcase((TreeNode.from_list([4,2,7,1,3,6,9]),), TreeNode.from_list([4,7,2,9,6,3,1])),
    ))