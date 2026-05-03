// https://leetcode.com/problems/third-maximum-number/description/
import { Examiner, Testcase } from '../utils';


function thirdMax(nums: number[]): number {
    if (nums.length === 1) return nums[0]!;
    if (nums.length === 2) return Math.max(nums[0]!, nums[1]!);
    const MIN = -(2 ** 31) - 1;
    let tops = [MIN, MIN, MIN];
    for (const num of nums) {
        if (num <= tops[0]!) continue;
        if (num < tops[1]!) { tops[0] = num; continue; }
        if (num === tops[1]) continue;
        if (num < tops[2]!) { tops[0] = tops[1]!; tops[1] = num; continue; }
        if (num === tops[2]) continue;
        tops[0] = tops[1]!; tops[1] = tops[2]!; tops[2] = num;
    }
    return tops[0] === MIN ? tops[2]! : tops[0]!;
}

export function examine(): void {
    new Examiner(thirdMax).run([
        new Testcase([[2, 3, 1]], 1),
        new Testcase([[2, 1]], 2),
        new Testcase([[1, 1, 2]], 2),
        new Testcase([[2, 1, 2, 3]], 1),
    ]);
}
