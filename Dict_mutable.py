# Defines a dictionary element that consists of keywords and values
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Defining dictionary class
class Dict(object):
    def __init__(self, size=0):
        # HashTable is a list of dictionaries to store
        self.hashTable = [None for i in range(size)]
        # Dictionary size
        self.dict_size = size
        # Used to record the current position
        # self.current = 0

    # Hash mapping
    def hash_map(self, k, i):
        return (k % self.dict_size + i * (1 + k % (self.dict_size - 2))) % self.dict_size

    # Add a new element
    def add(self, item):
        i = 0
        while i < self.dict_size:
            j = self.hash_map(item.key, i)
            if self.hashTable[j] is None:
                self.hashTable[j] = item
                return j
            else:
                i += 1
        return "dict overflow"

    # Find the element
    def find(self, k):
        i = 0
        while i < self.dict_size:
            if self.hashTable[i] is not None:
                if self.hashTable[i].key == k:
                    return i
            i += 1
        return None

    # Remove an element by key for dictionaries
    def remove(self, item):
        index = self.find(item.key)
        if index is not None:
            self.hashTable[index] = None
        else:
            return "element doesn't exist"
        return self.hashTable

    # Gets the size of the dictionary
    def size(self):

        return self.dict_size

    # Conversion to built-in list
    def to_list(self):
        res = []
        i = 0
        while i < self.dict_size:
            if self.hashTable[i] is not None:
                res.append(self.hashTable[i].value)
            else:
                res.append(self.hashTable[i])
            i += 1
        return res

    # Conversion from built-in list
    def from_list(self, a):
        dict1 = Dict(len(a))
        for x in a:
            dict1.add(x)
        return dict1

    # Filter dictionary by specific predicate
    def filter(self, p):
        i = 0
        while i < self.dict_size:
            if self.hashTable[i] is None:
                i += 1
            elif not p(self.hashTable[i].value):
                self.hashTable[i] = None
                i += 1
            else:
                i += 1

    # Map structure by specific function
    def map(self, f):
        i = 0
        while i < self.dict_size:
            if self.hashTable[i] is not None:
                self.hashTable[i].value = f(self.hashTable[i].value)
                i += 1
            else:
                i += 1

    # Reduce
    def reduce(self, f, initial_state):
        state = initial_state
        i = 0
        while i < self.dict_size:
            if self.hashTable[i] is not None:
                state = f(state, self.hashTable[i].value)
                i += 1
            else:
                i += 1
        return state

    # Empty the dictionary
    def empty(self):
        self.hashTable = [None for i in range(self.dict_size)]

    # Join two dictionaries
    def concat(self, dict):
        if self.dict_size == 0:
            self.hashTable = Dict().hashTable
            self.dict_size = Dict().size
        else:
            self.dict_size += dict.size()
            self.hashTable = self.hashTable + dict.hashTable

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


'''To define a multi-iteration type, __iter__ is required to return a new iterator, not self, 
that is, not its own iterator.'''


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


'''
my_dict = Dict(5)
my_entry1 = Entry(3, 1)
my_entry2 = Entry(5, 2)
my_entry3 = Entry(7, 3)
my_entry4 = Entry(7, 4)
my_entry5 = Entry(7, 5)

my_dict.add(my_entry1)
my_dict.add(my_entry2)
my_dict.add(my_entry3)
my_dict.add(my_entry4)
my_dict.add(my_entry5)'''


'''
for x in my_dict:
    print(x.value)

i1 = iter(my_dict)
i2 = iter(my_dict)

print(next(i1).value)  # -> 2
print(next(i1).value)  # -> 5
print(next(i2).value)  # -> 2
print(next(i2).value)  # -> 5
print(next(i1).value)  # -> 3
'''