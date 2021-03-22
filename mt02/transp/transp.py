# Meh este no lo quise hacer. Estaba complicadito.

from sys import stdin,setrecursionlimit

def solve(orders,people,i,acum):
  global n,m,n_orders,best_profit
  if i==n_orders: best_profit = max(best_profit,acum)
  solve(orders,people,i+1,acum)
  st,ds,np = orders[i]
  cc, ok = st, True
  while ok and cc < ds:
    if n_people < people[cc]+np:
      for j in range(st,cc):
        people[j]-=1
      ok = False
      continue
    people[cc]+=np
    cc+=1
  if ok==True:
    solve(i+1,acum+(ds-st)*np)
    for j in range(st,ds): people[j]-=1

def main():
  global n,m,n_orders,best_profit
  n, m, n_orders = map(int, stdin.readline().split())
  while n!=0 and m!=0 and n_orders!=0:
    orders,people,best_profit = list(),[0 for _ in range(m+1)],-1
    for _ in range(n_orders):
      st, ds, np = map(int, stdin.readline().split())
      orders.append((st,ds,np))
    solve(orders,people,0,0)
    print(best_profit)
    n, m, n_orders = map(int, stdin.readline().split())

main()
