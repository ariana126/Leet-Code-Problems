# https://leetcode.com/problems/keyboard-row/description/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows: list[str] = [
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm',
        ]
        index_rows: list[dict[str, str]] = []
        for row in rows:
            index_row: dict[str, str] = {}
            for c in row:
                index_row[c.lower()] = c
            index_rows.append(index_row)

        applicable_words: list[str] = []
        for word in words:
            for row in index_rows:
                is_applicable = True
                for c in word:
                    if not c.lower() in row:
                        is_applicable = False
                        break
                if is_applicable:
                    applicable_words.append(word)

        return applicable_words



def examine()->None:
    Examiner(Solution(), 'findWords').run((
        Testcase((["Hello","Alaska","Dad","Peace"],), ["Alaska","Dad"]),
        Testcase((["omk"],), []),
        Testcase((["adsdf","sfd"],), ["adsdf","sfd"]),
    ))