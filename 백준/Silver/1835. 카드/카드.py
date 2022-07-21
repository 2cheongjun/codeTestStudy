from collections import deque

N = int(input())
dq = deque()

for i in range(N):
    card = N - i
    dq.appendleft(card)

    for _ in range(card):
        popCard = dq.pop()
        dq.appendleft(popCard)

print(*dq)


from collections import deque

N = int(input())
dq = deque() # 덱을사용

for i in range(N): 
    card = N - i # N-i 번만큼을 카드에 넣음
    dq.appendleft(card) #덱의 맨앞에 넣는다.1을 맨앞으로 이동

    for _ in range(card): # N-i번 반복
        popCard = dq.pop() # 맨마지막것을 뽑아서,popCard에 넣는다.
        dq.appendleft(popCard) #dq맨앞에 뽑은popCard를 넣는다.

print(*dq)
