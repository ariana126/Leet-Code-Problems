from __future__ import annotations
from typing import Any

class TreeNode:
    def __init__(self, val: Any, left:TreeNode|None=None, right:TreeNode|None=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, nodes: list[Any]) -> TreeNode|None:
        if 0 == len(nodes):
            return None
        root: TreeNode = TreeNode(nodes[0])
        current_depth: list[TreeNode] = [root]
        next_depth: list[TreeNode] = []
        i: int = 1
        while len(nodes) > i:
            for node in current_depth:
                if len(nodes) > i and nodes[i] is not None:
                    node.left = TreeNode(nodes[i])
                    next_depth.append(node.left)
                if len(nodes) > i + 1 and nodes[i + 1] is not None:
                    node.right = TreeNode(nodes[i + 1])
                    next_depth.append(node.right)
                i += 2
            current_depth = next_depth
            next_depth = []
        return root

    def to_list(self) -> list[Any]:
        nodes: list[Any] = [self.val]
        current_depth: list[TreeNode] = [self]
        next_depth: list[TreeNode] = []
        while 0 != len(current_depth):
            for node in current_depth:
                if node.left is not None:
                    nodes.append(node.left.val)
                    next_depth.append(node.left)
                else:
                    nodes.append(None)
                if node.right is not None:
                    nodes.append(node.right.val)
                    next_depth.append(node.right)
                else:
                    nodes.append(None)
            current_depth = next_depth
            next_depth = []
        i: int = len(nodes) - 1
        while nodes[i] is None:
            i -= 1
        return nodes[0:i+1]

    def __eq__(self, other):
        # TODO: Implement a better way
        if self is None and other is None:
            return True
        if self is None or other is None:
            return False
        return self.to_list() == other.to_list()

    def __repr__(self):
        return str(self.to_list())