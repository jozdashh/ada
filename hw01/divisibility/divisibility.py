from sys import stdin,setrecursionlimit
setrecursionlimit(11000)

N, K, num = None, None, None

def solve(n, k, memo):
    global N, K, num
    ans = None
    if (n, k) in memo: ans = memo[(n, k)]
    else:
        if n == 0: ans = (k == 0)
        else:
            ans = solve(n-1,(k + num[n-1]) % K, memo) or solve(n-1,(k - num[n-1]) % K, memo)
            memo[(n, k)] = ans
    return ans

def main():
  global N, K, num
  tcnt = int(stdin.readline())
  while tcnt != 0:
    N,K = map(int, stdin.readline().split())
    num = list(map(int, stdin.readline().split()))
    memo = {}
    print('Divisible' if solve(N, 0, memo) else 'Not divisible')
    tcnt -= 1

main()
