class MergeSort(object):
    """ implementation of the non-optimized algorithm of MergeSort. 
    Ref: https://algs4.cs.princeton.edu/22mergesort/
    """
    
    @staticmethod
    def sort(a):
        aux = list(a)
        MergeSort.merge_sort(a, aux, 0, len(a) - 1)
        
    @staticmethod
    def merge_sort(a, aux, lo, hi):
        ''' recursive merge sort. To avoid overloading we use the name merge_sort instead of sort as in the lecture'''
        
        if (lo < hi):
            mid = lo + (hi - lo) // 2
            MergeSort.merge_sort(a, aux, lo, mid)
            MergeSort.merge_sort(a, aux, mid + 1, hi)
            MergeSort.merge(a, aux, lo, mid, hi)

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
        

if __name__ == '__main__':
    a = [9, 8, 5,6,7, 4, 3, 2, 1]
    MergeSort.sort(a)
    print(a)
                
