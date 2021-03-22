from sys import stdin, setrecursionlimit
setrecursionlimit(5000)

INF = float('inf')

def phi(i, j, memo):
    global c
    if (i, j) in memo:
        ans = memo[(i, j)]
    else:
        ans = INF
        if i+1 == j:
            ans = 0
        else:
            for k in range(i+1, j):
                ans = min(ans, phi(i, k, memo) + phi(k, j, memo) + c[j]-c[i])
        memo[(i, j)] = ans
    return ans

def main():
    global c
    l = int(stdin.readline())
    while(l!=0):
        l, n, c, memo = int(l), int(stdin.readline()), [0], {}
        c += list(map(int, stdin.readline().split()))
        c.append(l)
        print("The minimum cutting is {}.".format(phi(0, len(c)-1, memo)))
        l = int(stdin.readline())

main()
