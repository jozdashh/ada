# Estudiante: Josue Peña Atencio
# Código: 8935601
# Fecha: 13/08/2019

from sys import stdin, setrecursionlimit
setrecursionlimit(11000)

INF = float('inf')
D = list()

def phi_tabv2(X):
  """Coin change for denominations in D with tabulation and memory
     optimization"""
  N = len(D)
  tab = [ INF for x in range(20001) ] ; tab[0] = 0
  n,x = 1,20000
  while n!=N+1:
    if x==-1: n,x = n+1,20000
    else:
      if D[n-1]<=x: tab[x] = min(tab[x],1+tab[x-D[n-1]])
      x -= 1
  i = X
  while tab[i] == INF and i < 20001: i += 1
  return (i, tab[i])

def main():
    global D, i
    tcnt = int(stdin.readline())
    while tcnt != 0:
        x = int(stdin.readline())
        n = int(stdin.readline())
        for i in range(n): D.append(int(stdin.readline()))
        a, b = phi_tabv2(x)
        print(a, b)
        D = list()
        tcnt -= 1

main()
