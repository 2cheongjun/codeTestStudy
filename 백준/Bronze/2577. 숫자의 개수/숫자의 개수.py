*count함수
a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))

for i in range(10):
	print(result.count(str(i)))

	
	
*빈리스트 생성해 자릿수에 해당하는수가 있으면 넣어주기	
a = int(input())
b = int(input())
c = int(input())

result = a*b*c #17037300
li = [0]*10    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in str(result): #숫자를문자열로변환하고 문자열하나하나를 대조해서 result값과 일치하면            
    li[int(i)] += 1   #li의 cnt를 1씩 증가시킨다.
    
for i in li:
    print(i)



*
A=int(input())
B=int(input())
C=int(input())

D= str(A*B*C)

numbers=[0,1,2,3,4,5,6,7,8,9]
counter=[0]*10

for i in D:
    for j in numbers:
        if int(i) == j:
            counter[j]+=1

for i in counter:
    print(i)
