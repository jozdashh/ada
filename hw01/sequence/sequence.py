"""
2 147 483 647 <= Problem index limit
2 147 523 711 <= Sk[31268]
"""

from sys import stdin

Sk = [0 for _ in range(31268 + 1)]
seq = "".join(str(i) for i in range(31268))

def bin_search(x):
    global Sk
    lo, hi  = 0, len(Sk)
    while lo <= hi:
        mid = lo + ((hi - lo) >> 1)
        if Sk[mid] <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

def gen_Sks():
    global Sk
    i, acc, n = 1, 0, len(Sk)
    while i < n:
        acc += len(str(i))
        Sk[i] = acc + Sk[i-1]
        i += 1

def solve(i):
    global Sk, seq
    k = bin_search(i)
    amnt = Sk[k - 1]
    if i - amnt == 0: amnt = Sk[k - 2]
    return seq[i - amnt]

def main():
    gen_Sks()
    tcnt = int(stdin.readline().strip())
    while tcnt!=0:
        i = int(stdin.readline().strip())
        print(solve(i))
        tcnt-=1

main()
