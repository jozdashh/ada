all_solutions = list()

def is_valid_prefix(ans,n):
  """checks if the prefix ans[0..n] is valid for a configuration of
  non-attacking queens by assuming that ans[0..n) is a valid prefix
  """
  assert 0 <= n < 8
  ok, i = True,0
  while ok and i!=n:
    ok = not(ans[i]==ans[n] or (ans[n]>ans[i] and ans[n]-ans[i]==n-i) or (ans[n]<ans[i] and ans[i]-ans[n]==n-i))
    i += 1
  return ok

def find_solution(ans,n):
  """Builds all solutions to the 8-queens problem assuming that the
  prefix ans[0..n) is valid, i.e., there is no conflict among the
  queens located in column ans[0], ans[1], ..."""
  global all_solutions
  assert 0 <= n <= 8
  # print(ans,n)
  if n==8: all_solutions.append(list(ans))
  else:
    for i in range(8):
      ans[n] = i
      if is_valid_prefix(ans,n):
        find_solution(ans,n+1)
