def is_sorted(a):
    n = len(a)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            return False
    return True
