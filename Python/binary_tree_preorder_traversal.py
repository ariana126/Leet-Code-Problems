from utils.examination import Examiner, Testcase
from utils.tree import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode|None) -> list[int]:
        if root is None:
            return []
        traversal: list[int] = [root.val]
        traversal.extend(self.preorderTraversal(root.left))
        traversal.extend(self.preorderTraversal(root.right))
        return traversal

def examine()->None:
    Examiner(Solution(), 'preorderTraversal').run((
        Testcase((TreeNode.from_list([1,None,2,3]),), [1,2,3]),
        Testcase((TreeNode.from_list([]),), []),
        Testcase((TreeNode.from_list([1]),), [1]),
        Testcase((TreeNode.from_list([1,2,3,4,5,None,8,None,None,6,7,9]),), [1,2,4,5,6,7,3,8,9]),
    ))