# TheUnbreakableAlliance-lab1-8

This is lab1report.

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

- hash_map(k, i)
- dict_add(item)
- dict_find(k)
- dict_remove(item)
- dict_size( )
- dict_to_list( )
- dict_from_list(a)
- dict_filter(k)
- dict_map(f)
- dict_reduce(f, initial_state)
- dict_empty( )
- dict_concat(dict)
- __next__( )
- __iter__( )

## Contribution

- Fan Yuxin (1124626243@qq.com) -- Dict_mutable.py
- Wen Wenchao(285404190@qq.com) -- Dict_mutable.py

## Changelog

- 19.04.2022 - 2
- Wen Wenchao fix `Dict_mutable_test.py`.
- 19.04.2022 - 1
- Fan Yuxin fix `Dict_mutable.py`.
- 13.04.2022 - 2
- Wen Wenchao upload `Dict_mutable_test.py`.
- 13.04.2022 - 1
- Fan Yuxin upload `Dict_mutable.py`.
- 11.04.2022 - 0
  - Initial

## Design notes

We create an Entry class to represent an element in the dictionary.
Hash maps are used to store and find elements and open addressing
 is used to handle conflicts.
