// https://leetcode.com/problems/reverse-vowels-of-a-string/
import { Examiner, Testcase } from '../utils';


function reverseVowels(s: string): string {
    const isVowel = (c: string) => 'aeiouAEIOU'.includes(c);
    const vowelIndexes: number[] = [];
    for (let i = 0; i < s.length; i++) if (isVowel(s[i]!)) vowelIndexes.push(i);
    const arr = s.split('');
    let start = 0, end = vowelIndexes.length - 1;
    while (start < end) {
        [arr[vowelIndexes[start]!], arr[vowelIndexes[end]!]] = [arr[vowelIndexes[end]!]!, arr[vowelIndexes[start]!]!];
        start++; end--;
    }
    return arr.join('');
}

export function examine(): void {
    new Examiner(reverseVowels).run([
        new Testcase(['IceCreAm'], 'AceCreIm'),
        new Testcase(['AceCreIm'], 'IceCreAm'),
        new Testcase(['leetcode'], 'leotcede'),
        new Testcase(['leotcede'], 'leetcode'),
        new Testcase([''], ''),
    ]);
}
