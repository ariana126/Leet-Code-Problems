class Range:
    def __init__(self, start: int|None=None, end: int|None=None) -> None:
        self.start = start
        self.end = end

    def __str__(self):
        return f'Range(start={self.start}, end={self.end})'

    @classmethod
    def start_from(cls, start: int) -> 'Range':
        return Range(start, None)

    @classmethod
    def till(cls, end: int) -> 'Range':
        return Range(None, end)

class SearchQuery:
    def __init__(self, target: int, range_: Range|None=None):
        self.target = target
        self.range_ = range_

class Element:
    def __init__(self, value: int|None, index: int|None):
        self.value = value
        self.index = index

    @classmethod
    def out_of_range(cls) -> 'Element':
        return Element(None, None)

    def is_out_of_range(self) -> bool:
        return self.index is None

    def equals(self, other: 'Element') -> bool:
        if self.is_out_of_range() or other.is_out_of_range():
            return False
        return self.value == other.value and self.index == other.index

    def __str__(self):
        return f'Element(value={self.value}, index={self.index})'

class SearchResult:
    def __init__(self, nearest_left: Element, nearest_right: Element):
        self.nearest_left = nearest_left
        self.nearest_right = nearest_right

    def has_found(self) -> bool:
        return self.nearest_left.equals(self.nearest_right)

    @property
    def index(self) -> int:
        if not self.has_found():
            raise ValueError('No element found')
        return self.nearest_left.index

    @property
    def indexes(self) -> tuple[int, int]:
        return self.nearest_left.index, self.nearest_right.index

    def nearest_to(self, target: int) -> Element:
        if self.has_found():
            return self.nearest_left
        if self.nearest_right.is_out_of_range():
            return self.nearest_left
        if self.nearest_left.is_out_of_range():
            return self.nearest_right
        left_diff: int = abs(target - self.nearest_left.value)
        right_diff: int = abs(target - self.nearest_right.value)
        if left_diff < right_diff:
            return self.nearest_left
        else:
            return self.nearest_right

    def __str__(self):
        return f'SearchResult(nearest_left={self.nearest_left}, nearest_right={self.nearest_right})'
class Searcher:
    def __init__(self, list_: list[int]):
        self.list = list_

    @classmethod
    def in_(cls, list_: list[int]) -> 'Searcher':
        return Searcher(list_)

    def search(self, query: SearchQuery) -> SearchResult:
        start: int = 0
        if query.range_ is not None and query.range_.start is not None and 0 <= query.range_.start:
            start = query.range_.start
        end: int = len(self.list) - 1
        if query.range_ is not None and query.range_.end is not None and len(self.list) > query.range_.end:
            end = query.range_.end

        left_index: int|None = None
        right_index: int|None = None
        for i in range(start, end + 1):
            if query.target == self.list[i]:
                left_index = i
                right_index = i
                break
            if query.target < self.list[i]:
                right_index = i
                left_index = i - 1
                break
        if right_index is None and left_index is None:
            i: int = end
            return SearchResult(Element(self.list[i], i), Element.out_of_range())
        if start > left_index:
            return SearchResult(Element.out_of_range(), Element(self.list[right_index], right_index))
        return SearchResult(Element(self.list[left_index], left_index), Element(self.list[right_index], right_index))
