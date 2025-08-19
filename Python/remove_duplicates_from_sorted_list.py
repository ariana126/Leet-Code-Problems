# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from debian.debtags import output


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        unique_list: ListNode = ListNode(head.val)
        unique_list_head: ListNode = unique_list
        while head is not None:
            if unique_list.val < head.val:
                unique_list.next = ListNode(head.val)
                unique_list = unique_list.next
            head = head.next
        return unique_list_head

def examine()->None:
    head: ListNode = make_linked_list([1, 1, 2, 2, 2, 4, 10, 10])
    output = Solution().deleteDuplicates(head)
    while output is not None:
        print(output.val)
        output = output.next


def make_linked_list(nodes: list[int]) -> ListNode:
    head: ListNode = ListNode(nodes[len(nodes)-1])
    for i in range(len(nodes) - 2, -1, -1):
        t = head
        head = ListNode(nodes[i])
        head.next = t

    return head