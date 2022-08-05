n = int(input())
num = list(map(int, input().split()))
maxnum = max(num)

result =[]
for score in num:
    result.append(score /maxnum*100)
avg = sum(result)/n
print(avg)