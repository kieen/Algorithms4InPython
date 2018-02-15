from h_insertion_sort import HInsertionSort


class ShellSort(object):
    """ implementation of shell sort with the sequence 3h+1"""

    @staticmethod
    def sort(a):
        """ sort a """
        
        n = len(a)
        # Get 3h+1 sequence
        h = 1;
        while h < n // 3:
            h = h * 3 + 1
        
        # Perform h-sort
        while h > 0:
            HInsertionSort.sort(a, h)
            h = h // 3
   

if __name__ == '__main__':
    a = [4, 1, 2, 3]
    ShellSort.sort(a)
    print(a)
