// https://leetcode.com/problems/reverse-string-ii/
import { Examiner, Testcase } from '../utils';


function reverseStr(s: string, k: number): string {
    let i = 0;
    let arr = s.split('');
    while (true) {
        let start = 2 * k * i;
        if (start >= arr.length) break;
        let end = Math.min(start + k - 1, arr.length - 1);
        while (start < end) {
            [arr[start], arr[end]] = [arr[end]!, arr[start]!];
            start++;
            end--;
        }
        i++;
    }
    return arr.join('');
}

export function examine(): void {
    new Examiner(reverseStr).run([
        new Testcase(['abcdefg', 2], 'bacdfeg'),
        new Testcase(['abcd', 2], 'bacd'),
        new Testcase(['a', 2], 'a'),
        new Testcase(['a', 200], 'a'),
    ]);
}
