# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 23/08/2019

from sys import stdin

INF = float('inf')

def bin_search(x, y, lo, hi):
    global Dict
    while lo <= hi:
        mid = lo + ((hi - lo) >> 1)
        if Dict[x][mid] <= y: lo = mid + 1
        else: hi = mid - 1
    return lo

def search(x, last):
    global Dict
    ans = -1
    if x in Dict:
        n = len(Dict[x])
        start = bin_search(x, last, 0, n-1)
        if start < n:
            ans = Dict[x][start]
    return ans

def solve(s):
    global Dict
    i, res, ans, n = 0, -INF, "", len(s)
    first, last = 0, 0
    while i < n and res != -1:
        res = search(s[i], res)
        i += 1
        if i == 1: first = res
        if i == n: last = res
    if res == -1: ans = "Not matched"
    else: ans = "Matched {} {}".format(first, last)
    return ans

def main():
    global Dict
    S = stdin.readline().strip()
    Dict = {}
    i = 0
    while i < len(S):
        if S[i] in Dict: Dict[S[i]].append(i)
        else: Dict[S[i]] = [i]
        i += 1
    tcnt = int(stdin.readline().strip())
    while tcnt != 0:
        s = stdin.readline().strip()
        print(solve(s))
        tcnt -= 1

main()
