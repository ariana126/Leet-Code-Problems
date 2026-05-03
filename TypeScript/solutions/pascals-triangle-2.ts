// https://leetcode.com/problems/pascals-triangle-ii/description/
import { Examiner, Testcase } from '../utils';


function getRow(rowIndex: number): number[] {
    let current: number[] = [1];
    for (let i = 1; i <= rowIndex; i++) {
        const next: number[] = [1];
        for (let j = 0; j < current.length - 1; j++) next.push(current[j]! + current[j + 1]!);
        next.push(1);
        current = next;
    }
    return current;
}

export function examine(): void {
    new Examiner(getRow).run([
        new Testcase([3], [1, 3, 3, 1]),
        new Testcase([0], [1]),
        new Testcase([1], [1, 1]),
    ]);
}
