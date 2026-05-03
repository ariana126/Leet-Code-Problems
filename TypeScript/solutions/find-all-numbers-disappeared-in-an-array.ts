// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
import { Examiner, Testcase } from '../utils';


function findDisappearedNumbers(nums: number[]): number[] {
    const appeared = new Set(nums);
    const result: number[] = [];
    for (let i = 1; i <= nums.length; i++) {
        if (!appeared.has(i)) result.push(i);
    }
    return result;
}

export function examine(): void {
    new Examiner(findDisappearedNumbers).run([
        new Testcase([[4, 3, 2, 7, 8, 2, 3, 1]], [5, 6]),
        new Testcase([[1, 1]], [2]),
    ]);
}
