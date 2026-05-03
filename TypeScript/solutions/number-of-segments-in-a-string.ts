// https://leetcode.com/problems/number-of-segments-in-a-string/description/
import { Examiner, Testcase } from '../utils';


function countSegments(s: string): number {
    let count = 0, started = false;
    for (const c of s) {
        if (c === ' ') { if (started) { count++; started = false; } }
        else started = true;
    }
    if (started) count++;
    return count;
}

export function examine(): void {
    new Examiner(countSegments).run([
        new Testcase(['Hello, my name is John'], 5),
        new Testcase([' Hello, my name is John'], 5),
        new Testcase(['Hello,'], 1),
        new Testcase([''], 0),
        new Testcase(['  '], 0),
        new Testcase([' Hello, '], 1),
    ]);
}
