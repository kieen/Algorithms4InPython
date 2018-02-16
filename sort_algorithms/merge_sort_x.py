from sort_algorithms import sort_utils


class MergeSortX(object):
    """ implementation of MergeSort with optimizations: 
    cut-off; check if already sorted
    Ref 1: https://algs4.cs.princeton.edu/22MergeSort/
    Ref 2: lecture notes in Week 3: https://www.coursera.org/learn/algorithms-part1
    I did not implement the optimization that swap a and aux as I think it does not make much sense. 
    In any case, we only copy n times totally, with n is the number of elements. And I don't see why swapping a and aux helps.
    """
    CUT_OFF = 7
    
    @staticmethod
    def sort(a):
        aux = list(a)
        MergeSortX.merge_sort(a, aux, 0, len(a) - 1)
        
    @staticmethod
    def merge_sort(a, aux, lo, hi):
        ''' recursive merge sort. To avoid overloading we use the name merge_sort instead of sort as in the lecture'''
        if lo >= hi:
            return
        
        # Optimization 1: cut-off if the size of the subarray is <=7
        if (hi - lo + 1) <= MergeSortX.CUT_OFF:
            MergeSortX.insertion_sort(a, lo, hi)
            return
        
        mid = lo + (hi - lo) // 2
        MergeSortX.merge_sort(a, aux, lo, mid)
        MergeSortX.merge_sort(a, aux, mid + 1, hi)
        
        # Optimization 2: don't need to merge if a[lo]... a[hi] is already sorted
        if a[mid] <= a[mid + 1]:
            return
        MergeSortX.merge(a, aux, lo, mid, hi)

    @staticmethod
    def merge(a, aux, lo, mid, hi):
        ''' merge_sort two sorted parts of a: 
        the left part: a[lo] ...a[mid] 
        the right part: a[mid+1] ...a[hi]
        '''
               
        aux[lo:hi + 1] = a[lo:hi + 1]
        index_a = lo
        index_left = lo
        index_right = mid + 1
        
        for index_a in range(lo, hi + 1):
            if index_left > mid:
                a[index_a] = aux[index_right]
                index_right += 1
            elif index_right > hi:
                a[index_a] = aux[index_left]
                index_left += 1
            elif aux[index_left] < aux[index_right]:
                a[index_a] = aux[index_left]
                index_left += 1
            else:
                a[index_a] = aux[index_right]
                index_right += 1   

    @staticmethod
    def insertion_sort(a, lo, hi):
        ''' insertion sort on part of a: a[lo] ... a[hi]'''
        for i in range(lo + 1, hi + 1):
            j = i
            while (j > lo) and (a[j] < a[j - 1]):
                sort_utils.exchange(a, j, j - 1)
                j -= 1


if __name__ == '__main__':
    a = [9, 8, 5, 6, 7, 4, 3, 2, 1]
    MergeSortX.sort(a)
    print(a)
                
