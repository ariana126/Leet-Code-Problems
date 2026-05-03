// https://leetcode.com/problems/excel-sheet-column-title/description/
import { Examiner, Testcase } from '../utils';


function convertToTitle(columnNumber: number): string {
    if (columnNumber === 0) return '';
    const firstChar = columnNumber % 26 === 0 ? 26 : columnNumber % 26;
    return convertToTitle(Math.floor((columnNumber - firstChar) / 26)) + String.fromCharCode(64 + firstChar);
}

export function examine(): void {
    new Examiner(convertToTitle).run([
        new Testcase([1], 'A'),
        new Testcase([28], 'AB'),
        new Testcase([701], 'ZY'),
        new Testcase([26], 'Z'),
        new Testcase([27], 'AA'),
        new Testcase([52], 'AZ'),
    ]);
}
