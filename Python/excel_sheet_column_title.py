class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        i: int = 0
        while i <= columnNumber:
            if 26 >= columnNumber - i:
                break

            # TODO

            i += 26


def examine() -> None:
    print(Solution().convertToTitle(28))