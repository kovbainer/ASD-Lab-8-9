def selection_sort(a):
    pos = 0
    moves = 0
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
            if pos == i:
                pos = m
                moves += 1
            elif pos == m:
                pos = i
                moves += 1
    return moves


n = int(input())
a = list(map(int, input().split()))
print(selection_sort(a))
