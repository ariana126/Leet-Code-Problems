// https://leetcode.com/problems/valid-perfect-square/description/
import { Examiner, Testcase } from '../utils';


function isPerfectSquare(num: number): boolean {
    if (num === 1) return true;
    let start = 1, end = Math.floor(num / 2);
    while (start <= end) {
        const mid = Math.floor((start + end) / 2);
        const square = mid * mid;
        if (num === square) return true;
        if (num > square) start = mid + 1;
        else end = mid - 1;
    }
    return false;
}

export function examine(): void {
    new Examiner(isPerfectSquare).run([
        new Testcase([1], true),
        new Testcase([4], true),
        new Testcase([9], true),
        new Testcase([16], true),
        new Testcase([1849], true),
        new Testcase([2], false),
        new Testcase([10], false),
        new Testcase([43], false),
    ]);
}
