// https://leetcode.com/problems/construct-the-rectangle/
import { Examiner, Testcase } from '../utils';


function constructRectangle(area: number): number[] {
    const square = Math.floor(Math.sqrt(area));
    for (let i = square; i >= 1; i--) {
        if (area % i === 0) return [area / i, i];
    }
    return [];
}

export function examine(): void {
    new Examiner(constructRectangle).run([
        new Testcase([4], [2, 2]),
        new Testcase([37], [37, 1]),
        new Testcase([122122], [427, 286]),
    ]);
}
