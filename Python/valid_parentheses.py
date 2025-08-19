# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/
class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for char in s:
            if self._is_closing(char):
                if  0 == len(stack) or not self._is_same_kind(stack[len(stack) - 1], char):
                    return False
                stack.pop()
            if self._is_opening(char):
                stack.append(char)
        return 0 == len(stack)

    def _is_closing(self, s: str) -> bool:
        closing_strs: list[str] = [')', '}', ']']
        return s in closing_strs
    def _is_opening(self, s: str) -> bool:
        opening_strs: list[str] = ['(', '{', '[']
        return s in opening_strs
    def _is_same_kind(self, opener: str, closer: str) -> bool:
        match opener:
            case '(':
                return ')' == closer
            case '{':
                return '}' == closer
            case '[':
                return ']' == closer
        return False

def examine()-> None:
    print(Solution().isValid('({})[]'))