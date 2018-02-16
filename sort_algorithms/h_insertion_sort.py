from sort_algorithms import sort_utils


class HInsertionSort(object):
    """ implementation of insertion merge_sort for h-merge_sort"""
    
    @staticmethod
    def sort(a, h):
        n = len(a)
        for i in range(h, n):
            j = i 
            while (j >= h) and (a[j] < a[j - h]):
                sort_utils.exchange(a, j, j - h)
                j -= h

            
if __name__ == '__main__':
    a = [9, 8, 5, 6, 7, 4, 3, 2, 1]
    HInsertionSort.sort(a, 3)
    print(a)
