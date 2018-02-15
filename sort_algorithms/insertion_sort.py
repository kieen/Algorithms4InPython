import sort_utils


class InsertionSort(object):
    """ implementation of insertion sort"""
    
    @staticmethod
    def sort(a):
        n = len(a)
        for i in range(1, n):
            j = i 
            while (j > 0) and (a[j] < a[j - 1]):
                sort_utils.exchange(a, j, j - 1)
                j -= 1
            """ Note that if one "literally translate" the Java code in the slide/book, it won't work. 
            The resulting translation will be as follows:
            #===================================================================
            # for j in range(i, 1, -1):
            #     if a[j] < a[j - 1]:
            #         sort_utils.exchange(a, j, j - 1)
            #     else: 
            #         break
            #         
            #===================================================================
            In the case where i=1, rang(1,1-1) return empty list, which could result in the wrong position of a[1]
            """
