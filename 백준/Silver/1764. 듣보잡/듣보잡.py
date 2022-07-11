# 듣도 못한값 , 보도못한값을 입력받음
n, m = map(int, input().split())

a = set()# a를 set해줌
for i in range(n): #듣도못한사람길이 만큼 a에 넣어준다.
    a.add(input())

b = set()# b를 set해줌
for i in range(m): #보도못한사람길이 만큼 중복없이 b에 넣기
    b.add(input())

result = sorted(list(a & b)) #정렬(리스트에담아서 a,b의 교집합)을 담는다.

print(len(result)) #result의 길이 출력

for i in result: # result내용 출력
    print(i)