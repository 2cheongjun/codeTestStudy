n = int(input())
for i in range(n):
    num, t = input().split()
    text=''
    for i in t:
        text += int(num)*i
    print(text)