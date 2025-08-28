import time
from typing import Any

class Logger:
    logs: list[list[Any]] = []
    @classmethod
    def log(cls, *messages) -> None:
        cls.logs.append(list(messages))
    @classmethod
    def release(cls)->list[Any]:
        logs = cls.logs
        cls.logs = []
        return logs

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

class Testcase:
    def __init__(self, inputs: tuple[Any, ...], expected: Any, validation: Validation=Validation.on_output()) -> None:
        self.inputs = inputs
        self.expected = expected
        self.validation = validation

class Examiner:
    def __init__(self, solution: Any, method_name: str):
        self.solution = solution
        self.method_name = method_name

    def run(self, testcases: tuple[Testcase, ...]) -> None:
        print('Start.\n')

        execution_times: list[tuple[Testcase, float]] = []
        for testcase in testcases:
            start: float = time.perf_counter()
            output: Any = getattr(self.solution, self.method_name)(*testcase.inputs)
            end: float = time.perf_counter()
            execution_times.append((testcase, end - start))

            if testcase.validation.should_be_on_input():
                output = testcase.inputs[testcase.validation.input_index]
            if testcase.expected != output:
                print(f'Wrong: {testcase.inputs} -> {output} expected {testcase.expected}')
                for log in Logger.release():
                    print(*log)
                print('\n')

        print('Execution times:')
        total_time: float = 0
        max_time: float = 0
        min_time: float = float('inf')
        for execution_time in execution_times:
            print(f'{execution_time[1]*1_000_000:.2f} μs {execution_time[0].inputs}')
            total_time += execution_time[1]
            max_time = max(max_time, execution_time[1])
            min_time = min(min_time, execution_time[1])
        print(f'\nAverage: {total_time/len(execution_times)*1_000_000:.2f} μs')
        print(f'Max: {max_time*1_000_000:.2f} μs')
        print(f'Min: {min_time*1_000_000:.2f} μs')

        print('\nDone.')