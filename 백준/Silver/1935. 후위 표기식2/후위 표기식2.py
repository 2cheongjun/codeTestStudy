n = int(input())
word = input()
numList = [0] * n
for i in range(n):
    numList[i] = int(input())
stack = []
for i in word:
    if 'A' <= i <= 'Z':
        stack.append(numList[ord(i) - ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()

        if i == '+':
            stack.append(n1 + n2)
        elif i == '-':
            stack.append(n1 - n2)
        elif i == '*':
            stack.append(n1 * n2)
        elif i == '/':
            stack.append(n1 / n2)
print('%.2f' % stack[0])