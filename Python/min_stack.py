# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/
class MinStacNode:
    def __init__(self, val: int, min_val_in_stack: int):
        self._val = val
        self._min_val = min_val_in_stack
    def val(self) -> int:
        return self._val
    def min_val(self) -> int:
        return self._min_val

class MinStack:
    def __init__(self):
        self._stack: list[MinStacNode] = []
    def push(self, val: int) -> None:
        min_val: int = val
        if not self._empty() and self._top_node().min_val() < min_val:
            min_val = self._top_node().min_val()
        self._stack.append(MinStacNode(val, min_val))
    def pop(self) -> None:
        self._stack.pop()
    def top(self) -> int:
        return self._top_node().val()
    def getMin(self) -> int:
        return self._top_node().min_val()
    def _top_node(self) -> MinStacNode:
        return self._stack[-1]
    def _empty(self) -> bool:
        return 0 == len(self._stack)

def examine()-> None:
    stack = MinStack()
    stack.push(1)
    print(stack.getMin())
    stack.push(-3)
    stack.pop()
    print(stack.getMin())
    stack.pop()
    print(stack.top())