from typing import Callable, Any, Optional


class Entry:
    """Defines a dictionary element that consists of keywords and values"""
    def __init__(self, key: int, value: int) -> None:
        """
        Create an instance of Entry
        :param key: int
        :param value: int
        """
        self.key = key
        self.value = value


class Dict:
    """ Mutable dictionary based on hash-map, open address implementation """

    def __init__(self) -> None:
        """Create an instance of dictionary"""
        # The length of the hashTable
        self.len = 1000
        # HashTable is a list of dictionaries to store
        self.hashTable: list['Entry'] = [None for i in range(self.len)]
        # Dictionary size
        self.dict_size = 0

    def get(self, key: int) -> int:
        """
        getting value by key
        :param key: int
        :return: int
        """
        if self.find(key) != -1:
            return self.hashTable[self.find(key)].value
        else:
            print("The key element does not exist")
            return -1

    def member(self, key: int) -> int:
        """
        Is a member of a dictionary, 1 means existence, 0 means non-existence
        :param key: int
        :return: int
        """
        if self.find(key) != -1:
            return 1
        else:
            return 0

    def add(self, item: Optional['Entry']) -> None:
        """
        Add a new element，use linear detection for conflicts
        :param item: Optional['Entry']
        :return: None
        """
        if item is not None:
            j = item.key % self.len
            if self.hashTable[j] is None:
                self.hashTable[j] = item
                self.dict_size += 1
            else:
                i = 0
                while self.hashTable[j] is not None:
                    j = (j + 1) % self.len
                    i += 1
                    if i == self.len:
                        print("Failed to insert "
                              "because hashTable is full")
                        break
                self.hashTable[j] = item
                self.dict_size += 1

    def find(self, key: int) -> int:
        """
        Find the hash table position of the element
        :param key: int
        :return: int
        """
        j = key % self.len
        if self.hashTable[j] is not None:
            if self.hashTable[j].key == key:
                return j
            else:
                i = 0
                while self.hashTable[j] != key:
                    j = (j + 1) % self.len
                    i += 1
                    if i == self.len:
                        print("There is no element "
                              "with the value key in the dictionary")
                        return -1
                return j
        return -1

    def remove(self, key: int) -> None:
        """
        Remove an element by key for dictionaries
        :param key: int
        :return: None
        """
        if self.find(key) != -1:
            index = self.find(key)
            self.hashTable[index] = None
            self.dict_size -= 1
        else:
            print("element doesn't exist")

    def size(self) -> int:
        """
        Gets the size of the dictionary
        :return: int
        """
        return self.dict_size

    def to_list(self) -> dict[int, int]:
        """
        Conversion to built-in list
        :return:dict[int, int]
        """
        res = {}
        i = 0
        while i < self.len:
            if self.hashTable[i] is not None:
                res[self.hashTable[i].key] = self.hashTable[i].value
            i += 1
        return res

    def from_list(self, a: dict[int, int]) -> None:
        """
        Conversion from built-in list
        :param a: dict[int, int]
        :return: None
        """
        for key, value in a.items():
            x = Entry(key, value)
            self.add(x)

    def filter(self, p: Callable[[Any], Any]) -> None:
        """
        Filter dictionary by specific predicate
        :param p:Callable[[Any],Any]
        :return: None
        """
        i = 0
        while i < self.len:
            if self.hashTable[i] is None:
                i += 1
            else:
                if not p(self.hashTable[i].value):
                    self.hashTable[i] = None
                    i += 1
                else:
                    i += 1

    def map(self, f: Callable[[Any], Any]) -> None:
        """
        Map structure by specific function
        :param f: Callable[[Any], Any]
        :return: None
        """
        i = 0
        while i < self.len:
            if self.hashTable[i] is not None:
                self.hashTable[i].value = f(self.hashTable[i].value)
                i += 1
            else:
                i += 1

    def reduce(self,
               f: Callable[[Any, int], Any],
               initial_state: int) -> int:
        """
        Reduce process elements and build a value by the function
        :param f: Callable[[Any, int], Any]
        :param initial_state: int
        :return: int
        """
        state = initial_state
        i = 0
        while i < self.len:
            if self.hashTable[i] is not None:
                state = f(state, self.hashTable[i].value)
                i += 1
            else:
                i += 1
        return state

    def empty(self) -> None:
        """
        Data structure should be a monoid and implement empty
        :return: None
        """
        self.hashTable = [None for i in range(self.len)]

    def concat(self, dict_x: 'Dict') -> 'Dict':
        """
        Data structure should be a monoid and implement concat
        :param dict_x: Dict
        :return: Dict
        """
        self.dict_size = self.dict_size + dict_x.size()
        self.len = self.len + dict_x.len
        d1 = self.hashTable
        self.hashTable = [None for i in range(self.len)]
        for x in d1:
            if x is not None:
                self.add(x)
        for y in dict_x.hashTable:
            if y is not None:
                self.add(y)
        return self

    def __iter__(self) -> 'Next':
        """
        Data structure should be an iterator
        :return: Next
        """
        return Next(self.hashTable)


class Next:
    """To define a multi-iteration type,
    __iter__ is required to return a new iterator,
    not self, that is, not its own iterator."""
    def __init__(self, hashTable: list[Optional['Entry']]) -> None:
        """
        Create an instance of Next
        :param hashTable: list[Optional['Entry']
        """
        self.hashTable = hashTable
        self.current = 0

    def __iter__(self) -> 'Next':
        """
        Implement iter(self).
        :return: 'Next'
        """
        return self

    def __next__(self) -> 'Entry':
        """
        Implement next(self).
        :return: 'Entry'
        """
        if self.current < len(self.hashTable):
            x = self.current
            item = self.hashTable[x]
            self.current += 1
            return item
        else:
            raise StopIteration
