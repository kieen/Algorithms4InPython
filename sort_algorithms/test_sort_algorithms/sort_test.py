import unittest
from selection_sort import SelectionSort
import sort_utils
from insertion_sort import InsertionSort
import random
from shell_sort import ShellSort
from h_insertion_sort import HInsertionSort


class SortTest(unittest.TestCase):
    """ test sort algorithms"""
    
    def get_random_list(self):
        """ return a random list"""
        
        return random.sample(range(100), 10)
            
    def test_SelectionSort(self):
        a = self.get_random_list()
        SelectionSort.sort(a)
        print(a)
        self.assertTrue(sort_utils.is_sorted(a))

    def test_InsertionSort(self):
        a = self.get_random_list()
        InsertionSort.sort(a)
        print(a)
        self.assertTrue(sort_utils.is_sorted(a))
    
    def test_HInsertionSort(self):
        a = self.get_random_list()
        h= random.randint(1,len(a)-1)
        HInsertionSort.sort(a,h)
        print(a)
        self.assertTrue(sort_utils.is_h_sorted(a, h))
    
    def test_ShellSort(self):
        a = self.get_random_list()
        ShellSort.sort(a)
        print(a)
        self.assertTrue(sort_utils.is_sorted(a))
