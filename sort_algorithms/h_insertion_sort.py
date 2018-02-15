import sort_utils


class HInsertionSort(object):
    """ implementation of insertion sort for h-sort"""
    
    @staticmethod
    def sort(a, h):
        n = len(a)
        for i in range(h, n):
            j = i 
            while (j >= h) and (a[j] < a[j - h]):
                sort_utils.exchange(a, j, j - h)
                j -= h

            
if __name__ == '__main__':
    a = [4, 1, 2, 3]
    HInsertionSort.sort(a, 2)
    print(a)
