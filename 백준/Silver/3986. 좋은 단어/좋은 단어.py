N = int(input())
res = 0

for _ in range(N):
    temp = input().rstrip()
    stack = []

    for i in range(len(temp)):
        if stack and temp[i] == stack[-1]:
            stack.pop()

        else:
            stack.append(temp[i])

    if not stack:
        res += 1
print(res)
