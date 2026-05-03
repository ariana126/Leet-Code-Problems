export class ListNode {
    val: any;
    next: ListNode | null;

    constructor(val: any, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }

    static fromList(nodes: any[]): ListNode | null {
        if (nodes.length === 0) return null;
        const head = new ListNode(nodes[0]);
        let tail = head;
        for (let i = 1; i < nodes.length; i++) {
            tail.next = new ListNode(nodes[i]);
            tail = tail.next;
        }
        return head;
    }

    toList(): any[] {
        const nodes: any[] = [];
        let head: ListNode | null = this;
        while (head !== null) {
            nodes.push(head.val);
            head = head.next;
        }
        return nodes;
    }

    toString(): string {
        return JSON.stringify(this.toList());
    }

    equals(other: ListNode | null): boolean {
        if (other === null) return false;
        return JSON.stringify(this.toList()) === JSON.stringify(other.toList());
    }
}
