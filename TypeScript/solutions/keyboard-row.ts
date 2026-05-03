// https://leetcode.com/problems/keyboard-row/description/
import { Examiner, Testcase } from '../utils';


function findWords(words: string[]): string[] {
    const rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'].map(r => new Set(r));
    return words.filter(word =>
        rows.some(row => word.split('').every(c => row.has(c.toLowerCase())))
    );
}

export function examine(): void {
    new Examiner(findWords).run([
        new Testcase([['Hello', 'Alaska', 'Dad', 'Peace']], ['Alaska', 'Dad']),
        new Testcase([['omk']], []),
        new Testcase([['adsdf', 'sfd']], ['adsdf', 'sfd']),
    ]);
}
