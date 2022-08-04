arr = [x for x in range(1,20+1)]
for _ in range(10):
    l, r = map (int, input().split())
    arr[l-1:r] = arr[l-1:r][::-1]
print(*arr)