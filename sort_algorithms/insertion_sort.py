# import sort_algorithms.sort_utils
from sort_algorithms import sort_utils


class InsertionSort(object):
    """ implementation of insertion merge_sort"""
    
    @staticmethod
    def sort(a):
        n = len(a)
        for i in range(1, n):
            j = i 
            while (j > 0) and (a[j] < a[j - 1]):
                sort_utils.exchange(a, j, j - 1)
                j -= 1
            """ Note that if one use the for loop in python to "literally translate" the Java code in the slide/book, 
            it won't work. The resulting translation will be as follows:
            #===================================================================
            # for j in range(i, 2, -1):
            #     if a[j] < a[j - 1]:
            #         sort_utils.exchange(a, j, j - 1)
            #     else: 
            #         break
            #         
            #===================================================================
            range(i,2,-1) is used to get [i,i-1,....1].
            But for i=1 or 2, range(1,2,-1) and range(2,2,-1) return empty list
            """


if __name__ == '__main__':
    a = [9, 8, 5, 6, 7, 4, 3, 2, 1]
    InsertionSort.sort(a)
    print(a)
