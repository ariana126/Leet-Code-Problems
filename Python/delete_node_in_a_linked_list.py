# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        while node.next is not None:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
                break
            node = node.next


def examine()->None:
    nodes: list[int] = [1, 2, 3, 4, 5]

    head: ListNode = ListNode(nodes[len(nodes)-1])
    for i in range(len(nodes) - 1, -1, -1):
        node: ListNode = ListNode(nodes[i])
        node.next = head
        head = node

    solution = Solution()
    solution.deleteNode(head)
    while head.next is not None:
        print(head.val)
        head = head.next
