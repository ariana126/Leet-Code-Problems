// https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

import {Examiner, Logger, Testcase} from "../utils";

function findLengthOfLCIS(nums: number[]): number {
    let LCIS: number = 1;
    let currentLCIS: number = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i]! > nums[i - 1]!) {
            currentLCIS ++;
        } else {
            LCIS = Math.max(LCIS, currentLCIS);
            currentLCIS = 1;
        }
    }
    return Math.max(LCIS, currentLCIS);
}

export function examine(): void {
    new Examiner(findLengthOfLCIS).run([
        new Testcase([[1,3,5,4,7]], 3),
        new Testcase([[2,2,2,2,2]], 1),
        new Testcase([[2]], 1),
    ]);
}