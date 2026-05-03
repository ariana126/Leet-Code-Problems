// https://leetcode.com/problems/repeated-substring-pattern/description/
import { Examiner, Testcase } from '../utils';


function repeatedSubstringPattern(s: string): boolean {
    const l = s.length;
    if ((l & 1) === 0 && s.slice(0, l / 2) === s.slice(l / 2)) return true;

    let i = l % 2 === 1 ? 1 : 0;
    let left = Math.floor((l - i) / 2);
    let right = left + i;
    while (left >= 1) {
        if (s.slice(0, left) === s.slice(right) && s.slice(left, right) === s.slice(0, i) && s.slice(0, i) === s.slice(-i || l))
            return true;
        i += 2;
        left = Math.floor((l - i) / 2);
        right = left + i;
    }
    return false;
}

export function examine(): void {
    new Examiner(repeatedSubstringPattern).run([
        new Testcase(['babba'], false),
        new Testcase(['ababab'], true),
        new Testcase(['abaaaabaaaabaaa'], true),
        new Testcase(['aaa'], true),
        new Testcase(['abab'], true),
        new Testcase(['aba'], false),
        new Testcase(['abcabcabcabc'], true),
        new Testcase(['a'], false),
        new Testcase(['abaababaab'], true),
    ]);
}
