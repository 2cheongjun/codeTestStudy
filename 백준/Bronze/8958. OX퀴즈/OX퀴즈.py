n = int(input()) #테스트케이스

for i in range(n): #테스트케이스만큼 반복
    ox = list(input()) #ox문자열을 받아 리스트에 넣기
    sum = 0 #합
    cnt = 0 #누적카운트
    for x in ox:
        if x == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)