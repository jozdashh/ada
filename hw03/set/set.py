from sys import stdin

def solve(S, G, n):
    A, B = [], []
    for i in range(n):
        if S[i] <= G[i]: A.append(i)
        else: B.append(i)
    A.sort(key = lambda x: S[x])
    B.sort(key = lambda x: -G[x])
    L, s, total = A + B, 0, 0
    for i in range(n):
        s += S[L[i]]
        total = max(total, s)
        total += G[L[i]]
    return total

def main():
    n = stdin.readline()
    while len(n)!=0:
        n = int(n)
        S = list(map(int, stdin.readline().split()))
        G = list(map(int, stdin.readline().split()))
        print(solve(S, G, n))
        n = stdin.readline()

main()
