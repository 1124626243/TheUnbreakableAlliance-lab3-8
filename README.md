# TheUnbreakableAlliance-lab1-8

This is lab1 report.

## Variant

(8) Dictionary based on hash-map, open address

## laboratory work description

• Add a new element  (lst.add(3))
• Set an element with specific index / key (lst.set(1, 3)) if applicable.
• Remove an element by (lst.remove(3)):

- index for lists
- key for dictionaries - value for sets value

• Access:

- size (lst.size())
- is member (lst.member(3))
- reverse (lst.reverse() (if applicable)

• Conversion from/to built-in list :

- from_list (lst.from_list([12, 99, 37]))
- to_list (lst.to_list())

• Filter data structure by specific predicate (lst.filter(is_even))
• Map1 structure by specific function (lst.map(increment))
• Reduce2 – process structure elements to build a return value by specific functions(lst.reduce(sum))
• Data structure should be an iterator3 in Python style
• Data structure should be a monoid and implement empty and concat methods

## Project structure

- `Dict_mutable.py` -- implementation of `Dict` class with `remove` 、`add` etc.
- `Dict_mutable_test.py` -- unit and PBT tests for `Foo`.

## Features

- map(f)
- add(item)
- find(key)
- remove(key)
- size( )
- to_list( )
- from_list(a)
- filter(p)
- map(f)
- reduce(f, initial_state)
- empty( )
- concat(dict)
- get(key)
- member(key)
- __next__( )
- __iter__( )

## Contribution

- Fan Yuxin (1124626243@qq.com) -- Dict_mutable.py
- Wen Wenchao(285404190@qq.com) -- Dict_mutable.py

## Changelog

- 24.04.2022 - 2
- Wen Wenchao added `test_get()`, `test_member()`, 
- changed  `test_find()`, `test_remove()`.
- 24.04.2022 - 1
- Fan Yuxin add `get(key)`, `member(key)`, 
- change  `find(key)`, `remove(key)`,`from_list()`,`add(item)``concat(dict)`.
- 19.04.2022 - 2
- Wen Wenchao fixed `Dict_mutable_test.py`.
- 19.04.2022 - 1
- Fan Yuxin fixed `Dict_mutable.py`.
- 13.04.2022 - 2
- Wen Wenchao uploaded `Dict_mutable_test.py`.
- 13.04.2022 - 1
- Fan Yuxin uploaded `Dict_mutable.py`.
- 11.04.2022 - 0
  - Initial

## Design notes

We create an Entry class to represent an element in the dictionary.
Hash maps are used to store and find elements and open addressing
is used to handle conflicts. The internal hash table has a table length of 1000.
 
 ### Advantages and disadvantages of unittest

 * Advantages：
   * Support automated testing
   * Secondary development is convenient
   * Organize test cases together by class
 * Disadvantages：
   * Must be written in TestCase subclass
   * Must write test method
   * Difficult to expand

 ### Advantages and disadvantages of PBT tests

 * Advantages：
   * Check with automatically generated input data to ensure enough test cases
   * Allows developers to increase test coverage and effectively save time
 * Disadvantages：
   * Not covering all examples
