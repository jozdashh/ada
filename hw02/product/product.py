# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 10/08/2019

from sys import stdin

def solve(A):
    currnt_max_prodct = currnt_min_prodct = A[0]
    prev_max_prodct = prev_min_prodct = A[0]
    ans = A[0]
    for i in range(1, len(A)):
        currnt_max_prodct = max(prev_max_prodct * A[i], prev_min_prodct * A[i], A[i])
        currnt_min_prodct = min(prev_max_prodct * A[i], prev_min_prodct * A[i], A[i])
        prev_max_prodct = currnt_max_prodct
        prev_min_prodct = currnt_min_prodct
        ans = max(ans, currnt_max_prodct)
    return ans

def main():
    INPUT = list()
    for line in stdin: INPUT += list(map(int, line.strip().split()))
    aux = list()
    for tkn in INPUT:
        if tkn != -999999: aux.append(tkn)
        else: print(solve(aux)) ; aux = list()

main()
