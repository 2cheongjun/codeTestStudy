T = int(input())

for _ in range(T):
    S = input()

    isVPS = True

    stack = []
    for e in S:
        if e == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                isVPS = False
                break

    if stack:
        isVPS = False

    if isVPS:
        print("YES")
    else:
        print("NO")



