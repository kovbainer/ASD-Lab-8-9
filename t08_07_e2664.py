def insertion_sort(a):
    out = []
    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:
            continue
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
        out.append(" ".join(map(str, a)))
    return out


n = int(input())
a = list(map(int, input().split()))
res = insertion_sort(a)
if res:
    print("\n".join(res))
