// https://leetcode.com/problems/relative-ranks/description/
import { Examiner, Testcase } from '../utils';


function findRelativeRanks(score: number[]): string[] {
    const sorted = [...score].sort((a, b) => b - a);
    const map = new Map<number, number>();
    sorted.forEach((s, i) => map.set(s, i));
    return score.map(s => {
        const rank = map.get(s)!;
        if (rank === 0) return 'Gold Medal';
        if (rank === 1) return 'Silver Medal';
        if (rank === 2) return 'Bronze Medal';
        return String(rank + 1);
    });
}

export function examine(): void {
    new Examiner(findRelativeRanks).run([
        new Testcase([[5, 4, 3, 2, 1]], ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']),
        new Testcase([[10, 3, 8, 9, 4]], ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']),
    ]);
}
