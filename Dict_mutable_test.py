# Author: Fan Yuxin, Weng Wenchao
import unittest
from Dict_mutable import *


my_entry1 = Entry(3, 4)
my_entry2 = Entry(5, 6)
my_entry3 = Entry(7, 8)


class TestMutabledict(unittest.TestCase):
    def test_add(self):
        dict = Dict(3)
        self.assertEqual(dict.to_list(), [None, None, None])
        dict.add(my_entry1)
        self.assertEqual(dict.to_list(), [4, None, None])
        dict.add(my_entry2)
        self.assertEqual(dict.to_list(), [4, None, 6])
        dict.add(my_entry3)
        self.assertEqual(dict.to_list(), [4, 8, 6])

    def test_remove(self):
        dict = Dict(3)
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        self.assertEqual(dict.to_list(), [4, 8, 6])
        dict.remove(my_entry3)
        self.assertEqual(dict.to_list(), [4, None, 6])
        dict.remove(my_entry2)
        self.assertEqual(dict.to_list(), [4, None, None])
        dict.remove(my_entry1)
        self.assertEqual(dict.to_list(), [None, None, None])

    def test_size(self):
        dict = Dict(0)
        self.assertEqual(dict.size(), 0)
        dict = Dict(1)
        self.assertEqual(dict.size(), 1)
        dict = Dict(2)
        self.assertEqual(dict.size(), 2)

    def test_to_list(self):
        dict = Dict(3)
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        self.assertEqual(dict.to_list(), [4, 8, 6])

    def test_find(self):
        dict = Dict(3)
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        self.assertEqual(dict.find(my_entry1.key), 0)
        self.assertEqual(dict.find(my_entry3.key), 1)
        self.assertEqual(dict.find(my_entry2.key), 2)

    def test_filter(self):
        dict = Dict(3)
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        dict.filter(lambda e:e % 2 == 0)
        self.assertEqual(dict.to_list(), [4, 8, 6])
        dict.filter(lambda e:e % 2 == 1)
        self.assertEqual(dict.to_list(), [None, None, None])

    def test_map(self):
        dict = Dict()
        dict.map(lambda e: e*2)
        self.assertEqual(dict.to_list(), [])
        dict = Dict(3)
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        dict.map(lambda e: e*2)
        self.assertEqual(dict.to_list(), [8, 16, 12])

    def test_reduce(self):
        dict = Dict()
        self.assertEqual(dict.reduce(lambda st, e: st + e, 0), 0)
        dict = Dict(3)
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        self.assertEqual(dict.reduce(lambda st, e: st + e, 0), 18)

    def test_mempty(self):
        dict = Dict(3)
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)
        dict.empty()
        self.assertEqual(dict.to_list(), [None, None, None])

    def test_concat(self):
        dict = Dict(3)
        dict.add(my_entry1)
        dict.add(my_entry2)
        dict.add(my_entry3)

        dict1 = Dict(3)
        dict1.add(my_entry1)
        dict1.add(my_entry2)
        dict1.add(my_entry3)
        # dict1 = dict1.to_list()
        dict.concat(dict1)
        self.assertEqual(dict.to_list(), [4, 8, 6, 4, 8, 6])

    def test_from_list(self):
        test_data = [
            [my_entry1],
            [my_entry1, my_entry3, my_entry2]
        ]
        for e in test_data:
            dict = Dict()
            dict = dict.from_list(e)
            self.assertEqual(dict.to_list(), [i.value for i in e])


if __name__ == '__main__':
    unittest.main()
