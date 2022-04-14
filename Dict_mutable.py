# Defines a dictionary element that consists of keywords and values
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Defining dictionary class
class Dict(object):
    def __init__(self, hashTable=[], size=0):
        # HashTable is a list of dictionaries to store
        if len(hashTable) == 0:
            self.hashTable = [None for i in range(size)]
        else:
            self.hashTable = hashTable
        #Dictionary size
        self.size = size
        # Used to record the current position
        self.current = 0

    # Hash mapping, where the key of a dictionary element is mapped to an address
    def hash_map(self, k, i):
        return (k % self.size + i * (1 + k % (self.size - 2))) % self.size

    # Add a new element. If a collision occurs, use linear probing in the open address method
    def dict_add(self, item):
        i=0
        while i < self.size:
            j = self.hash_map(item.key, i)
            if self.hashTable[j] is None:
                self.hashTable[j] = item
                return j
            else:
                i += 1
        return "dict overflow"

    # Find the element
    def dict_find(self, k):
        i = 0
        while i < self.size:
            if self.hashTable[i] is not None:
                if self.hashTable[i].key == k:
                    return i
            i += 1
        return None

    # Remove an element by key for dictionaries
    def dict_remove(self, item):
        index = self.dict_find(item.key)
        if index is not None:
            self.hashTable[index] = None
        else:
            return "element doesn't exist"
        return self.hashTable

    # Gets the size of the dictionary
    def dict_size(self):

        return self.size

    # Conversion to built-in list
    def dict_to_list(self):
        res = []
        i = 0
        while i < self.size:
            if self.hashTable[i] is not None:
                res.append(self.hashTable[i].value)
            else:
                res.append(self.hashTable[i])
            i += 1
        return res

    # Conversion from built-in list
    def dict_from_list(self, a):
        if len(a) == 0:
            self.hashTable = Dict().hashTable
            self.size = Dict().size
            return Dict()
        else:
            self.hashTable = Dict(a, len(a)).hashTable
            self.size = Dict(a, len(a)).size
            return Dict(a, len(a))

    # Filter out dictionary elements with values less than k
    def dict_filter(self, k):
        i = 0
        while i < self.size:
            if self.hashTable[i] is None:
                i += 1
            elif self.hashTable[i].value < k:
                self.hashTable[i] = None
                i += 1
            else:
                i += 1

    # Map structure by specific function
    def dict_map(self, f):
        i = 0
        while i < self.size:
            if self.hashTable[i] is not None:
                self.hashTable[i].value = f(self.hashTable[i].value)
                i += 1
            else:
                i += 1

    # Reduce – process structure elements to build a return value by specific functions
    def dict_reduce(self, f, initial_state):
        state = initial_state
        i = 0
        while i < self.size:
            if self.hashTable[i] is not None:
                state = f(state, self.hashTable[i].value)
                i += 1
            else:
                i += 1
        return state

    # Empty the dictionary
    def dict_empty(self):
        self.hashTable = [None for i in range(self.size)]

    # Join two dictionaries
    def dict_concat(self, dict):
        if self.size == 0:
            self.hashTable = Dict().hashTable
            self.size = Dict().size
        else:
            self.size += dict.size
            self.hashTable = self.hashTable + dict.hashTable

    # Make dictionaries iterable
    def __next__(self):
        if self.current < self.size:
            item = self.hashTable[self.current]
            self.current += 1
            #print(item.key)
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self
