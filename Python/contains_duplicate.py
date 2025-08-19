class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap: dict[int, int] = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = 1
        return False

def examine() -> None:
    input_: list[int] = [32, 3, 3, 54, 54]

    solution = Solution()
    output = solution.containsDuplicate(input_)
    print(output)

