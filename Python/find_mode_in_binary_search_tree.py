# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
from utils.examination import Examiner, Testcase
from utils.tree import TreeNode


class Solution:
    def findMode(self, root: TreeNode|None) -> list[int]:
        return []

def examine() -> None:
    Examiner(Solution(), 'findMode').run((
        Testcase((TreeNode.from_list([1,None,2,2]),), [2]),
        Testcase((TreeNode.from_list([0]),), [0]),
    ))