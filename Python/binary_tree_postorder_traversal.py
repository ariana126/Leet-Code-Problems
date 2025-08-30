# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
from utils.examination import Examiner, Testcase
from utils.tree import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode|None) -> list[int]:
        if root is None:
            return []
        traversal: list[int] = []
        traversal.extend(self.postorderTraversal(root.left))
        traversal.extend(self.postorderTraversal(root.right))
        traversal.append(root.val)
        return traversal

def examine()->None:
    Examiner(Solution(), 'postorderTraversal').run((
        Testcase((TreeNode.from_list([1,None,2,3]),), [3, 2, 1]),
        Testcase((TreeNode.from_list([]),), []),
        Testcase((TreeNode.from_list([1]),), [1]),
        Testcase((TreeNode.from_list([1,2,3,4,5,None,8,None,None,6,7,9]),), [4,6,7,5,2,9,8,3,1]),
    ))