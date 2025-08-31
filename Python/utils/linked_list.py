from __future__ import annotations

import copy
from typing import Any


class ListNode:
    def __init__(self, val: Any, next:ListNode|None=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, nodes: list[Any]) -> ListNode|None:
        if 0 == len(nodes):
            return None
        head: ListNode = ListNode(nodes[0])
        tail: ListNode = head
        for node in nodes[1:]:
            tail.next = ListNode(node)
            tail = tail.next
        return head

    def to_list(self) -> list[Any]:
        nodes: list[Any] = []
        head: ListNode = copy.deepcopy(self)
        while head is not None:
            nodes.append(head.val)
            head = head.next
        return nodes

    def __repr__(self):
        return str(self.to_list())

    def __eq__(self, other):
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False
        return self.to_list() == other.to_list()