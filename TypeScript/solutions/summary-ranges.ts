// https://leetcode.com/problems/summary-ranges/
import { Examiner, Testcase } from '../utils';


function summaryRanges(nums: number[]): string[] {
    if (nums.length === 0) return [];
    const summary: string[] = [];
    let a = 0, b = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[b]! === nums[i]! - 1) { b++; continue; }
        summary.push(a === b ? String(nums[a]!) : `${nums[a]}->${nums[b]}`);
        b++;
        a = b;
    }
    summary.push(a === b ? String(nums[a]!) : `${nums[a]}->${nums[b]}`);
    return summary;
}

export function examine(): void {
    new Examiner(summaryRanges).run([
        new Testcase([[0, 1, 2, 4, 5, 7]], ['0->2', '4->5', '7']),
        new Testcase([[0, 2, 3, 4, 6, 8, 9]], ['0', '2->4', '6', '8->9']),
    ]);
}
