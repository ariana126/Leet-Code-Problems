// https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
import { Examiner, Testcase } from '../utils';


function reverseWords(s: string): string {
    const arr = s.split('');
    let start = 0, end = 0;
    while (end <= arr.length) {
        if (end < arr.length && arr[end] !== ' ') { end++; continue; }
        let l = start, r = end - 1;
        while (l < r) {
            [arr[l], arr[r]] = [arr[r]!, arr[l]!];
            l++; r--;
        }
        end++;
        start = end;
    }
    return arr.join('');
}

export function examine(): void {
    new Examiner(reverseWords).run([
        new Testcase([''], ''),
        new Testcase(['ab'], 'ba'),
        new Testcase(['Mr Ding'], 'rM gniD'),
        new Testcase(["Let's take LeetCode contest"], "s'teL ekat edoCteeL tsetnoc"),
    ]);
}
