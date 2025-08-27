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
        for testcase in testcases:
            output: Any = getattr(self.solution, self.method_name)(*testcase.inputs)
            if testcase.validation.should_be_on_input():
                output = testcase.inputs[testcase.validation.input_index]
            if testcase.expected != output:
                print(f'Wrong: {testcase.inputs} -> {output} expected {testcase.expected}')
                for log in Logger.release():
                    print(*log)
                print('\n')