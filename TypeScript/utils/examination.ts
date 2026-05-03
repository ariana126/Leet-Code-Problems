import { ListNode } from './linked-list.ts';
import { TreeNode } from './tree.ts';

function deepEquals(a: any, b: any): boolean {
    if (a == null && b == null) return true;
    if (a instanceof ListNode && b instanceof ListNode) return a.equals(b);
    if (a instanceof TreeNode && b instanceof TreeNode) return a.equals(b);
    return JSON.stringify(a) === JSON.stringify(b);
}

export class Logger {
    private static logs: any[][] = [];

    static log(...messages: any[]): void {
        Logger.logs.push(structuredClone(messages));
    }

    static release(): any[][] {
        const logs = Logger.logs;
        Logger.logs = [];
        return logs;
    }
}

export abstract class TestcaseInterface {
    abstract id(): string;
}

export class TestcaseResult {
    readonly passed: boolean;
    readonly note: string;

    private constructor(passed: boolean, note: string) {
        this.passed = passed;
        this.note = note;
    }

    static passed(): TestcaseResult {
        return new TestcaseResult(true, '');
    }

    static failed(expected: any, actual: any, context?: string): TestcaseResult {
        let note = `${String(actual)} expected ${String(expected)}`;
        if (context !== undefined) note += ` - ${context}`;
        return new TestcaseResult(false, note);
    }
}

export abstract class ExaminerInterface {
    abstract run(testcases: readonly TestcaseInterface[]): void;
}

export abstract class FullReviewExaminer extends ExaminerInterface {
    private static readonly RED = '\x1b[31m';
    private static readonly GREEN = '\x1b[32m';
    private static readonly YELLOW = '\x1b[33m';
    private static readonly DIM = '\x1b[2m';
    private static readonly RESET = '\x1b[0m';

    run(testcases: readonly TestcaseInterface[]): void {
        const executionTimes: Array<[TestcaseInterface, number]> = [];
        let passCount = 0;

        for (const testcase of testcases) {
            const start = performance.now();
            const result = this.examine(testcase);
            const end = performance.now();
            executionTimes.push([testcase, end - start]);

            if (result.passed) {
                passCount++;
            } else {
                const logs = Logger.release();
                console.log(`${FullReviewExaminer.RED}✗ ${testcase.id()}${FullReviewExaminer.RESET}`);
                console.log(`  ${result.note}`);
                for (const log of logs) {
                    console.log(' ', ...log);
                }
                console.log('');
            }
            Logger.release();
        }

        const n = executionTimes.length;
        const failCount = n - passCount;
        const allPassed = failCount === 0;
        const summaryColor = allPassed ? FullReviewExaminer.GREEN : FullReviewExaminer.RED;
        const passIcon = allPassed ? '✓' : '✗';
        console.log(`${summaryColor}${passIcon} ${passCount}/${n} passed${FullReviewExaminer.RESET}`);

        const sorted = [...executionTimes].sort((a, b) => a[1] - b[1]).map(([, t]) => t);
        const totalTime = sorted.reduce((s, t) => s + t, 0);
        const percentile = (p: number) => sorted[Math.min(Math.floor(p / 100 * n), n - 1)]! * 1000;

        console.log(`\n${FullReviewExaminer.YELLOW}Execution times:${FullReviewExaminer.RESET}`);
        for (const [testcase, elapsed] of executionTimes) {
            console.log(`  ${FullReviewExaminer.DIM}${(elapsed * 1000).toFixed(2).padStart(8)} μs${FullReviewExaminer.RESET}  ${testcase.id()}`);
        }
        console.log(`\n  p50 ${percentile(50).toFixed(2)} μs  p95 ${percentile(95).toFixed(2)} μs  avg ${(totalTime / n * 1000).toFixed(2)} μs`);
    }

    abstract examine(testcase: TestcaseInterface): TestcaseResult;
}

export class Validation {
    static readonly TYPE_INPUT = 'INPUT' as const;
    static readonly TYPE_OUTPUT = 'OUTPUT' as const;

    readonly type: 'INPUT' | 'OUTPUT';
    readonly inputIndex: number | null;

    private constructor(type: 'INPUT' | 'OUTPUT', inputIndex: number | null = null) {
        this.type = type;
        this.inputIndex = inputIndex;
    }

    static onInputNumber(inputIndex: number): Validation {
        return new Validation(Validation.TYPE_INPUT, inputIndex);
    }

    static onOutput(): Validation {
        return new Validation(Validation.TYPE_OUTPUT);
    }

    shouldBeOnInput(): boolean {
        return this.type === Validation.TYPE_INPUT;
    }
}

export class Testcase extends TestcaseInterface {
    readonly inputs: readonly any[];
    readonly expected: any;
    readonly validation: Validation;

    constructor(inputs: readonly any[], expected: any, validation: Validation = Validation.onOutput()) {
        super();
        this.inputs = inputs;
        this.expected = expected;
        this.validation = validation;
    }

    override id(): string {
        return String(this.inputs);
    }
}

export class Examiner extends FullReviewExaminer {
    private readonly fn: (...args: any[]) => any;

    constructor(fn: (...args: any[]) => any) {
        super();
        this.fn = fn;
    }

    override examine(testcase: Testcase): TestcaseResult {
        let output: any = this.fn(...testcase.inputs);
        if (testcase.validation.shouldBeOnInput()) {
            output = testcase.inputs[testcase.validation.inputIndex!];
        }
        if (!deepEquals(testcase.expected, output)) {
            return TestcaseResult.failed(testcase.expected, output);
        }
        return TestcaseResult.passed();
    }
}

export class DesignTestcase extends TestcaseInterface {
    readonly calls: string[];
    readonly inputs: any[][];
    readonly outputs: any[];

    constructor(calls: string[], inputs: any[][], outputs: any[]) {
        super();
        this.calls = calls;
        this.inputs = inputs;
        this.outputs = outputs;
    }

    override id(): string {
        return `${JSON.stringify(this.calls)} - ${JSON.stringify(this.inputs)}`;
    }
}

export class DesignExaminer extends FullReviewExaminer {
    private readonly solutionClass: new (...args: any[]) => any;

    constructor(solutionClass: new (...args: any[]) => any) {
        super();
        this.solutionClass = solutionClass;
    }

    override examine(testcase: DesignTestcase): TestcaseResult {
        let solution: any = null;
        for (let i = 0; i < testcase.calls.length; i++) {
            const call = testcase.calls[i]!;
            const callInputs = testcase.inputs[i] ?? [];
            if (this.solutionClass.name === call) {
                solution = new this.solutionClass(...callInputs);
                continue;
            }
            const output: any = solution[call](...callInputs);
            if (!deepEquals(testcase.outputs[i], output)) {
                return TestcaseResult.failed(testcase.outputs[i], output, `index ${i} ${call}(${JSON.stringify(callInputs)})`);
            }
        }
        return TestcaseResult.passed();
    }
}
