hour, min = map(int, input().split())
add = int(input())

h = (hour + (min + add) // 60) % 24
m = (min + add) % 60

print(h,m)