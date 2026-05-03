// https://leetcode.com/problems/is-subsequence/description/
import { Examiner, Testcase } from '../utils';


function isSubsequence(s: string, t: string): boolean {
    if (s.length > t.length) return false;
    let sI = 0, tI = 0;
    while (sI < s.length && tI < t.length) {
        if (s[sI] === t[tI]) sI++;
        tI++;
    }
    return sI >= s.length;
}

export function examine(): void {
    new Examiner(isSubsequence).run([
        new Testcase(['', ''], true),
        new Testcase(['A', 'c'], false),
        new Testcase(['abc', 'ahbgdc'], true),
        new Testcase(['axc', 'ahbgdc'], false),
    ]);
}
