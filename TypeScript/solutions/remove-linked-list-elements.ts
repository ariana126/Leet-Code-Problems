// https://leetcode.com/problems/remove-linked-list-elements/description/
import { Examiner, Testcase, ListNode } from '../utils';


function removeElements(head: ListNode | null, val: number): ListNode | null {
    if (head === null) return null;
    let tail: ListNode | null = head;
    while (tail !== null && tail.next !== null) {
        if (val === tail.next.val) { tail.next = tail.next.next; continue; }
        tail = tail.next;
    }
    if (val === head.val) head = head.next;
    return head;
}

export function examine(): void {
    new Examiner(removeElements).run([
        new Testcase([ListNode.fromList([1, 2, 6, 3, 4, 5, 6]), 6], ListNode.fromList([1, 2, 3, 4, 5])),
        new Testcase([ListNode.fromList([7, 7, 7, 7]), 7], null),
        new Testcase([null, 7], null),
    ]);
}
