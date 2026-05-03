// https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
import { DesignExaminer, DesignTestcase } from '../utils';


class KthLargest {
    private scores: number[];
    private k: number;
    constructor(k: number, nums: number[]) {
        this.scores = [...nums].sort((a, b) => a - b);
        this.k = k;
    }
    add(val: number): number {
        this.scores.push(val);
        this.scores.sort((a, b) => a - b);
        return this.scores[this.scores.length - this.k]!;
    }
}

export function examine(): void {
    new DesignExaminer(KthLargest).run([
        new DesignTestcase(
            ['KthLargest', 'add', 'add', 'add', 'add', 'add'],
            [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            [null, 4, 5, 5, 8, 8],
        ),
        new DesignTestcase(
            ['KthLargest', 'add', 'add', 'add', 'add'],
            [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]],
            [null, 7, 7, 7, 8],
        ),
    ]);
}
