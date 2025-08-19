# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/
from unittest import case


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        fizz: str = 'Fizz'
        buzz: str = 'Buzz'
        string_: list[str] = []
        for i in range(1, n + 1):
            is_divided_by_tree: bool = 0 == i % 3
            is_divided_by_five: int = 0 == i % 5
            if not is_divided_by_tree and not is_divided_by_five:
                string_.append(str(i))
                continue
            if is_divided_by_tree and is_divided_by_five:
                string_.append(fizz + buzz)
                continue
            if is_divided_by_tree:
                string_.append(fizz)
                continue
            if is_divided_by_five:
                string_.append(buzz)
                continue
        return string_

def examine()->None:
    n = 15
    print(Solution().fizzBuzz(n))