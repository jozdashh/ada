# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 13/08/2019

from sys import stdin
from collections import deque

def solve(A):
    lena = len(A)
    lis, lds = [None for _ in range(lena)], [None for _ in range(lena)]
    best = 0
    for n in range(lena):
        lis[n] = lds[n] = 1
        for i in range(n):
            if A[i] <= A[n] and lis[i] >= lis[n]: lis[n] = lis[i] + 1
            if A[i] >= A[n] and lds[i] >= lds[n]: lds[n] = lds[i] + 1
        best = max(best, lis[n] + lds[n] - 1)
    return best

def main():
    tcnt = int(stdin.readline())
    while tcnt != 0:
        n_wagons = int(stdin.readline())
        wagons = []
        while n_wagons != 0:
            wagons.append(int(stdin.readline()))
            n_wagons -= 1
        wagons.reverse()
        print(solve(wagons))
        tcnt -= 1

main()
