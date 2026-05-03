// https://leetcode.com/problems/binary-tree-paths/description/
import { Examiner, Testcase, TreeNode } from '../utils';


function binaryTreePaths(root: TreeNode | null): string[] {
    if (root === null) return [];
    if (root.left === null && root.right === null) return [String(root.val)];
    const leafs: string[] = [];
    if (root.left !== null) leafs.push(...binaryTreePaths(root.left));
    if (root.right !== null) leafs.push(...binaryTreePaths(root.right));
    return leafs.map(path => `${root.val}->${path}`);
}

export function examine(): void {
    new Examiner(binaryTreePaths).run([
        new Testcase([TreeNode.fromList([1, 2, 3, null, 5])], ['1->2->5', '1->3']),
        new Testcase([TreeNode.fromList([])], []),
        new Testcase([TreeNode.fromList([1])], ['1']),
    ]);
}