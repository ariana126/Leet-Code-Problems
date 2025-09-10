# https://leetcode.com/problems/lru-cache/description/
from utils.examination import DesignExaminer, DesignTestcase, Logger


class Node:
    def __init__(self, key: int, value: int, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def set_right(self, node)->None:
        self.right = node
        if not node is None:
            node.left = self
    def unlink_right(self) -> None:
        if not self.right is None:
            self.right.left = None
        self.right = None

    def set_left(self, node)->None:
        self.left = node
        if not node is None:
            node.right = self
    def unlink_left(self)->None:
        if not self.left is None:
            self.left.right = None
        self.left = None

    def is_equal(self, node)->bool:
        if node is None:
            return False
        return self.key == node.key

class LRUCache:

    def __init__(self, capacity: int):
        self.__capacity: int = capacity
        self.__cache: dict[int, Node] = {}
        self.__head: Node|None = None
        self.__tail: Node|None = None

    def get(self, key: int) -> int:
        if not key in self.__cache:
            return -1
        node: Node = self.__cache[key]
        self.__update_rank(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.__cache:
            node: Node = self.__cache[key]
            node.value = value
            self.__update_rank(node)
            self.__cache[key] = node
            return
        node: Node = Node(key, value)
        if self.__capacity == len(self.__cache):
            head_key: int = self.__head.key
            self.__pop_head_rank()
            del self.__cache[head_key]
        self.__calculate_new_node_rank(node)
        self.__cache[key] = node

    def __pop_head_rank(self)->None:
        if self.__head.is_equal(self.__tail):
            self.__head = None
            self.__tail = None
            return
        self.__head = self.__head.right
        self.__head.unlink_left()
    def __set_tail_rank(self, node: Node)->None:
        self.__tail.set_right(node)
        self.__tail = node
        self.__tail.unlink_right()

    def __calculate_new_node_rank(self, node: Node)->None:
        if self.__head is None:
            self.__head = node
            self.__tail = node
            return
        self.__set_tail_rank(node)

    def __update_rank(self, node: Node) -> None:
        if self.__tail.is_equal(node):
            return
        if self.__head.is_equal(node):
            self.__pop_head_rank()
            self.__set_tail_rank(node)
            return
        right: Node = node.right
        node.unlink_right()
        left: Node = node.left
        node.unlink_left()
        left.set_right(right)
        self.__set_tail_rank(node)

def examine()->None:
    DesignExaminer(LRUCache).run((
        DesignTestcase(
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4]
        ),
        DesignTestcase(
            ["LRUCache","put","get","put","get","get"],
            [[1],[2,1],[2],[3,2],[2],[3]],
            [None, None, 1, None, -1, 2]
        ),
    ))