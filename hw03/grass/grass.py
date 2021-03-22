from sys import stdin
from math import sqrt

def solve(a, L, H):
    a.sort(key = lambda x: (x[0], x[1]))
    n, N = 0,len(a)
    low, ans = L, 0
    ok = True
    while n != N and ok and low < H:
        ok = a[n][0] <= low
        best, n = n, n+1
        while ok and n != N and a[n][0] <= low:
            if a[n][1] > a[best][1]: best = n
            n += 1
        ans += 1
        low = a[best][1]
    ok = ok and low >= H
    if not ok: ans = -1
    return ans

def main():
    c = stdin.readline()
    while len(c)!=0:
        n, l, w = map(int, c.split())
        S = []
        for i in range(n):
            x, r = map(int, stdin.readline().split())
            if r > (w/2):
                d = round(sqrt((r**2)-((w/2)**2)), 10)
                s, e = max(x - d, 0), x + d
                S.append((s, e))
        print(solve(S, 0, l))
        c = stdin.readline()

main()
