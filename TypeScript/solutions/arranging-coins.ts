// https://leetcode.com/problems/arranging-coins/description/
import { Examiner, Testcase } from '../utils';


function arrangeCoins(n: number): number {
    let t = 0;
    for (let i = 1; i <= n; i++) {
        t += i;
        if (t > n) return i - 1;
        if (t === n) return i;
    }
    return 0;
}

export function examine(): void {
    new Examiner(arrangeCoins).run([
        new Testcase([1], 1),
        new Testcase([2], 1),
        new Testcase([5], 2),
        new Testcase([6], 3),
        new Testcase([8], 3),
        new Testcase([10], 4),
    ]);
}