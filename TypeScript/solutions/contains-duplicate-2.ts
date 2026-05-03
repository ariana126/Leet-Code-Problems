// https://leetcode.com/problems/contains-duplicate-ii/
import { Examiner, Testcase } from '../utils';


function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const map = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i]!;
        if (!map.has(num)) { map.set(num, i); continue; }
        if (k >= i - map.get(num)!) return true;
        map.set(num, i);
    }
    return false;
}

export function examine(): void {
    new Examiner(containsNearbyDuplicate).run([
        new Testcase([[1, 2, 3, 1], 3], true),
        new Testcase([[1, 0, 1, 1], 1], true),
        new Testcase([[1, 2, 3, 1, 2, 3], 2], false),
    ]);
}
