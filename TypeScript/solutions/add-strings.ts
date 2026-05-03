// https://leetcode.com/problems/add-strings/description/
import { Examiner, Testcase } from '../utils';


function addStrings(num1: string, num2: string): string {
    let num1I = num1.length - 1;
    let num2I = num2.length - 1;
    let p = 0;
    let sum = '';
    while (num1I >= 0 || num2I >= 0) {
        const n1 = num1I >= 0 ? num1.charCodeAt(num1I) - '0'.charCodeAt(0) : 0;
        const n2 = num2I >= 0 ? num2.charCodeAt(num2I) - '0'.charCodeAt(0) : 0;
        let s = n1 + n2 + p;
        if (s >= 10) {
            p = 1;
            s -= 10;
        } else {
            p = 0;
        }
        sum = String.fromCharCode(s + '0'.charCodeAt(0)) + sum;
        num1I--;
        num2I--;
    }
    if (p > 0) sum = String.fromCharCode(p + '0'.charCodeAt(0)) + sum;
    return sum;
}

export function examine(): void {
    new Examiner(addStrings).run([
        new Testcase(['11', '123'], '134'),
        new Testcase(['456', '77'], '533'),
        new Testcase(['0', '0'], '0'),
        new Testcase(['32', '0'], '32'),
        new Testcase(['999', '1'], '1000'),
    ]);
}