// https://leetcode.com/problems/intersection-of-two-arrays/description/
import { Examiner, Testcase } from '../utils';


function intersection(nums1: number[], nums2: number[]): number[] {
    const seen = new Set(nums1);
    const seen2 = new Set<number>();
    const result: number[] = [];
    for (const num of nums2) {
        if (seen.has(num) && !seen2.has(num)) { seen2.add(num); result.push(num); }
    }
    return result;
}

export function examine(): void {
    new Examiner(intersection).run([
        new Testcase([[], []], []),
        new Testcase([[1, 2, 2, 1], [2, 2]], [2]),
        new Testcase([[4, 9, 5], [9, 4, 9, 8, 4]], [9, 4]),
    ]);
}
