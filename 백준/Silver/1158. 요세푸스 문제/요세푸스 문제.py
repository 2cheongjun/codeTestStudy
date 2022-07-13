from sys import stdin
from collections import deque

# n명,k번째 를 입력받음
n, k = map(int, stdin.readline().split())
# 덱에 1부터,n명 만큼 넣어준다.
queue = deque([i for i in range(1, n + 1)])
# 결과출력할 리스트
res = []
i = 0

# 큐가 있다면, i를 1씩 증가시킴
while queue:
	i += 1
	tmp = queue.popleft()
	if i % k != 0:
		queue.append(tmp)
	else:
		res.append(tmp)
s = ", ".join(map(str, res))
print('<' + s + '>')