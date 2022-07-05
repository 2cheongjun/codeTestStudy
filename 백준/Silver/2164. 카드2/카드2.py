from collections import deque

N = int(input())
q = deque()

for card in range(1, N+1):
    q.append(card)

while len(q) > 1:
    firstCard = q.popleft()
    secondCard = q.popleft()
    q.append(secondCard)

print(q.pop())