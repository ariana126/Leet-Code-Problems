# https://leetcode.com/problems/count-complete-tree-nodes/description/
from utils.examination import Examiner, Testcase, Logger
from utils.tree import TreeNode


class Solution:
    def countNodes(self, root: TreeNode|None) -> int:
        # Implement log(n) complexity
        return 0


    def countNodes2(self, root: TreeNode|None) -> int:
        if root is None:
            return 0
        if root.left is None:
            return 1
        count_: int = 1 + self.countNodes(root.left)
        if root.right is not None:
            count_ += self.countNodes(root.right)
        return count_

    def countNodes1(self, root: TreeNode|None) -> int:
        if root is None:
            return 0
        h: int = 0
        current: list[TreeNode] = [root]
        next_: list[TreeNode] = []
        while current[-1] is not None:
            for node in current:
                next_.append(node.left)
                next_.append(node.right)
            current = next_
            next_ = []
            h += 1
        count: int = 0
        for i in range(h + 1):
            count += 2 ** i
        Logger.log(count, h, current)
        for i in range(len(current) - 1, -1, -1):
            if current[i] is not None:
                break
            count -= 1
        return count

def examine()->None:
    Examiner(Solution(), 'countNodes').run((
        Testcase((TreeNode.from_list([1, 2, 3, 4, 5, 6]),), 6),
        Testcase((TreeNode.from_list([]),), 0),
        Testcase((TreeNode.from_list([1]),), 1),
    ))