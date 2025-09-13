# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
from utils.examination import DesignExaminer, DesignTestcase


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.scores: list[int] = nums
        self.scores.sort()
        self.k: int = k

    def add(self, val: int) -> int:
        self.scores.append(val)
        self.scores.sort()
        return self.scores[-self.k]

def examine()->None:
    DesignExaminer(KthLargest).run((
        DesignTestcase(
            ["KthLargest","add","add","add","add","add"],
            [[3,[4,5,8,2]],[3],[5],[10],[9],[4]],
            [None, 4, 5, 5, 8, 8],
        ),
        DesignTestcase(
            ["KthLargest", "add", "add", "add", "add"],
            [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]],
            [None, 7, 7, 7, 8],
        ),
    ))