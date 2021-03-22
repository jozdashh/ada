from sys import stdin

arr = [(i*(i + 1)) >> 1 for i in range(45500)]

def bin_search(x, lo, hi):
    while lo + 1 != hi:
        mid = lo + ((hi - lo) >> 1)
        if arr[mid] < x:
            lo = mid
        else: hi = mid
    return hi

def solve(k):
    i = bin_search(k, 0, len(arr))
    while (arr[i] - k) % 2 != 0: i += 1
    return i

def main():
    tcnt = int(stdin.readline())
    aux = tcnt
    while tcnt != 0:
        stdin.readline()
        k = int(stdin.readline())
        print(solve(abs(k)))
        tcnt -= 1
        if tcnt != 0:
            print("")

main()
