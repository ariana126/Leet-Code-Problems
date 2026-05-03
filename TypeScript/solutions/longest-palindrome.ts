// https://leetcode.com/problems/longest-palindrome/description/
import { Examiner, Testcase } from '../utils';


function longestPalindrome(s: string): number {
    if (s === '') return 0;
    const d = new Map<string, number>();
    let l = 0;
    for (const c of s) {
        const count = (d.get(c) ?? 0) + 1;
        d.set(c, count);
        if (count === 2) { l += 2; d.set(c, 0); }
    }
    for (const v of d.values()) { if (v >= 1) { l += 1; break; } }
    return l;
}

export function examine(): void {
    new Examiner(longestPalindrome).run([
        new Testcase([''], 0),
        new Testcase(['a'], 1),
        new Testcase(['abccccdd'], 7),
    ]);
}
