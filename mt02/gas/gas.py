from sys import stdin

def mic_wf(L,H,a):
  a.sort()
  ans,low,n,ok,N = 0,L,0,True,len(a)
  while ok and low<H and n!=N:
    ok = a[n][0]<=low
    best,n = n,n+1
    while ok and n!=N and a[n][0]<=low:
      if a[n][1]>a[best][1]:
        best = n
      n += 1
    ans += 1
    low = a[best][1]
  ok = ok and low>=H
  if ok==False:
    ans = 0
  return ans

def main():
  L,G = map(int,stdin.readline().split())
  while L!=0 and G!=0:
    a = list()
    for i in range(G):
      x,r = map(int,stdin.readline().split())
      a.append((x-r,x+r))
    ans = mic_wf(0,L,a)
    print('{}'.format(G-ans if ans!=0 else -1))
    L,G = map(int,stdin.readline().split())
    
main()
