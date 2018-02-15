"""this module has some utilities for sort algorithm"""

def is_sorted(a):
    ''' check if a is sorted'''
    n = len(a)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            return False
    return True


def is_h_sorted(a, h):
    ''' check if a is h-sorted'''
    n = len(a)
    for i in range(h, n):
        if a[i] < a[i - h]:
            return False
    return True


def exchange(a, i, j):
        """  exchange/swap a[i] and a[j] written in the pythonic way.
        Alternatively, you can use a temporary variable as usual:
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
        """
        a[i], a[j] = a[j], a[i]
        
