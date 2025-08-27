# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
class Solution:
    def toHex(self, num: int) -> str:
        if 0 ==  num:
            return '0'
        characters: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
        hex_: str = ''
        if 0 > num:
            num = 2 ** 32 + num
        while 0 < num:
            p: int = num & 15
            num >>= 4
            hex_ = characters[p] + hex_
        return hex_

def examine()->None:
    print(Solution().toHex(-255))