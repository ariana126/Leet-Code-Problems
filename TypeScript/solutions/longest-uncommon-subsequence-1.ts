// https://leetcode.com/problems/longest-uncommon-subsequence-i/description/
import { Examiner, Testcase } from '../utils';


function findLUSlength(a: string, b: string): number {
    if (a === b) return -1;
    return Math.max(a.length, b.length);
}

export function examine(): void {
    new Examiner(findLUSlength).run([
        new Testcase(['aba', 'cdc'], 3),
        new Testcase(['aaa', 'bbb'], 3),
        new Testcase(['aac', 'bbc'], 3),
        new Testcase(['aca', 'bcb'], 3),
        new Testcase(['aaa', 'a'], 3),
        new Testcase(['aaa', 'aaa'], -1),
    ]);
}
