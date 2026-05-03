// https://leetcode.com/problems/power-of-four/description/
import { Examiner, Testcase } from '../utils';


function isPowerOfFour(n: number): boolean {
    if (n <= 0) return false;
    if (n === 1) return true;
    while (n > 1) {
        if (n % 4 !== 0) return false;
        n = Math.floor(n / 4);
    }
    return true;
}

export function examine(): void {
    new Examiner(isPowerOfFour).run([
        new Testcase([16], true),
        new Testcase([1], true),
        new Testcase([5], false),
    ]);
}
