from sys import stdin

def solve(n):
    ans = 0
    while n != 0:
        if n % 2 == 0: n //= 2
        elif n == 3: n -= 1
        elif ((n - 1) / 2) % 2 == 0: n -= 1
        else: n += 1
        ans += 1
    return ans

def main():
    n = stdin.readline()
    while len(n)!=0:
        print(solve(int(n)))
        n = stdin.readline()

main()
