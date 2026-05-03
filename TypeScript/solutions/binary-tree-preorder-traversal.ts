// https://leetcode.com/problems/binary-tree-preorder-traversal/description/
import { Examiner, Testcase, TreeNode } from '../utils';


function preorderTraversal(root: TreeNode | null): number[] {
    if (root === null) return [];
    return [root.val, ...preorderTraversal(root.left), ...preorderTraversal(root.right)];
}

export function examine(): void {
    new Examiner(preorderTraversal).run([
        new Testcase([TreeNode.fromList([1, null, 2, 3])], [1, 2, 3]),
        new Testcase([TreeNode.fromList([])], []),
        new Testcase([TreeNode.fromList([1])], [1]),
        new Testcase([TreeNode.fromList([1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9])], [1, 2, 4, 5, 6, 7, 3, 8, 9]),
    ]);
}
