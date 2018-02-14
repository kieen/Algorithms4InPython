import unittest
from sort_algorithms.selection_sort import SelectionSort
from sort_algorithms import sort_utils


class SelectionSortTest(unittest.TestCase):

    def test_sort(self):
        a = [4, 3, 2, 1]
        SelectionSort().sort(a)
        print(a)
        sort_utils.is_sorted(a)
