// https://leetcode.com/problems/3sum-closest/description/
import { Examiner, Testcase, Searcher, SearchQuery, Range, Element } from '../utils';


function threeSumClosest(nums: number[], target: number): number {
    nums.sort((a, b) => a - b);

    if (nums[0]! > 0 && target <= nums[0]!) return nums[0]! + nums[1]! + nums[2]!;
    if (nums[nums.length - 1]! < 0 && target <= nums[nums.length - 1]!) {
        return nums[nums.length - 1]! + nums[nums.length - 2]! + nums[nums.length - 3]!;
    }

    const searcher = Searcher.in_(nums);
    let minDiff = Infinity;
    let closestSum = 0;

    const zero = searcher.search(new SearchQuery(0));
    let pointers: [number, number];
    if (zero.hasFound()) {
        pointers = [zero.index, zero.index + 1];
    } else {
        let firstPointer = zero.nearestLeft;
        let secondPointer = zero.nearestRight;
        if (firstPointer.isOutOfRange()) {
            firstPointer = new Element(nums[0]!, 0);
            secondPointer = new Element(nums[1]!, 1);
        }
        if (secondPointer.isOutOfRange()) {
            firstPointer = new Element(nums[nums.length - 2]!, nums.length - 2);
            secondPointer = new Element(nums[nums.length - 1]!, nums.length - 1);
        }
        pointers = [firstPointer.index!, secondPointer.index!];
    }

    while (pointers[0] >= 0 && pointers[1] <= nums.length - 1) {
        const remainingValue = target - (nums[pointers[0]]! + nums[pointers[1]]!);
        let range: Range;
        if (remainingValue >= 0) {
            range = Range.startFrom(pointers[1] + 1);
        } else {
            range = Range.till(pointers[0] - 1);
        }
        if (pointers[0] === 0 && pointers[1] === nums.length - 1) {
            range = new Range(1, nums.length - 2);
        }

        const remainingResult = searcher.search(new SearchQuery(remainingValue, range));
        if (remainingResult.hasFound()) return target;
        const remaining = remainingResult.nearestTo(remainingValue);

        const sum = remaining.value! + (nums[pointers[0]]! + nums[pointers[1]]!);
        const diff = Math.abs(target - sum);
        if (minDiff > diff) { minDiff = diff; closestSum = sum; }

        if (pointers[0] === 0 && pointers[1] === nums.length - 1) break;
        if (target <= sum) {
            const s = pointers[0] - 1;
            if (s < 0) { pointers = [0, pointers[1] + 1]; continue; }
            pointers = [s, pointers[1]];
        } else {
            const e = pointers[1] + 1;
            if (e > nums.length - 1) { pointers = [pointers[0] - 1, nums.length - 1]; continue; }
            pointers = [pointers[0], e];
        }
    }
    return closestSum;
}

export function examine(): void {
    new Examiner(threeSumClosest).run([
        new Testcase([[1, 1, -1], 2], 1),
        new Testcase([[1, 1, 1, 1], 3], 3),
        new Testcase([[1, 1, 1, 0], -100], 2),
        new Testcase([[-100, -98, -2, -1], -101], -101),
        new Testcase([[-1, 2, 1, -4], 1], 2),
        new Testcase([[-100, -2, 1, 3, 25, 75], 0], 0),
        new Testcase([[102, 4, 3, -23, -73], 2], 6),
        new Testcase([[102, 4, 3, 2, 2, 2, -23, -73], 2], 6),
    ]);
}
