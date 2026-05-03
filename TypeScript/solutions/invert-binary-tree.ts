// https://leetcode.com/problems/invert-binary-tree/description/
import { Examiner, Testcase, TreeNode } from '../utils';


function invertTree(root: TreeNode | null): TreeNode | null {
    if (root === null) return null;
    const left = root.left;
    root.left = invertTree(root.right);
    root.right = invertTree(left);
    return root;
}

export function examine(): void {
    new Examiner(invertTree).run([
        new Testcase([TreeNode.fromList([])], TreeNode.fromList([])),
        new Testcase([TreeNode.fromList([2, 1, 3])], TreeNode.fromList([2, 3, 1])),
        new Testcase([TreeNode.fromList([4, 2, 7, 1, 3, 6, 9])], TreeNode.fromList([4, 7, 2, 9, 6, 3, 1])),
    ]);
}
