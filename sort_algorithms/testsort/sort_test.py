import unittest
from selection_sort import SelectionSort
import sort_utils

class SortTest(unittest.TestCase):

    def test_SelectionSort(self):
        a = [4, 3, 2, 1]
        SelectionSort().sort(a)
        print(a)
        sort_utils.is_sorted(a)
