// https://leetcode.com/problems/perfect-number/
import { Examiner, Testcase } from '../utils';


function checkPerfectNumber(num: number): boolean {
    if (num === 1) return false;
    let i = 2, max = num, sum = 1;
    while (max > i) {
        if (num % i === 0) {
            sum += i + Math.floor(num / i);
            if (sum > num) return false;
            max = Math.floor(num / i);
        }
        i++;
    }
    return sum === num;
}

export function examine(): void {
    new Examiner(checkPerfectNumber).run([
        new Testcase([28], true),
        new Testcase([1], false),
        new Testcase([2], false),
        new Testcase([7], false),
    ]);
}
