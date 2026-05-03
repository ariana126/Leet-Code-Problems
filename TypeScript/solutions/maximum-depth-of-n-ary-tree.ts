// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
// TODO

class _Node {
    val: number
    children: _Node[]

    constructor(val?: number, children?: _Node[]) {
        this.val = (val===undefined ? 0 : val)
        this.children = (children===undefined ? [] : children)
    }
}

function maxDepth(root: _Node | null): number {
    return 2;
}


export function examine(): void {
    console.log(maxDepth(new _Node()))
}