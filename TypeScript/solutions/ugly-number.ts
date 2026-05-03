// https://leetcode.com/problems/ugly-number/description/
import { Examiner, Testcase } from '../utils';


function isUgly(n: number): boolean {
    if (n <= 0) return false;
    while (n > 1) {
        if (n % 2 === 0) { n = Math.floor(n / 2); continue; }
        if (n % 3 === 0) { n = Math.floor(n / 3); continue; }
        if (n % 5 === 0) { n = Math.floor(n / 5); continue; }
        return false;
    }
    return true;
}

export function examine(): void {
    new Examiner(isUgly).run([
        new Testcase([6], true),
        new Testcase([1], true),
        new Testcase([14], false),
    ]);
}
