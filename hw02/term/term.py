# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 18/08/2019

from sys import stdin

INF = float('inf')

def solve(a, e, h, memo):
    global L
    ans = None
    if (a, e, h) in memo:
        ans = memo[(a, e, h)]
    else:
        if a == 0: ans = 0
        elif a != 0 and e == 0: ans = -INF
        elif a != 0 and e != 0 and L[a-1][e-1] < 5: ans = solve(a, e-1, h, memo)
        elif a != 0 and e != 0 and L[a-1][e-1] >= 5 and h < e: ans = solve(a, e-1, h, memo)
        elif a != 0 and e != 0 and L[a-1][e-1] >= 5 and h >= e:
            ans = max(solve(a, e-1, h, memo), L[a-1][e-1] + solve(a-1, h-e, h-e, memo))
        memo[(a, e, h)] = ans
    return ans

def main():
    global L
    tcnt = int(stdin.readline().strip())
    while tcnt != 0:
        A, E = map(int, stdin.readline().split())
        L = [None for _ in range(A)]
        memo = {}
        for i in range(A): L[i] = list(map(int, stdin.readline().split()))
        ans = solve(A, E, E, memo)
        if ans != -INF: print('Maximal possible average mark - {:.2f}.'.format(round(ans/A, 2)))
        else: print("Peter, you shouldn't have played billiard that much.")
        tcnt -= 1

main()
