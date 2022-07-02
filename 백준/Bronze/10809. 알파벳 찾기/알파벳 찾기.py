s = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in s:
        print(s.index(i), end = ' ')
    else:
        print(-1, end=' ')
        

// 단어를 입력받아서 list에 담는다.        
s = list(input())
// 비교할 알파벳
c = 'abcdefghijklmnopqrstuvwxyz'

// a부터 z까지 S에 그 알바벳이 있는지 검사한다.
for i in c:
    // 단어에 i가 있으면 인덱스를 출력
    if i in s:
        print(s.index(i), end = ' ')
    else:
        // 없으면  -1을 출력
        print(-1, end=' ')
        
