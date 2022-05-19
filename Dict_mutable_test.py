import unittest
from Dict_mutable import Entry, Dict
from hypothesis import given
import hypothesis.strategies as st

my_entry1 = Entry(3, 4)
my_entry2 = Entry(1004, 6)
my_entry3 = Entry(7, 8)
my_entry4 = Entry(3, 4)
my_entry5 = Entry(5, 6)
my_entry6 = Entry(7, 8)
my_entry7 = Entry(3, 4)
my_entry8 = Entry(5, 6)
my_entry9 = Entry(7, 8)
my_entry10 = Entry(8, 9)
my_entry11 = Entry(14, 15)
my_entry12 = Entry(15, 16)


class TestMutableDict(unittest.TestCase):
    def test_add(self) -> None:
        dict_x = Dict()
        self.assertEqual(dict_x.to_list(), {})
        dict_x.add(my_entry1)
        self.assertEqual(dict_x.to_list(), {3: 4})
        dict_x.add(my_entry2)
        self.assertEqual(dict_x.to_list(), {3: 4, 1004: 6})
        dict_x.add(my_entry3)
        self.assertEqual(dict_x.to_list(), {3: 4, 1004: 6, 7: 8})

    def test_remove(self) -> None:
        dict_x = Dict()
        dict_x.add(my_entry1)
        dict_x.add(my_entry2)
        dict_x.add(my_entry3)
        self.assertEqual(dict_x.to_list(), {3: 4, 1004: 6, 7: 8})
        dict_x.remove(my_entry3.key)
        self.assertEqual(dict_x.to_list(), {3: 4, 1004: 6})
        dict_x.remove(my_entry2.key)
        self.assertEqual(dict_x.to_list(), {3: 4})
        dict_x.remove(my_entry1.key)
        self.assertEqual(dict_x.to_list(), {})

    def test_size(self) -> None:
        dict_x = Dict()
        self.assertEqual(dict_x.size(), 0)
        dict1 = Dict()
        dict1.add(my_entry1)
        dict1.add(my_entry2)
        self.assertEqual(dict1.size(), 2)
        dict2 = Dict()
        dict2.add(my_entry1)
        dict2.add(my_entry2)
        dict2.add(my_entry3)
        self.assertEqual(dict2.size(), 3)

    def test_find(self) -> None:
        dict_x = Dict()
        dict_x.add(my_entry1)
        dict_x.add(my_entry2)
        dict_x.add(my_entry3)
        self.assertEqual(dict_x.find(my_entry1.key), 3)
        self.assertEqual(dict_x.find(my_entry2.key), 4)
        self.assertEqual(dict_x.find(my_entry3.key), 7)

    def test_filter(self) -> None:
        dict_x = Dict()
        dict_x.add(my_entry1)
        dict_x.add(my_entry2)
        dict_x.add(my_entry3)
        dict_x.add(my_entry10)
        dict_x.filter(lambda e: e % 2 == 1)
        self.assertEqual(dict_x.to_list(), {8: 9})

    def test_map(self) -> None:
        dict_x = Dict()
        dict_x.map(lambda e: e * 2)
        self.assertEqual(dict_x.to_list(), {})
        dict1 = Dict()

        dict1.add(my_entry4)
        dict1.add(my_entry5)
        dict1.add(my_entry6)
        dict1.map(lambda e: e*2)
        self.assertEqual(dict1.to_list(), {3: 8, 5: 12, 7: 16})

    def test_reduce(self) -> None:
        dict_x = Dict()
        self.assertEqual(dict_x.reduce(lambda a, e: a + e, 0), 0)
        dict1 = Dict()
        dict1.add(my_entry7)
        dict1.add(my_entry8)
        dict1.add(my_entry9)
        self.assertEqual(dict1.reduce(lambda a, e: a + e, 0), 18)

    def test_mempty(self) -> None:
        dict_x = Dict()
        dict_x.add(my_entry1)
        dict_x.add(my_entry2)
        dict_x.add(my_entry3)
        dict_x.empty()
        self.assertEqual(dict_x.to_list(), {})

    def test_concat(self) -> None:
        dict_x = Dict()
        dict_x.add(my_entry1)
        dict_x.add(my_entry2)
        dict_x.add(my_entry3)

        dict1 = Dict()
        dict1.add(my_entry10)
        dict1.add(my_entry11)
        dict1.add(my_entry12)
        x = dict_x.concat(dict1)
        self.assertEqual(x.to_list(), {3: 4, 1004: 6, 7: 8,
                                       8: 9, 14: 15, 15: 16})

    def test_to_list(self) -> None:
        dict_x = Dict()
        self.assertEqual(dict_x.to_list(), {})
        dict_x.add(my_entry1)
        dict_x.add(my_entry2)
        dict_x.add(my_entry3)
        self.assertEqual(dict_x.to_list(), {3: 4, 1004: 6, 7: 8})

    def test_from_list(self) -> None:
        test_data = {3: 4, 1004: 6, 7: 8}
        dict_x = Dict()
        dict_x.from_list(test_data)
        self.assertEqual(dict_x.to_list(), {3: 4, 1004: 6, 7: 8})
        test_data1 = {0: 0, 1000: 0}
        dict1 = Dict()
        dict1.from_list(test_data1)
        self.assertEqual(dict1.to_list(), {0: 0, 1000: 0})

    def test_get(self) -> None:
        dict_x = Dict()
        dict_x.add(my_entry1)
        dict_x.add(my_entry2)
        dict_x.add(my_entry3)
        self.assertEqual(dict_x.get(3), 4)

    def test_member(self) -> None:
        dict_x = Dict()
        dict_x.add(my_entry1)
        dict_x.add(my_entry2)
        dict_x.add(my_entry3)
        self.assertEqual(dict_x.member(3), 1)
        self.assertEqual(dict_x.member(100), 0)

    @given(st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)))
    def test_from_list_to_list_equality(self, a) -> None:
        dict_x = Dict()
        dict_x.from_list(a)
        b = dict_x.to_list()
        self.assertEqual(a, b)

    @given(st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)))
    def test_python_len_and_list_size_equality(self, a) -> None:
        dict_x = Dict()
        dict_x.from_list(a)
        self.assertEqual(dict_x.size(), len(a))

    @given(st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)))
    def test_monoid_identity(self, a) -> None:
        #  a•e = a
        dict_x = Dict()
        dict_x.from_list(a)
        empty_dict = Dict()
        x = dict_x.concat(empty_dict)
        self.assertEqual(dict_x.to_list(), x.to_list())
        # e•a = a
        y = empty_dict.concat(dict_x)
        self.assertEqual(dict_x.to_list(), y.to_list())

    @given(st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)),
           st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)),
           st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0))
           )
    def test_monoid_associativity(self, a, b, c) -> None:
        dict1 = Dict()
        dict1.from_list(a)
        dict2 = Dict()
        dict2.from_list(b)
        dict3 = Dict()
        dict3.from_list(c)
        # (a•b)•c
        x = dict1.concat(dict2).concat(dict3)
        # a•(b•c)
        y = dict1.concat(dict2.concat(dict3))
        self.assertEqual(x.to_list(), y.to_list())


if __name__ == '__main__':
    unittest.main()
