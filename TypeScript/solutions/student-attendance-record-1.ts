// https://leetcode.com/problems/student-attendance-record-i/description/
import { Examiner, Testcase } from '../utils';


function checkRecord(s: string): boolean {
    let absentTimes = 0, lateWindow = 0;
    for (const record of s) {
        if (record === 'A') {
            absentTimes++;
            if (absentTimes > 1) return false;
        }
        if (record === 'L') {
            lateWindow++;
            if (lateWindow > 2) return false;
        } else {
            lateWindow = 0;
        }
    }
    return true;
}

export function examine(): void {
    new Examiner(checkRecord).run([
        new Testcase(['PPALLP'], true),
        new Testcase(['PPALLL'], false),
    ]);
}
