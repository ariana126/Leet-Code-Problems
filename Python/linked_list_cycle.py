# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        fast: ListNode = head
        slow: ListNode = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

def examine()->None:
    input_: ListNode = make_linked_list([1, 2, 3, 4])
    t: ListNode = input_
    while t.next is not None:
        t = t.next
    t.next = input_
    input_ = t

    solution = Solution()
    output = solution.hasCycle(input_)
    print(output)

def make_linked_list(nodes: list[int]) -> ListNode:
    head: ListNode = ListNode(nodes[len(nodes)-1])
    for i in range(len(nodes) - 2, -1, -1):
        t = head
        head = ListNode(nodes[i])
        head.next = t

    return head