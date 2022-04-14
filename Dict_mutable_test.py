#Author: Fan Yuxin, Weng Wenchao
import unittest
from Dict_mutable import *
from hypothesis import given
import hypothesis.strategies as st


my_entry1 = Entry(3, 4)
my_entry2 = Entry(5, 6)
my_entry3 = Entry(7, 8)



class TestMutabledict(unittest.TestCase):
    def test_dict_add(self):
        T = []
        dict = Dict(T, 3)
        self.assertEqual(dict.dict_to_list(), [None, None, None])
        dict.dict_add(my_entry1)
        self.assertEqual(dict.dict_to_list(), [4, None, None])
        dict.dict_add(my_entry2)
        self.assertEqual(dict.dict_to_list(), [4, None, 6])
        dict.dict_add(my_entry3)
        self.assertEqual(dict.dict_to_list(), [4, 8, 6])

    def test_dict_remove(self):
        T = [my_entry1,my_entry3,my_entry2]
        dict = Dict(T, 3)
        self.assertEqual(dict.dict_to_list(), [4, 8, 6])
        dict.dict_remove(my_entry3)
        self.assertEqual(dict.dict_to_list(), [4, None, 6])
        dict.dict_remove(my_entry2)
        self.assertEqual(dict.dict_to_list(), [4, None, None])
        dict.dict_remove(my_entry1)
        self.assertEqual(dict.dict_to_list(), [None, None, None])

    def test_dict_size(self):
        T = []
        dict = Dict(T, 0)
        self.assertEqual(dict.dict_size(), 0)
        dict = Dict(T, 1)
        self.assertEqual(dict.dict_size(), 1)
        dict = Dict(T, 2)
        self.assertEqual(dict.dict_size(), 2)

    def test_dict_to_list(self):
        T = [my_entry1,my_entry3,my_entry2]
        dict = Dict(T, 3)
        self.assertEqual(dict.dict_to_list(), [4, 8, 6])

    def test_dict_find(self):
        T = [my_entry1,my_entry3,my_entry2]
        dict = Dict(T, 3)
        self.assertEqual(dict.dict_find(my_entry1.key), 0)
        self.assertEqual(dict.dict_find(my_entry3.key), 1)
        self.assertEqual(dict.dict_find(my_entry2.key), 2)

    def test_dict_filter(self):
        T = [my_entry1,my_entry3,my_entry2]
        dict = Dict(T, 3)
        dict.dict_filter(5)
        self.assertEqual(dict.dict_to_list(), [None, 8, 6])
        dict.dict_filter(7)
        self.assertEqual(dict.dict_to_list(), [None, 8, None])

    def test_dict_map(self):
        T = []
        dict = Dict(T)
        dict.dict_map(lambda e: e*2)
        self.assertEqual(dict.dict_to_list(), [])
        T = [Entry(3, 4), Entry(7, 8), Entry(5, 6)]
        dict = Dict(T, 3)
        dict.dict_map(lambda e: e*2)
        self.assertEqual(dict.dict_to_list(), [8, 16, 12])

    def test_dict_reduce(self):
        T = []
        dict = Dict(T)
        self.assertEqual(dict.dict_reduce(lambda st, e: st + e, 0), 0)
        T = [my_entry1, my_entry3, my_entry2]
        dict = Dict(T, 3)
        self.assertEqual(dict.dict_reduce(lambda st, e: st + e, 0), 18)

    def test_dict_mempty(self):
        T = [my_entry1, my_entry3, my_entry2]
        dict = Dict(T, 3)
        dict.dict_empty()
        self.assertEqual(dict.dict_to_list(), [None, None, None])

    def test_dict_concat(self):
        T = [my_entry1, my_entry3, my_entry2]
        dict = Dict(T, 3)
        T1= [my_entry1, my_entry3]
        dict1 = Dict(T1, 2)
        #dict1 = dict1.dict_to_list()
        dict.dict_concat(dict1)
        self.assertEqual(dict.dict_to_list(), [4, 8, 6, 4, 8])

    def test_dict_from_list(self):
        test_data = [
            [my_entry1],
            [my_entry1, my_entry3],
            [my_entry1, my_entry3, my_entry2]
        ]
        for e in test_data:
            dict = Dict()
            dict = dict.dict_from_list(e)
            self.assertEqual(dict.dict_to_list(), [i.value for i in e])



if __name__ == '__main__':
    unittest.main()
