// https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
import { Examiner, Testcase, TreeNode } from '../utils';


function getMinimumDifference(root: TreeNode | null): number {
    let minDiff = Infinity;
    if (root === null) return minDiff;

    let biggestInLeft = root.left;
    while (biggestInLeft?.right !== null && biggestInLeft !== null) biggestInLeft = biggestInLeft.right;
    if (biggestInLeft !== null) {
        minDiff = Math.min(minDiff, Math.abs(biggestInLeft.val - root.val));
        if (minDiff === 1) return 1;
    }

    let smallestInRight = root.right;
    while (smallestInRight?.left !== null && smallestInRight !== null) smallestInRight = smallestInRight.left;
    if (smallestInRight !== null) {
        minDiff = Math.min(minDiff, Math.abs(smallestInRight.val - root.val));
        if (minDiff === 1) return 1;
    }

    return Math.min(minDiff, getMinimumDifference(root.left), getMinimumDifference(root.right));
}

export function examine(): void {
    new Examiner(getMinimumDifference).run([
        new Testcase([TreeNode.fromList([236, 104, 701, null, 227, null, 911])], 9),
        new Testcase([TreeNode.fromList([4, 2, 6, 1, 3])], 1),
        new Testcase([TreeNode.fromList([1, 0, 48, null, null, 12, 49])], 1),
    ]);
}
