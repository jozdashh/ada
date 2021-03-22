# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 18/08/2019

from sys import stdin

INF = float('inf')

def solve(n, a, memo):
    if (n, a) in memo:
        ans = memo[(n, a)]
    else:
        ans = 0
        if n == 0 and a == 0:
            ans = 0
        elif n != 0 and a < 0:
            ans = INF
        elif n != 0 and 0 < a < 9:
            ans = min(solve(n-1, a, memo) + 30 - L[n-1][a-1],
                solve(n-1, a-1, memo) + 60 - L[n-1][a-1],
                solve(n-1, a+1, memo) + 20 - L[n-1][a-1])
        elif n != 0 and a == 0:
            ans = min(solve(n-1, a, memo)   + 30,
                      solve(n-1, a-1, memo) + 60)
        elif n != 0 and a == 9:
            ans = min(solve(n-1, a, memo)   + 30 - L[n-1][a-1],
                      solve(n-1, a+1, memo) + 20 - L[n-1][a-1])
        memo[(n, a)] = ans
    return ans

def main():
    global L
    tcnt = int(stdin.readline())
    stdin.readline()
    while tcnt != 0:
        X = int(stdin.readline())
        L = [None for _ in range(10)]
        memo = {}
        for i in range(10):
            L[i] = list(map(int, stdin.readline().split()))
        print(solve(X//100, 0, memo))
        print()
        tcnt -= 1
        if tcnt != 0:
            stdin.readline()

main()
