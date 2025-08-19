# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length: int = 0
        iterator: ListNode = head
        while iterator is not None:
            length += 1
            iterator = iterator.next

        mid: ListNode = head
        for i in range(int((length - (length % 2)) / 2)):
            mid = mid.next

        if 1 & length:
            mid = mid.next
        mid = self.reverseList(mid)
        while mid is not None:
            if mid.val != head.val:
                return False
            head = head.next
            mid = mid.next
        return True

    def reverseList(self, head: ListNode) -> ListNode:
        prev: ListNode | None = None
        while head is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

def examine()-> None:
    input_: ListNode = make_linked_list([])

    solution = Solution()
    output: bool = solution.isPalindrome(input_)
    print(output)

def make_linked_list(nodes: list[int]) -> ListNode:
    head: ListNode = ListNode(nodes[len(nodes)-1])
    for i in range(len(nodes) - 2, -1, -1):
        head = ListNode(nodes[i], head)
    return head