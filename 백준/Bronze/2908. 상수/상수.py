*인덱스 활용
a, b = (input().split())
newa = int(a[2]+ a[1]+ a[0])
newb = int(b[2]+ b[1] +b[0])
print(max(newa, newb))


*reversed()활용
a, b = input().split()
print(max("".join(reversed(a)), "".join(reversed(b))))
