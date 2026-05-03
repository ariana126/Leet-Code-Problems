// https://leetcode.com/problems/next-greater-element-i/
import { Examiner, Testcase } from '../utils';


function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    if (nums1.length === 0 || nums2.length === 0) return [];
    const greater = new Map<number, number>();
    const stack: number[] = [];
    for (const num of nums2) {
        while (stack.length > 0 && num > stack[stack.length - 1]!) greater.set(stack.pop()!, num);
        stack.push(num);
    }
    for (const num of stack) greater.set(num, -1);
    return nums1.map(num => greater.get(num)!);
}

export function examine(): void {
    new Examiner(nextGreaterElement).run([
        new Testcase([[4, 1, 2], [1, 3, 4, 2]], [-1, 3, -1]),
        new Testcase([[2, 4], [1, 2, 3, 4]], [3, -1]),
    ]);
}
