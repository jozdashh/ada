from sys import stdin

arr = [0 for _ in range(100000)]

def bin_search(x, lo, hi):
    while lo + 1 != hi:
        mid = lo + ((hi - lo) >> 1)
        if arr[mid] < x:
            lo = mid
        else:
            hi = mid
    return hi

def gen_arr():
    for i in range(1, len(arr)):
        arr[i] = ((i+1) >> 1) + arr[i-1]

def solve(x, y):
    if x - y == 0: ans = 0
    else: ans = bin_search(y - x, 0, len(arr))
    return ans

def main():
    gen_arr()
    tcnt = int(stdin.readline().strip())
    while tcnt != 0:
        x, y = stdin.readline().split()
        print(solve(int(x), int(y)))
        tcnt -= 1

main()
