# Defines a dictionary element that consists of keywords and values
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Defining dictionary class
class Dict(object):
    def __init__(self):
        # The length of the hashTable
        self.len = 1000
        # HashTable is a list of dictionaries to store
        self.hashTable = [None for i in range(self.len)]
        # Dictionary size
        self.dict_size = 0

    # Add a new element，use linear detection for conflicts
    def add(self, item):
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
                    print("Failed to insert because hashTable is full")
                    break
            self.hashTable[j] = item
            self.dict_size += 1

    # Find the element
    def find(self, key):
        return key % self.len

    # Remove an element by key for dictionaries
    def remove(self, item):
        index = self.find(item.key)
        if self.hashTable[index] is not None:
            self.hashTable[index] = None
            self.dict_size -= 1
        else:
            return "element doesn't exist"

    # Gets the size of the dictionary
    def size(self):
        return self.dict_size

    # Conversion to built-in list
    def to_list(self):
        res = {}
        i = 0
        while i < self.len:
            if self.hashTable[i] is not None:
                res[self.hashTable[i].key] = self.hashTable[i].value
            i += 1
        return res

    # Conversion from built-in list
    def from_list(self, a):
        dict1 = Dict()
        for key, value in a.items():
            x = Entry(key, value)
            dict1.add(x)
        return dict1

    # Filter dictionary by specific predicate
    def filter(self, p):
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

    # Map structure by specific function
    def map(self, f):
        i = 0
        while i < self.len:
            if self.hashTable[i] is not None:
                self.hashTable[i].value = f(self.hashTable[i].value)
                i += 1
            else:
                i += 1

    # Reduce
    def reduce(self, f, initial_state):
        state = initial_state
        i = 0
        while i < self.len:
            if self.hashTable[i] is not None:
                state = f(state, self.hashTable[i].value)
                i += 1
            else:
                i += 1
        return state

    # Empty the dictionary
    def empty(self):
        self.hashTable = [None for i in range(self.len)]

    # Join two dictionaries
    def concat(self, dict):
        self.dict_size += dict.size()
        self.len += dict.len
        self.hashTable += dict.hashTable

    # Make dictionaries iterable
    '''def __next__(self):
        if self.current < self.dict_size:
            x = self.current
            item = self.hashTable[x]
            self.current += 1
            # print(item.key)
            return item
        else:
            raise StopIteration'''

    def __iter__(self):
        return Next(self.hashTable)


'''To define a multi-iteration type,
__iter__ is required to return a new iterator,
not self, that is, not its own iterator.'''


class Next:
    def __init__(self, hashTable):
        self.hashTable = hashTable
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.hashTable):
            x = self.current
            item = self.hashTable[x]
            self.current += 1
            # print(item.key)
            return item
        else:
            raise StopIteration
