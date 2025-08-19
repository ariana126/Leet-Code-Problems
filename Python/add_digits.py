# https://leetcode.com/problems/add-digits/description/?envType=problem-list-v2&envId=math
class Solution:
    def addDigits(self, num: int) -> int:
        while 9 < num:
            temp: int = 0
            while 0 < num:
                temp += num % 10
                num = (num - (num % 10)) / 10
            num = temp
        return int(num)

def examine()->None:
    print(Solution().addDigits(1234))