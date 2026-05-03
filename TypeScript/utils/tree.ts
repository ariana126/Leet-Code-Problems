export class TreeNode {
    val: any;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val: any, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    static fromList(nodes: (any | null)[]): TreeNode | null {
        if (nodes.length === 0) return null;
        const root = new TreeNode(nodes[0]);
        let currentDepth: TreeNode[] = [root];
        let nextDepth: TreeNode[] = [];
        let i = 1;
        while (i < nodes.length) {
            for (const node of currentDepth) {
                if (i < nodes.length && nodes[i] !== null) {
                    node.left = new TreeNode(nodes[i]);
                    nextDepth.push(node.left);
                }
                if (i + 1 < nodes.length && nodes[i + 1] !== null) {
                    node.right = new TreeNode(nodes[i + 1]);
                    nextDepth.push(node.right);
                }
                i += 2;
            }
            currentDepth = nextDepth;
            nextDepth = [];
        }
        return root;
    }

    toList(): (any | null)[] {
        const nodes: (any | null)[] = [this.val];
        let currentDepth: TreeNode[] = [this];
        let nextDepth: TreeNode[] = [];
        while (currentDepth.length !== 0) {
            for (const node of currentDepth) {
                if (node.left !== null) {
                    nodes.push(node.left.val);
                    nextDepth.push(node.left);
                } else {
                    nodes.push(null);
                }
                if (node.right !== null) {
                    nodes.push(node.right.val);
                    nextDepth.push(node.right);
                } else {
                    nodes.push(null);
                }
            }
            currentDepth = nextDepth;
            nextDepth = [];
        }
        let end = nodes.length - 1;
        while (end >= 0 && nodes[end] === null) {
            end--;
        }
        return nodes.slice(0, end + 1);
    }

    toString(): string {
        return JSON.stringify(this.toList());
    }

    equals(other: TreeNode | null): boolean {
        if (other === null) return false;
        return JSON.stringify(this.toList()) === JSON.stringify(other.toList());
    }
}
