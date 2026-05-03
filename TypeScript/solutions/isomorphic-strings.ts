// https://leetcode.com/problems/isomorphic-strings/description/
import { Examiner, Testcase } from '../utils';


function isIsomorphic(s: string, t: string): boolean {
    if (s.length !== t.length) return false;
    const sToT = new Map<string, string>();
    const tToS = new Map<string, string>();
    for (let i = 0; i < s.length; i++) {
        const sc = s[i]!, tc = t[i]!;
        if (!sToT.has(sc) && !tToS.has(tc)) { sToT.set(sc, tc); tToS.set(tc, sc); }
        if (!sToT.has(sc) || !tToS.has(tc)) return false;
        if (sc !== tToS.get(tc)!) return false;
    }
    return true;
}

export function examine(): void {
    new Examiner(isIsomorphic).run([
        new Testcase(['paper', 'title'], true),
        new Testcase(['egg', 'add'], true),
        new Testcase(['egg', 'adda'], false),
        new Testcase(['egg', 'addb'], false),
        new Testcase(['egg', 'ad'], false),
        new Testcase(['eg', 'add'], false),
        new Testcase(['ege', 'add'], false),
        new Testcase(['eggp', 'add'], false),
    ]);
}
