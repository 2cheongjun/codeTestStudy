import sys

n = int(sys.stdin.readline())
target = int(sys.stdin.readline())
m = [int(sys.stdin.readline()) for _ in range(1, n)]

buy = 0

if n == 1:
    print(0)

else:
    m.sort(reverse=True)
    while m[0] >= target:
        target += 1
        m[0] -= 1
        buy += 1
        m.sort(reverse=True)
    print(buy)
