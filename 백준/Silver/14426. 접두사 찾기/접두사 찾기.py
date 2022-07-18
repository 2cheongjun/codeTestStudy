n, m = map(int, input().split())  # 문자열갯수, 검사할단어갯수입력받기
words = [input() for _ in range(n)] #문자열입력받기
test = [input() for _ in range(m)] #검사단어입력받기
answer = 0
for i in range(m):
    for j in range(n):#문자열과 검사할단어를 비교
        if words[j].startswith(test[i]): #문자열중에 검사단어로 시작되는 것이 있으면
            answer += 1 #+1을 더한다.
            break
print(answer)