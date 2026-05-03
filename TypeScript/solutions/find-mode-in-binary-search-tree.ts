// https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
import { Examiner, Testcase, TreeNode } from '../utils';


function findMode(root: TreeNode | null): number[] {
    let modes: number[] = [];
    let maxCount = 0, currentCount = 0;
    let prevVal: number | null = null;
    function inorder(node: TreeNode | null): void {
        if (node === null) return;
        inorder(node.left);
        currentCount = prevVal === node.val ? currentCount + 1 : 1;
        if (currentCount > maxCount) { maxCount = currentCount; modes = [node.val]; }
        else if (currentCount === maxCount) modes.push(node.val);
        prevVal = node.val;
        inorder(node.right);
    }
    inorder(root);
    return modes;
}

export function examine(): void {
    new Examiner(findMode).run([
        new Testcase([TreeNode.fromList([1, null, 2, 2])], [2]),
        new Testcase([TreeNode.fromList([0])], [0]),
    ]);
}
