// https://leetcode.com/problems/count-complete-tree-nodes/description/
import { Examiner, Testcase, TreeNode } from '../utils';


function countNodes(root: TreeNode | null): number {
    if (root === null) return 0;
    return 1 + countNodes(root.left) + countNodes(root.right);
}

export function examine(): void {
    new Examiner(countNodes).run([
        new Testcase([TreeNode.fromList([1, 2, 3, 4, 5, 6])], 6),
        new Testcase([TreeNode.fromList([])], 0),
        new Testcase([TreeNode.fromList([1])], 1),
    ]);
}
