from sys import stdin

INF = float('inf')

def test_solution(mmdist):
    global DC, N, K
    k, i, pivot = 0, 0, mmdist
    while i < N+1 and k <= K and mmdist-DC[i]>=0:
        if pivot >= DC[i]:
            pivot -= DC[i]
            i += 1
        else:
            k += 1
            pivot = mmdist
    return k <= K and i == N+1

def bin_search():
    global DC, N, K
    lo, hi, mmdist = 0, sum(DC), INF
    while lo+1 != hi:
        mid = lo + ((hi - lo) >> 1)
        if (test_solution(mid)):
            mmdist = min(mmdist, mid)
            hi = mid
        else: lo = mid
    return min(mmdist, hi)

def main():
    global DC, N, K
    tc = stdin.readline()
    while len(tc)!=0:
        N, K = map(int, tc.split())
        DC = []
        for i in range(N+1): DC.append(int(stdin.readline()))
        print(bin_search())
        tc = stdin.readline()

main()
