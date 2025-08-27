# https://leetcode.com/problems/integer-to-roman/description/
class Solution:
    def intToRoman(self, num: int) -> str:
        def get_symbol(num_: int, position_: int) -> str:
            translation: dict[int, dict[str, str]] = {
                0: {'1': 'I', '5': 'V'},
                1: {'1': 'X', '5': 'L'},
                2: {'1': 'C', '5': 'D'},
                3: {'1': 'M', '5': ''},
            }
            if 3 >= num_:
                return translation[position_]['1'] * num_
            if 4 == num_:
                return translation[position_]['1'] + translation[position_]['5']
            if 5 == num_:
                return translation[position_]['5']
            if 8 >= num_:
                return translation[position_]['5'] + (translation[position_]['1'] * (num_ - 5))
            if 9 == num_:
                return translation[position_]['1'] + translation[position_ + 1]['1']
            return translation[position_ + 1]['1']
        roman: str = ''
        position: int = 0
        while 0 < num:
            position_num: int = num % 10
            roman = get_symbol(position_num, position) + roman
            num = (num - position_num) // 10
            position += 1
        return roman

def examine()->None:
    print(Solution().intToRoman(3749))