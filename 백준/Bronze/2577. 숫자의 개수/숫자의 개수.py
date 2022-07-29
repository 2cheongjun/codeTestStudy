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
