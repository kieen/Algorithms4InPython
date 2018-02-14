def is_sorted(a):
    n = len(a)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            return False
    return True


def exchange(a, i, j):
        """  exchange a[i] and a[j]"""
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
