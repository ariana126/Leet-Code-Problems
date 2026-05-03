// https://leetcode.com/problems/power-of-two/description/
import { Examiner, Testcase } from '../utils';


function isPowerOfTwo(n: number): boolean {
    if (n <= 0) return false;
    while (n > 1) {
        if (n % 2 === 1) return false;
        n = Math.floor(n / 2);
    }
    return true;
}

export function examine(): void {
    new Examiner(isPowerOfTwo).run([
        new Testcase([1], true),
        new Testcase([16], true),
        new Testcase([3], false),
    ]);
}
