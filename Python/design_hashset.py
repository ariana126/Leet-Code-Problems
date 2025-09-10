# https://leetcode.com/problems/design-hashset/description/
from utils.examination import DesignExaminer, DesignTestcase


class MyHashSet:

    def __init__(self):
        self.hashTable = {}
    def add(self, key: int) -> None:
        self.hashTable[key] = None
    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        del self.hashTable[key]
    def contains(self, key: int) -> bool:
        return key in self.hashTable

def examine()->None:
    DesignExaminer(MyHashSet).run((
        DesignTestcase(
            ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"],
            [[],[1],[2],[1],[3],[2],[2],[2],[2]],
            [None, None, None, True, False, None, True, None, False],
        ),
        DesignTestcase(
            ["MyHashSet","add","remove","add","remove","remove","add","add","add","add","remove"],
            [[],[9],[19],[14],[19],[9],[0],[3],[4],[0],[9]],
            [None,None,None,None,None,None,None,None,None,None,None],
        ),
    ))