import sys
input = sys.stdin.readline

import heapq

N, M = map(int, input().split())
giftArray = list(map(int, input().split()))
wishArray = list(map(int, input().split()))

heap = []

for i in range(N):
    heapq.heappush(heap, - giftArray[i])

for i in range(M):
    wishCount = wishArray[i]

    maxCount = -heapq.heappop(heap)

    if wishCount > maxCount:
        print(0)
        exit(0)

    if wishCount == maxCount:
        continue

    # wishCount < maxCount
    remain = maxCount - wishCount
    heapq.heappush(heap, -remain)

print(1)



*방법2
import heapq as hq

n, m = map(int, input().split())
present = []
for x in list(map(int, input().split())):
    hq.heappush(present, -x) 
wish = list(map(int, input().split()))

ispre = False
for i in wish:
    x = -hq.heappop(present)
    if x - i < 0:
        ispre = True
        break
    hq.heappush(present, -(x-i))

if ispre:
    print(0)
else:
    print(1)
    
 
