import random
import unittest

from sort_algorithms import sort_utils
from sort_algorithms.selection_sort import SelectionSort
from sort_algorithms.insertion_sort import InsertionSort
from sort_algorithms.h_insertion_sort import HInsertionSort
from sort_algorithms.shell_sort import ShellSort
from sort_algorithms.merge_sort import MergeSort
from sort_algorithms.merge_sort_x import MergeSortX

class SortTest(unittest.TestCase):
    """ test merge_sort algorithms"""
    
    def get_random_list(self):
        """ return a random list"""
        
        return random.sample(range(1000), 100)
            
    def test_SelectionSort(self):
        a = self.get_random_list()
        SelectionSort.sort(a)
        self.assertTrue(sort_utils.is_sorted(a))

    def test_InsertionSort(self):
        a = self.get_random_list()
        InsertionSort.sort(a)
        self.assertTrue(sort_utils.is_sorted(a))
    
    def test_HInsertionSort(self):
        a = self.get_random_list()
        h= random.randint(1,len(a)-1)
        HInsertionSort.sort(a,h)
        self.assertTrue(sort_utils.is_h_sorted(a, h))
    
    def test_ShellSort(self):
        a = self.get_random_list()
        ShellSort.sort(a)
        self.assertTrue(sort_utils.is_sorted(a))
        
    def test_MergeSort(self):
        a = self.get_random_list()
        MergeSort.sort(a)
        self.assertTrue(sort_utils.is_sorted(a))
        
    def test_MergeSortX(self):
        a = self.get_random_list()
        MergeSortX.sort(a)
        self.assertTrue(sort_utils.is_sorted(a))
