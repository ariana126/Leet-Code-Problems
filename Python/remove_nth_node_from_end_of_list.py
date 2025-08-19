# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
# Definition for singly-linked list.
from debian.debtags import output


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        leader: ListNode = head
        follower: ListNode = head
        for i in range(n + 1):
            # print(i , leader. val, leader.next)
            if leader is None:
                if n == i:
                    return head.next
                else:
                    head.next = head.next.next
                    return head
            leader = leader.next

        while not leader is None:
            leader = leader.next
            follower = follower.next

        follower.next = follower.next.next

        return head

def examine()->None:
    nodes: list[int] = [1, 2, 3, 4, 5]

    head: ListNode = ListNode(nodes[len(nodes)-1])
    for i in range(len(nodes) - 2, -1, -1):
        head = ListNode(nodes[i], head)

    solution = Solution()
    head = solution.removeNthFromEnd(head, 5)
    while head is not None:
        print(head.val)
        head = head.next