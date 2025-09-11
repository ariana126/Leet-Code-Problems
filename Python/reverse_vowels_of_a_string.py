# https://leetcode.com/problems/reverse-vowels-of-a-string/
from utils.examination import Examiner, Testcase


class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(char: str)->bool:
            vowels: tuple[str,...] = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u')
            return char in vowels
        vowels_indexes: list[int] = []
        for i, c in enumerate(s):
            if not is_vowel(c):
                continue
            vowels_indexes.append(i)
        s_list: list[str] = list(s)
        start: int = 0
        end: int = len(vowels_indexes) - 1
        while start < end:
            s_t: str = s_list[vowels_indexes[start]]
            s_list[vowels_indexes[start]] = s_list[vowels_indexes[end]]
            s_list[vowels_indexes[end]] = s_t
            start += 1
            end -= 1
        return ''.join(s_list)

def examine()->None:
    Examiner(Solution(), 'reverseVowels').run((
        Testcase(('IceCreAm',), 'AceCreIm'),
        Testcase(('AceCreIm',), 'IceCreAm'),
        Testcase(('leetcode',), 'leotcede'),
        Testcase(('leotcede',), 'leetcode'),
        Testcase(('',), ''),
    ))