# https://leetcode.com/problems/3sum-closest/description/
from utils.examination import Examiner, Testcase, Logger
from utils.search import Searcher, SearchResult, SearchQuery, Range, Element

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        if 0 < nums[0] and target <= nums[0]:
            return nums[0] + nums[1] + nums[2]
        if 0 > nums[-1] and target <= nums[-1]:
            return nums[-1] + nums[-2] + nums[-3]
        searcher: Searcher = Searcher.in_(nums)
        min_diff = float('+inf')
        closest_sum_: int = 0
        zero: SearchResult = searcher.search(SearchQuery(0))
        if zero.has_found():
            pointers: tuple[int, int] = (zero.index, zero.index + 1)
        else:
            first_pointer: Element = zero.nearest_left
            second_pointer: Element = zero.nearest_right
            if first_pointer.is_out_of_range():
                first_pointer = Element(nums[0], 0)
                second_pointer = Element(nums[1], 1)
            if second_pointer.is_out_of_range():
                first_pointer = Element(nums[-2], len(nums) - 2)
                second_pointer = Element(nums[-1], len(nums) - 1)
            pointers: tuple[int, int] = (first_pointer.index, second_pointer.index)
        while 0 <= pointers[0] and len(nums) - 1 >= pointers[1]:
            remaining_value: int = target - (nums[pointers[0]] + nums[pointers[1]])
            if 0 <= remaining_value:
                range_: Range = Range.start_from(pointers[1] + 1)
            else:
                range_: Range = Range.till(pointers[0] - 1)
            if 0 == pointers[0] and len(nums) - 1 == pointers[1]:
                range_: Range = Range(1, len(nums) - 2)
            remaining_search_result: SearchResult = searcher.search(SearchQuery(remaining_value, range_))
            if remaining_search_result.has_found():
                return target
            remaining: Element = remaining_search_result.nearest_to(remaining_value)

            sum_: int = remaining.value + (nums[pointers[0]] + nums[pointers[1]])
            diff: int = abs(target - sum_)
            Logger.log(min_diff, diff, pointers[0], pointers[1], remaining.value, remaining_search_result, remaining_value, range_)
            if min_diff > diff:
                min_diff = diff
                closest_sum_ = sum_

            if 0 == pointers[0] and len(nums) - 1 == pointers[1]:
                break
            if target <= sum_:
                s: int = pointers[0] - 1
                if 0 > s:
                    pointers: tuple[int, int] = (0, pointers[1] + 1)
                    continue
                pointers: tuple[int, int] = (s, pointers[1])
            else:
                e: int = pointers[1] + 1
                if len(nums) - 1 < e:
                    pointers: tuple[int, int] = (pointers[0] - 1, len(nums) - 1)
                    continue
                pointers: tuple[int, int] = (pointers[0], e)
        return closest_sum_

def examine()->None:
    Examiner(Solution(), 'threeSumClosest').run((
        Testcase(([1,1,-1], 2), -1),
        Testcase(([1,1,1,1], 3), 3),
        Testcase(([1,1,1,0], -100), 2),
        Testcase(([-100,-98,-2,-1], -101), -101),
        Testcase(([-1,2,1,-4], 1), 2),
        Testcase(([-100, -2, 1, 3, 25, 75], 0), 0),
        Testcase(([102, 4, 3, -23, -73], 2), 6),
        Testcase(([102, 4, 3, 2, 2, 2, -23, -73], 2), 6),
    ))