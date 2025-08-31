# https://leetcode.com/problems/remove-linked-list-elements/description/
import copy

from utils.examination import Examiner, Testcase
from utils.linked_list import ListNode


class Solution:
    def removeElements(self, head: ListNode|None, val: int) -> ListNode|None:
        head: ListNode|None = copy.deepcopy(head)
        if head is None:
            return None
        tail: ListNode = head
        while tail is not None and tail.next is not None:
            if val == tail.next.val:
                tail.next = tail.next.next
                continue
            tail = tail.next
        if val == head.val:
            head = head.next
        return head

def examine()->None:
    Examiner(Solution(), 'removeElements').run((
        Testcase((ListNode.from_list([1,2,6,3,4,5,6]), 6), ListNode.from_list([1,2,3,4,5])),
        Testcase((ListNode.from_list([7,7,7,7]), 7), ListNode.from_list([])),
        Testcase((ListNode.from_list([]), 7), ListNode.from_list([])),
    ))