// https://leetcode.com/problems/design-hashmap/description/
import { DesignExaminer, DesignTestcase } from '../utils';


class MyHashMap {
    private readonly bucketsSize = 10 ** 3;
    private storage: (number | null)[][] = [];

    put(key: number, value: number): void {
        const sec = this.sec(key);
        while (sec >= this.storage.length) this.storage.push([]);
        const idx = this.idx(key);
        while (idx >= this.storage[sec]!.length) this.storage[sec]!.push(null);
        this.storage[sec]![idx] = value;
    }

    get(key: number): number {
        const sec = this.sec(key), idx = this.idx(key);
        if (sec >= this.storage.length || idx >= this.storage[sec]!.length) return -1;
        const val = this.storage[sec]![idx];
        return val == null ? -1 : val;
    }

    remove(key: number): void {
        const sec = this.sec(key), idx = this.idx(key);
        if (sec >= this.storage.length || idx >= this.storage[sec]!.length) return;
        this.storage[sec]![idx] = null;
    }

    private idx(key: number): number { return key % this.bucketsSize; }
    private sec(key: number): number { return (key - this.idx(key)) / this.bucketsSize; }
}

export function examine(): void {
    new DesignExaminer(MyHashMap).run([
        new DesignTestcase(
            ['MyHashMap', 'put', 'put', 'get', 'get', 'put', 'get', 'remove', 'get'],
            [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]],
            [null, null, null, 1, -1, null, 1, null, -1],
        ),
    ]);
}
