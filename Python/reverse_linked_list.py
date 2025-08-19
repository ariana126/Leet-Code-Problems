# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev: ListNode | None = None
        while head is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        leaf: ListNode = head
        pre_leaf: ListNode = head
        while leaf.next is not None:
            if leaf.next.next is None:
                pre_leaf.next = leaf
            leaf = leaf.next

        pre_leaf.next = None
        return ListNode(leaf.val, self.reverseList(head))

    def reverseList1(self, head: ListNode) -> ListNode:
        reversed_list: ListNode | None = None
        while head is not None:
            reversed_list = ListNode(head.val, reversed_list)
            head = head.next
        return reversed_list

def examine()->None:
    nodes: list[int] = [1, 2, 3, 4, 5]

    head: ListNode = ListNode(nodes[len(nodes)-1])
    for i in range(len(nodes) - 2, -1, -1):
        head = ListNode(nodes[i], head)

    solution = Solution()
    head = solution.reverseList(head)
    while head is not None:
        print(head.val)
        head = head.next
