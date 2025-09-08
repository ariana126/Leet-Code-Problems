# https://leetcode.com/problems/binary-tree-paths/description/
from utils.examination import Examiner, Testcase
from utils.tree import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode|None) -> list[str]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        leafs: list[str] = []
        if root.left is not None:
            leafs.extend(self.binaryTreePaths(root.left))
        if root.right is not None:
            leafs.extend(self.binaryTreePaths(root.right))
        paths: list[str] = []
        for path in leafs:
            paths.append(f'{root.val}->{path}')
        return paths

def examine()->None:
    Examiner(Solution(), 'binaryTreePaths').run((
        Testcase((TreeNode.from_list([1,2,3,None,5]),), ["1->2->5","1->3"]),
        Testcase((TreeNode.from_list([]),), []),
        Testcase((TreeNode.from_list([1]),), ['1']),
    ))