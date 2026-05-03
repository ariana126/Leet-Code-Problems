// https://leetcode.com/problems/lru-cache/description/
import { DesignExaminer, DesignTestcase } from '../utils';


class CacheNode {
    key: number; value: number;
    left: CacheNode | null = null;
    right: CacheNode | null = null;
    constructor(key: number, value: number) { this.key = key; this.value = value; }
    setRight(node: CacheNode | null): void { this.right = node; if (node) node.left = this; }
    unlinkRight(): void { if (this.right) this.right.left = null; this.right = null; }
    setLeft(node: CacheNode | null): void { this.left = node; if (node) node.right = this; }
    unlinkLeft(): void { if (this.left) this.left.right = null; this.left = null; }
    isEqual(node: CacheNode | null): boolean { return node !== null && this.key === node.key; }
}

class LRUCache {
    private capacity: number;
    private cache = new Map<number, CacheNode>();
    private head: CacheNode | null = null;
    private tail: CacheNode | null = null;
    constructor(capacity: number) { this.capacity = capacity; }

    get(key: number): number {
        if (!this.cache.has(key)) return -1;
        const node = this.cache.get(key)!;
        this.updateRank(node);
        return node.value;
    }

    put(key: number, value: number): void {
        if (this.cache.has(key)) {
            const node = this.cache.get(key)!;
            node.value = value;
            this.updateRank(node);
            return;
        }
        const node = new CacheNode(key, value);
        if (this.capacity === this.cache.size) {
            const headKey = this.head!.key;
            this.popHead();
            this.cache.delete(headKey);
        }
        this.insertTail(node);
        this.cache.set(key, node);
    }

    private popHead(): void {
        if (this.head!.isEqual(this.tail)) { this.head = null; this.tail = null; return; }
        this.head = this.head!.right;
        this.head!.unlinkLeft();
    }

    private setTail(node: CacheNode): void {
        this.tail!.setRight(node);
        this.tail = node;
        this.tail.unlinkRight();
    }

    private insertTail(node: CacheNode): void {
        if (this.head === null) { this.head = node; this.tail = node; return; }
        this.setTail(node);
    }

    private updateRank(node: CacheNode): void {
        if (this.tail!.isEqual(node)) return;
        if (this.head!.isEqual(node)) { this.popHead(); this.setTail(node); return; }
        const right = node.right!;
        node.unlinkRight();
        const left = node.left!;
        node.unlinkLeft();
        left.setRight(right);
        this.setTail(node);
    }
}

export function examine(): void {
    new DesignExaminer(LRUCache).run([
        new DesignTestcase(
            ['LRUCache', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get'],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [null, null, null, 1, null, -1, null, -1, 3, 4],
        ),
        new DesignTestcase(
            ['LRUCache', 'put', 'get', 'put', 'get', 'get'],
            [[1], [2, 1], [2], [3, 2], [2], [3]],
            [null, null, 1, null, -1, 2],
        ),
    ]);
}
