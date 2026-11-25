def quick_sort(a, lo, hi):
    while lo < hi:
        pivot = a[(lo + hi) // 2]
        i, j = lo, hi
        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        if j - lo < hi - i:
            quick_sort(a, lo, j)
            lo = i
        else:
            quick_sort(a, i, hi)
            hi = j


n = int(input())
a = list(map(int, input().split()))
quick_sort(a, 0, n - 1)
print(*a)
