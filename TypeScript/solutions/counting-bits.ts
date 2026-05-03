// https://leetcode.com/problems/counting-bits/description/
import { Examiner, Testcase } from '../utils';


function countBits(n: number): number[] {
    const bits: number[] = [0];
    while (n + 1 > bits.length) {
        const l = bits.length;
        let i = 0;
        while (n + 1 > bits.length && l > i) {
            bits.push(1 + bits[i]!);
            i++;
        }
    }
    return bits;
}

export function examine(): void {
    new Examiner(countBits).run([
        new Testcase([2], [0, 1, 1]),
        new Testcase([5], [0, 1, 1, 2, 1, 2]),
        new Testcase([20], [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2]),
    ]);
}
