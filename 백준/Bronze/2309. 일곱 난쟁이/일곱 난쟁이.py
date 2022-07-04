arr = [int(input()) for _ in range(9)]

totalSum = sum(arr)
for i in range(9):
    totalSum -= arr[i]
    for j in range(i + 1, 9):
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
arr.sort()
print(*arr, sep="\n")
