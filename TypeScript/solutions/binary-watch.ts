// https://leetcode.com/problems/binary-watch/description/
import { Examiner, Testcase } from '../utils';


function readBinaryWatch(turnedOn: number): string[] {
    if (turnedOn > 8) return [];
    const result: string[] = [];
    for (let h = 0; h < 12; h++) {
        for (let m = 0; m < 60; m++) {
            const bits = h.toString(2).split('').filter(c => c === '1').length
                       + m.toString(2).split('').filter(c => c === '1').length;
            if (bits === turnedOn) result.push(`${h}:${m < 10 ? '0' : ''}${m}`);
        }
    }
    return result;
}

export function examine(): void {
    new Examiner(readBinaryWatch).run([
        new Testcase([9], []),
        new Testcase([0], ['0:00']),
        new Testcase([1], ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']),
    ]);
}
