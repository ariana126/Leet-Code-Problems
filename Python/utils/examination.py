import copy
import time
from abc import ABC, abstractmethod
from typing import Any, Type


class Logger:
    logs: list[list[Any]] = []
    @classmethod
    def log(cls, *messages) -> None:
        cls.logs.append(copy.deepcopy(list(messages)))
    @classmethod
    def release(cls)->list[Any]:
        logs = cls.logs
        cls.logs = []
        return logs

class TestcaseInterface(ABC):
    @abstractmethod
    def id(self) -> str:
        pass

class TestcaseResult:
    def __init__(self, passed: bool, note: str):
        self.passed = passed
        self.note = note
    @classmethod
    def passed(cls) -> 'TestcaseResult':
        return cls(True, '')
    @classmethod
    def failed(cls, expected: str, actual: str, context: str|None = None) -> 'TestcaseResult':
        note: str = f'{actual} expected {expected}'
        if not context is None:
            note += f' - {context}'
        return cls(False, note)


class ExaminerInterface(ABC):
    @abstractmethod
    def run(self, testcases: tuple[TestcaseInterface, ...]) -> None:
        pass

class FullReviewExaminer(ExaminerInterface, ABC):

    def run(self, testcases: tuple[TestcaseInterface, ...]) -> None:
        print('Start.\n')

        execution_times: list[tuple[TestcaseInterface, float]] = []
        for testcase in testcases:
            start: float = time.perf_counter()
            result: TestcaseResult = self.examine(testcase)
            end: float = time.perf_counter()
            execution_times.append((testcase, end - start))
            if not result.passed:
                print(f'Wrong: {testcase.id()} -> {result.note}')
                for log in Logger.release():
                    print(*log)
                print('')
            Logger.release()

        print('End.')

        print('\nExecution times:')
        total_time: float = 0
        max_time: float = 0
        min_time: float = float('inf')
        for execution_time in execution_times:
            print(f'{execution_time[1]*1_000_000:.2f} μs {execution_time[0].id()}')
            total_time += execution_time[1]
            max_time = max(max_time, execution_time[1])
            min_time = min(min_time, execution_time[1])
        print(f'\nAverage: {total_time/len(execution_times)*1_000_000:.2f} μs')
        print(f'Max: {max_time*1_000_000:.2f} μs')
        print(f'Min: {min_time*1_000_000:.2f} μs')

    @abstractmethod
    def examine(self, testcase: TestcaseInterface) -> TestcaseResult:
        pass

class Validation:
    TYPE_INPUT: str = 'INPUT'
    TYPE_OUTPUT: str = 'OUTPUT'
    VALID_TYPES: tuple[str] = (TYPE_INPUT, TYPE_OUTPUT)
    def __init__(self, type_: str, input_index: int|None=None):
        if type_ not in self.VALID_TYPES:
            raise ValueError(f'Invalid type: {type_}')
        self.type = type_
        self.input_index = input_index
    @classmethod
    def on_input_number(cls, input_index: int) -> 'Validation':
        return cls(cls.TYPE_INPUT, input_index)
    @classmethod
    def on_output(cls) -> 'Validation':
        return cls(cls.TYPE_OUTPUT)
    def should_be_on_input(self) -> bool:
        return self.TYPE_INPUT == self.type

class Testcase(TestcaseInterface):
    def __init__(self, inputs: tuple[Any, ...], expected: Any, validation: Validation=Validation.on_output()) -> None:
        self.inputs = inputs
        self.expected = expected
        self.validation = validation

    def id(self) -> str:
        return str(self.inputs)

class Examiner(FullReviewExaminer):
    def __init__(self, solution: Any, method_name: str):
        self.solution = solution
        self.method_name = method_name

    def examine(self, testcase: Testcase) -> TestcaseResult:
        output: Any = getattr(self.solution, self.method_name)(*testcase.inputs)
        if testcase.validation.should_be_on_input():
            output = testcase.inputs[testcase.validation.input_index]
        if testcase.expected != output:
            return TestcaseResult.failed(testcase.expected, output)
        return TestcaseResult.passed()

class DesignTestcase(TestcaseInterface):
    def __init__(self, calls: list[str], inputs: list[Any], outputs: list[Any]):
        self.calls = calls
        self.inputs = inputs
        self.outputs = outputs
    def id(self) -> str:
        return f'{self.calls} - {self.inputs}'


class DesignExaminer(FullReviewExaminer):
    def __init__(self, solution_class: Type[Any]):
        self.__solution_class = solution_class

    def examine(self, testcase: DesignTestcase) -> TestcaseResult:
        solution: Type[Any] | None = None
        for i, call in enumerate(testcase.calls):
            if self.__solution_class.__name__ == call:
                solution = self.__solution_class(*testcase.inputs[i])
                continue
            output: Any = getattr(solution, call)(*testcase.inputs[i])
            if not testcase.outputs[i] == output:
                return TestcaseResult.failed(testcase.outputs[i], output, f'index {i} {call}({testcase.inputs[i]})')
        return TestcaseResult.passed()