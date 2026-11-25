import sys


def merge_sort(a):
    n = len(a)
    buf = [0] * n
    width = 1
    while width < n:
        for lo in range(0, n, 2 * width):
            mid = min(lo + width, n)
            hi = min(lo + 2 * width, n)
            i, j, k = lo, mid, lo
            while i < mid and j < hi:
                if a[j] < a[i]:
                    buf[k] = a[j]
                    j += 1
                else:
                    buf[k] = a[i]
                    i += 1
                k += 1
            while i < mid:
                buf[k] = a[i]
                i += 1
                k += 1
            while j < hi:
                buf[k] = a[j]
                j += 1
                k += 1
        a, buf = buf, a
        width *= 2
    return a


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    keys = [0] * n
    for i in range(n):
        keys[i] = int(data[1 + 2 * i]) * 200000 + i
    keys = merge_sort(keys)
    out = []
    for k in keys:
        i = k % 200000
        out.append(data[1 + 2 * i].decode() + " " + data[2 + 2 * i].decode())
    sys.stdout.write("\n".join(out) + "\n")


main()
