class SelectionSort(object):
    """ implementation of selection sort"""

    @staticmethod
    def sort(a):
        """ sort a """
        n = len(a)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if a[min_index] > a[j]:
                    min_index = j
            if a[i] > a[min_index]:
                SelectionSort._exchange(a, i, min_index)

    @staticmethod
    def _exchange(a, i, j):
        """  exchange a[i] and a[j]"""
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp


if __name__ == '__main__':
    a = [4, 1, 2, 3]
    SelectionSort().sort(a)
    print(a)
