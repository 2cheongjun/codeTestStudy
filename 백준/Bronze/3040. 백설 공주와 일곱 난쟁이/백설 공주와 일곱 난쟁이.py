* 부르트포스 풀이 
arr = [int(input()) for _ in range(9)]

totalSum = sum(arr)
for i in range(9):
    totalSum -= arr[i]
    for j in range(i+1, 9):
        totalSum -= arr[j]
        if totalSum == 100:
            arr.remove(arr[j])
            arr.remove(arr[i])
            break
        totalSum += arr[j]
    else:
        totalSum += arr[i]
        continue
    break
print(*arr, sep="\n")



* 조합풀이
from itertools import combinations

list = [int(input()) for i in range(9)]
for i in combinations(list,7):
    if sum(i)==100:
        print(*i, sep='\n')
        break
