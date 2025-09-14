from utils.examination import DesignExaminer, DesignTestcase


class MyHashMap:
    def __init__(self):
        self.buckets_size: int = 10 ** 3
        self.storage: list[list[int|None]] = []

    def put(self, key: int, value: int) -> None:
        section_number: int = self.__get_section_number(key)
        if section_number >= len(self.storage):
            for i in range(section_number - len(self.storage) + 1):
                self.storage.append([])
        key_index_in_section: int = self.__get_key_index_in_section(key)
        if key_index_in_section >= len(self.storage[section_number]):
            for i in range(key_index_in_section - len(self.storage[section_number]) + 1):
                self.storage[section_number].append(None)
        self.storage[section_number][key_index_in_section] = value

    def get(self, key: int) -> int:
        section_number: int = self.__get_section_number(key)
        if section_number >= len(self.storage):
            return -1
        key_index_in_section: int = self.__get_key_index_in_section(key)
        if key_index_in_section >= len(self.storage[section_number]):
            return -1
        val: int|None = self.storage[section_number][key_index_in_section]
        if val is None:
            return -1
        return val

    def remove(self, key: int) -> None:
        section_number: int = self.__get_section_number(key)
        if section_number >= len(self.storage):
            return
        key_index_in_section: int = self.__get_key_index_in_section(key)
        if key_index_in_section >= len(self.storage[section_number]):
            return
        self.storage[section_number][key_index_in_section] = None

    def __get_section_number(self, key: int) -> int:
        return int((key - self.__get_key_index_in_section(key)) / self.buckets_size)
    def __get_key_index_in_section(self, key: int) -> int:
        return key % self.buckets_size

def examine()->None:
    DesignExaminer(MyHashMap).run((
        DesignTestcase(
            ["MyHashMap","put","put","get","get","put","get","remove","get"],
            [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]],
            [None, None, None, 1, -1, None, 1, None, -1],
        ),
    ))