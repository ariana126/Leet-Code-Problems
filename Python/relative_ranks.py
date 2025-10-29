# https://leetcode.com/problems/relative-ranks/description/
from utils.examination import Examiner, Testcase, Logger


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ranks: list[int] = sorted(score, reverse=True)
        map_: dict[int, int] = {}
        for i, s in enumerate(ranks):
            map_[s] = i

        result: list[str] = []
        for s in score:
            rank: str = ''
            match map_[s]:
                case 0:
                    rank = 'Gold Medal'
                case 1:
                    rank = 'Silver Medal'
                case 2:
                    rank = 'Bronze Medal'
                case _:
                    rank = str(map_[s] + 1)
            result.append(rank)
        return result

def examine() -> None:
    Examiner(Solution(), 'findRelativeRanks').run((
        Testcase(([5,4,3,2,1],), ["Gold Medal","Silver Medal","Bronze Medal","4","5"]),
        Testcase(([10,3,8,9,4],), ["Gold Medal","5","Bronze Medal","Silver Medal","4"]),
    ))