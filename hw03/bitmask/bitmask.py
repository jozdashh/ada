from sys import stdin

def solve(N, L, U):
    M = 0
    for i in range(31, -1, -1):
        if N & (1 << i) == 0 and M | (1 << i) <= U:
            M = M | (1 << i)
        elif N & (1 << i) > 0 and M | ((N & (1 << i)) - 1) < L:
            M = M | (1 << i)
    return M

def main():
    c = stdin.readline()
    while len(c)!=0:
        N, L, U = map(int, c.split())
        print(solve(N, L, U))
        c = stdin.readline()

main()
