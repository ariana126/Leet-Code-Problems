// https://leetcode.com/problems/binary-tree-postorder-traversal/description/
import { Examiner, Testcase, TreeNode } from '../utils';


function postorderTraversal(root: TreeNode | null): number[] {
    if (root === null) return [];
    return [
        ...postorderTraversal(root.left),
        ...postorderTraversal(root.right),
        root.val,
    ];
}

export function examine(): void {
    new Examiner(postorderTraversal).run([
        new Testcase([TreeNode.fromList([1, null, 2, 3])], [3, 2, 1]),
        new Testcase([TreeNode.fromList([])], []),
        new Testcase([TreeNode.fromList([1])], [1]),
        new Testcase([TreeNode.fromList([1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9])], [4, 6, 7, 5, 2, 9, 8, 3, 1]),
    ]);
}
