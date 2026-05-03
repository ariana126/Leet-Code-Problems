// https://leetcode.com/problems/fibonacci-number/description/
import { Examiner, Testcase } from '../utils';


function fib(n: number): number {
    let one = 0, two = 1;
    for (let i = 0; i < n; i++) [one, two] = [two, one + two];
    return one;
}

export function examine(): void {
    new Examiner(fib).run([
        new Testcase([0], 0),
        new Testcase([1], 1),
        new Testcase([2], 1),
        new Testcase([3], 2),
        new Testcase([4], 3),
    ]);
}
