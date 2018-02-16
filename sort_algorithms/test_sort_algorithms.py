import random
import unittest

from sort_algorithms.selection_sort import SelectionSort
from sort_algorithms import sort_utils
from sort_algorithms.insertion_sort import InsertionSort
from sort_algorithms.h_insertion_sort import HInsertionSort
from sort_algorithms.shell_sort import ShellSort

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
