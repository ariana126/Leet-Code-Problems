export class Range {
    readonly start: number | null;
    readonly end: number | null;

    constructor(start: number | null = null, end: number | null = null) {
        this.start = start;
        this.end = end;
    }

    static startFrom(start: number): Range {
        return new Range(start, null);
    }

    static till(end: number): Range {
        return new Range(null, end);
    }

    toString(): string {
        return `Range(start=${this.start}, end=${this.end})`;
    }
}

export class SearchQuery {
    readonly target: number;
    readonly range: Range | null;

    constructor(target: number, range: Range | null = null) {
        this.target = target;
        this.range = range;
    }
}

export class Element {
    readonly value: number | null;
    readonly index: number | null;

    constructor(value: number | null, index: number | null) {
        this.value = value;
        this.index = index;
    }

    static outOfRange(): Element {
        return new Element(null, null);
    }

    isOutOfRange(): boolean {
        return this.index === null;
    }

    equals(other: Element): boolean {
        if (this.isOutOfRange() || other.isOutOfRange()) return false;
        return this.value === other.value && this.index === other.index;
    }

    toString(): string {
        return `Element(value=${this.value}, index=${this.index})`;
    }
}

export class SearchResult {
    readonly nearestLeft: Element;
    readonly nearestRight: Element;

    constructor(nearestLeft: Element, nearestRight: Element) {
        this.nearestLeft = nearestLeft;
        this.nearestRight = nearestRight;
    }

    hasFound(): boolean {
        return this.nearestLeft.equals(this.nearestRight);
    }

    get index(): number {
        if (!this.hasFound()) throw new Error('No element found');
        return this.nearestLeft.index!;
    }

    get indexes(): [number | null, number | null] {
        return [this.nearestLeft.index, this.nearestRight.index];
    }

    nearestTo(target: number): Element {
        if (this.hasFound()) return this.nearestLeft;
        if (this.nearestRight.isOutOfRange()) return this.nearestLeft;
        if (this.nearestLeft.isOutOfRange()) return this.nearestRight;
        const leftDiff = Math.abs(target - this.nearestLeft.value!);
        const rightDiff = Math.abs(target - this.nearestRight.value!);
        return leftDiff < rightDiff ? this.nearestLeft : this.nearestRight;
    }

    toString(): string {
        return `SearchResult(nearestLeft=${this.nearestLeft}, nearestRight=${this.nearestRight})`;
    }
}

export class Searcher {
    private readonly list: number[];

    constructor(list: number[]) {
        this.list = list;
    }

    static in_(list: number[]): Searcher {
        return new Searcher(list);
    }

    search(query: SearchQuery): SearchResult {
        let start = 0;
        if (query.range !== null && query.range.start !== null && query.range.start >= 0) {
            start = query.range.start;
        }
        let end = this.list.length - 1;
        if (query.range !== null && query.range.end !== null && this.list.length > query.range.end) {
            end = query.range.end;
        }

        let leftIndex: number | null = null;
        let rightIndex: number | null = null;
        let i = start;
        for (i = start; i <= end; i++) {
            const val = this.list[i]!;
            if (query.target === val) {
                leftIndex = i;
                rightIndex = i;
                break;
            }
            if (query.target < val) {
                rightIndex = i;
                leftIndex = i - 1;
                break;
            }
        }

        if (rightIndex === null && leftIndex === null) {
            return new SearchResult(new Element(this.list[end]!, end), Element.outOfRange());
        }
        if (start > leftIndex!) {
            return new SearchResult(Element.outOfRange(), new Element(this.list[rightIndex!]!, rightIndex!));
        }
        return new SearchResult(
            new Element(this.list[leftIndex!]!, leftIndex!),
            new Element(this.list[rightIndex!]!, rightIndex!)
        );
    }
}
