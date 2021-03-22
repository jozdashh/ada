def conflict(A, n, i):
  ans,j = False,0
  while ans==False and j!=n:
    ans,j = A[j]==i or n-j==i-A[j] or n-j==A[j]-i,j+1
  return ans

def solve(A, n, alll):
  if n==8: alll.append(list(A))
  else:
    for i in range(8):
      if conflict(A, n, i)==False:
        A[n] = i
        solve(A, n+1, alll)
        A[n] = None

def solve2(A, n, alll):
  if n==8: alll.append(list(A))
  else:
    if A[n]!=None:
      if conflict(A, n, A[n])==False:
        solve2(A, n+1, alll)
    else:
      for i in range(8):      
        if conflict(A, n, i)==False:
          A[n] = i
          solve2(A, n+1, alll)
          A[n] = None
