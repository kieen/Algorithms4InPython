import sort_utils


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
                sort_utils.exchange(a, i, min_index)


if __name__ == '__main__':
    a = [4, 1, 2, 3]
    SelectionSort.sort(a)
    print(a)
