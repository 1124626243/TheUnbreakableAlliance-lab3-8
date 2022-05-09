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
my_entry13 = Entry(3, 5)


class TestMutableDict(unittest.TestCase):
    def test_add(self):
        dict = Dict()
        self.assertEqual(dict.to_list(), {})
        dict.add(my_entry1)
        self.assertEqual(dict.to_list(), {3: 4})
        dict.add(my_entry2)
        self.assertEqual(dict.to_list(), {3: 4, 1004: 6})
        dict.add(my_entry3)
        self.assertEqual(dict.to_list(), {3: 4, 1004: 6, 7: 8})
        dict.add(my_entry13)
        self.assertEqual(dict.to_list(), {3: 4, 1004: 6, 3: 5, 7: 8})

    def test_remove(self):
        dict = Dict()
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        self.assertEqual(dict.to_list(), {3: 4, 1004: 6, 7: 8})
        dict.remove(my_entry3.key)
        self.assertEqual(dict.to_list(), {3: 4, 1004: 6})
        dict.remove(my_entry2.key)
        self.assertEqual(dict.to_list(), {3: 4})
        dict.remove(my_entry1.key)
        self.assertEqual(dict.to_list(), {})

    def test_size(self):
        dict = Dict()
        self.assertEqual(dict.size(), 0)
        dict1 = Dict()
        dict1.add(my_entry1)
        dict1.add(my_entry2)
        self.assertEqual(dict1.size(), 2)
        dict2 = Dict()
        dict2.add(my_entry1)
        dict2.add(my_entry2)
        dict2.add(my_entry3)
        self.assertEqual(dict2.size(), 3)

    def test_find(self):
        dict = Dict()
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        self.assertEqual(dict.find(my_entry1.key), 3)
        self.assertEqual(dict.find(my_entry2.key), 4)
        self.assertEqual(dict.find(my_entry3.key), 7)

    def test_filter(self):
        dict = Dict()
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        dict.add(my_entry10)
        dict.filter(lambda e: e % 2 == 1)
        self.assertEqual(dict.to_list(), {8: 9})

    def test_map(self):
        dict = Dict()
        dict.map(lambda e: e*2)
        self.assertEqual(dict.to_list(), {})
        dict1 = Dict()

        dict1.add(my_entry4)
        dict1.add(my_entry5)
        dict1.add(my_entry6)
        dict1.map(lambda e: e*2)
        self.assertEqual(dict1.to_list(), {3: 8, 5: 12, 7: 16})

    def test_reduce(self):
        dict = Dict()
        self.assertEqual(dict.reduce(lambda a, e: a + e, 0), 0)
        dict1 = Dict()
        dict1.add(my_entry7)
        dict1.add(my_entry8)
        dict1.add(my_entry9)
        self.assertEqual(dict1.reduce(lambda a, e: a + e, 0), 18)

    def test_mempty(self):
        dict = Dict()
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        dict.empty()
        self.assertEqual(dict.to_list(), {})

    def test_concat(self):
        dict = Dict()
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)

        dict1 = Dict()
        dict1.add(my_entry10)
        dict1.add(my_entry11)
        dict1.add(my_entry12)
        x = dict.concat(dict1)
        self.assertEqual(x.to_list(), {3: 4, 1004: 6, 7: 8,
                                          8: 9, 14: 15, 15: 16})

    def test_to_list(self):
        dict = Dict()
        self.assertEqual(dict.to_list(), {})
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        self.assertEqual(dict.to_list(), {3: 4, 1004: 6, 7: 8})

    def test_from_list(self):
        test_data = {3: 4, 1004: 6, 7: 8}
        dict = Dict()
        dict.from_list(test_data)
        self.assertEqual(dict.to_list(), {3: 4, 1004: 6, 7: 8})
        test_data1 = {0: 0, 1000: 0}
        dict1 = Dict()
        dict1.from_list(test_data1)
        self.assertEqual(dict1.to_list(), {0: 0, 1000: 0})

    def test_get(self):
        dict = Dict()
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        self.assertEqual(dict.get(3), 4)

    def test_member(self):
        dict = Dict()
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        self.assertEqual(dict.member(3), 1)
        self.assertEqual(dict.member(100), 0)

    @given(st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)))
    def test_from_list_to_list_equality(self, a):
        dict = Dict()
        dict.from_list(a)
        b = dict.to_list()
        self.assertEqual(a, b)

    @given(st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)))
    def test_python_len_and_list_size_equality(self, a):
        dict = Dict()
        dict.from_list(a)
        self.assertEqual(dict.size(), len(a))

    @given(st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)))
    def test_monoid_identity(self, a):
        #  a•e = a
        dict = Dict()
        dict.from_list(a)
        empty_dict = Dict()
        x = dict.concat(empty_dict)
        self.assertEqual(dict.to_list(), x.to_list())
        # e•a = a
        y = empty_dict.concat(dict)
        self.assertEqual(dict.to_list(), y.to_list())

    @given(st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)),
           st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0)),
           st.dictionaries(keys=st.integers(min_value=0),
                           values=st.integers(min_value=0))
           )
    def test_monoid_associativity(self, a, b, c):
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
