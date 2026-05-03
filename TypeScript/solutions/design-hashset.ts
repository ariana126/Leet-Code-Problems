// https://leetcode.com/problems/design-hashset/description/
import { DesignExaminer, DesignTestcase } from '../utils';


class MyHashSet {
    private hashTable = new Map<number, null>();
    add(key: number): void { this.hashTable.set(key, null); }
    remove(key: number): void { this.hashTable.delete(key); }
    contains(key: number): boolean { return this.hashTable.has(key); }
}

export function examine(): void {
    new DesignExaminer(MyHashSet).run([
        new DesignTestcase(
            ['MyHashSet', 'add', 'add', 'contains', 'contains', 'add', 'contains', 'remove', 'contains'],
            [[], [1], [2], [1], [3], [2], [2], [2], [2]],
            [null, null, null, true, false, null, true, null, false],
        ),
        new DesignTestcase(
            ['MyHashSet', 'add', 'remove', 'add', 'remove', 'remove', 'add', 'add', 'add', 'add', 'remove'],
            [[], [9], [19], [14], [19], [9], [0], [3], [4], [0], [9]],
            [null, null, null, null, null, null, null, null, null, null, null],
        ),
    ]);
}
