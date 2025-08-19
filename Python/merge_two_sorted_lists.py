# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        merged: ListNode = ListNode(-10000)
        head = merged
        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    merged.next = ListNode(list1.val)
                    merged = merged.next
                    list1 = list1.next
                else:
                    merged.next = ListNode(list2.val)
                    merged = merged.next
                    list2 = list2.next
            if list1 is None and list2 is not None:
                merged.next = ListNode(list2.val)
                merged = merged.next
                list2 = list2.next
            if list2 is None and list1 is not None:
                merged.next = ListNode(list1.val)
                merged = merged.next
                list1 = list1.next
        return head.next

def examine()-> None:
    list1: ListNode | None = make_linked_list([1, 2, 4])
    list2: ListNode | None = make_linked_list([1, 3, 4])

    solution = Solution()
    output: ListNode = solution.mergeTwoLists(list1, list2)
    while output is not None:
        print(output.val)
        output = output.next

def make_linked_list(nodes: list[int]) -> ListNode:
    head: ListNode = ListNode(nodes[len(nodes)-1])
    for i in range(len(nodes) - 2, -1, -1):
        head = ListNode(nodes[i], head)
    return head