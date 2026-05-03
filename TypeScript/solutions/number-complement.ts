// https://leetcode.com/problems/number-complement/description/
import { Examiner, Testcase } from '../utils';


function findComplement(num: number): number {
    let b = 0, i = 0, p = 0;
    while (num >= p) { b += p; p = 2 ** i; i++; }
    return num ^ b;
}

export function examine(): void {
    new Examiner(findComplement).run([
        new Testcase([5], 2),
        new Testcase([1], 0),
    ]);
}
