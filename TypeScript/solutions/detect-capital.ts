// https://leetcode.com/problems/detect-capital/description/
import { Examiner, Testcase } from '../utils';


function detectCapitalUse(word: string): boolean {
    if (word.length < 2) return true;
    if (word[0]! === word[0]!.toLowerCase() && word[1]! !== word[1]!.toLowerCase()) return false;
    const isLower = word[1]! === word[1]!.toLowerCase();
    for (let i = 2; i < word.length; i++) {
        if ((word[i]! === word[i]!.toLowerCase()) !== isLower) return false;
    }
    return true;
}

export function examine(): void {
    new Examiner(detectCapitalUse).run([
        new Testcase([''], true),
        new Testcase(['g'], true),
        new Testcase(['gg'], true),
        new Testcase(['G'], true),
        new Testcase(['USA'], true),
        new Testcase(['leetcode'], true),
        new Testcase(['Google'], true),
        new Testcase(['gG'], false),
        new Testcase(['FlaG'], false),
        new Testcase(['flaG'], false),
    ]);
}
