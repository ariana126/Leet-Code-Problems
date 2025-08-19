# https://leetcode.com/problems/base-7?envType=problem-list-v2&envId=math
class Solution:
    def convertToBase7(self, num: int) -> str:
        in_string: str = ''

        sign: str = ''
        if num < 0:
            sign = '-'
            num -= 2 * num

        ones: int = num % 7
        in_string = str(ones) + in_string
        x: int = int(num / 7)
        while  0 < x:
            y: int = x % 7
            in_string = str(y) + in_string
            x = int((x - y) / 7)

        if '-' == sign:
            in_string = '-' + in_string
        return in_string


def examine()->None:
    print(Solution().convertToBase7(-7))